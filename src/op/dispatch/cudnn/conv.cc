/*!
 * Copyright (c) 2019 by Contributors
 * \file src/op/dispatch/cudnn/conv.cc
 * \brief Manually-written cuDNN binding for conv2d
 */
#include "../../schema/nn.h"
#include "../../op_utils.h"
#include "./cudnn_utils.h"

namespace mnm {
namespace op {
namespace cudnn {
namespace manual {

using common::shape_utils::BytesCompactTensor;
using common::shape_utils::GetShape;
using common::shape_utils::MakeShape;
using ir::Array;
using ir::Attrs;
using value::Value;

MetaCache<cudnnConvolutionFwdAlgo_t> _conv_fwd_alg_cache;

cudnnConvolutionFwdAlgo_t FindConvolutionForwardAlgorithm(const std::vector<uint8_t>& key,
                                                          cudnnTensorDescriptor_t xDesc,
                                                          cudnnFilterDescriptor_t wDesc,
                                                          cudnnConvolutionDescriptor_t convDesc,
                                                          cudnnTensorDescriptor_t yDesc) {
  if (auto *val = _conv_fwd_alg_cache.Get(key)) {
    return *val;
  }
  int cnt;
  cudnnConvolutionFwdAlgoPerf_t res;
  CUDNN_CALL(cudnnFindConvolutionForwardAlgorithm(CUDNNThreadEntry::ThreadLocal()->handle, xDesc,
                                                  wDesc, convDesc, yDesc, 1, &cnt, &res));
  _conv_fwd_alg_cache.Set(key, res.algo);
  return res.algo;
}

class ConvCUDNN : public mnm::op::OpEnv {
 public:
  const void* alpha;
  cudnnTensorDescriptor_t x_desc;
  cudnnFilterDescriptor_t w_desc;
  cudnnConvolutionDescriptor_t conv_desc;
  cudnnConvolutionFwdAlgo_t algo;
  size_t ws_size;
  void* ws;
  const void* beta;
  cudnnTensorDescriptor_t y_desc;

  explicit ConvCUDNN(CallValues call) {
    const auto* args = call->args.as<mnm::op::schema::ConvArgs>();
    DLTensor* x = args->x;
    DLTensor* w = args->w;
    DLTensor* y = call->out;

    ir::TensorType x_tt = SquashTensorShape(x, {});
    ir::TensorType w_tt = SquashTensorShape(w, {});
    x_desc = NormalizeTensorType(x_tt);
    w_desc = NormalizeFilter(args->w);

    std::vector<int> padding = CastVector<int>(NormalizeScalarToTuple<2>(args->padding));
    std::vector<int> stride = CastVector<int>(NormalizeScalarToTuple<2>(args->stride));
    std::vector<int> dilation = CastVector<int>(NormalizeScalarToTuple<2>(args->dilation));

    CUDNN_CALL(cudnnCreateConvolutionDescriptor(&conv_desc));
    CUDNN_CALL(cudnnSetConvolutionNdDescriptor(conv_desc, padding.size(), dmlc::BeginPtr(padding),
                                               dmlc::BeginPtr(stride), dmlc::BeginPtr(dilation),
                                               CUDNN_CROSS_CORRELATION, CUDNNDType(y->dtype)));
    CUDNN_CALL(cudnnSetConvolutionGroupCount(conv_desc, args->groups));

    ir::TensorType y_tt = SquashTensorShape(y, {});
    y_desc = NormalizeTensorType(y_tt);

    HashKey hasher;
    hasher << x_tt  << w_tt << y_tt << args->padding << args->stride << args->dilation;

    const std::vector<uint8_t> &key = hasher.byte_vector;

    algo = FindConvolutionForwardAlgorithm(key, x_desc, w_desc, conv_desc, y_desc);
    CUDNN_CALL(cudnnGetConvolutionForwardWorkspaceSize(CUDNNThreadEntry::ThreadLocal()->handle,
                                                       x_desc, w_desc, conv_desc, y_desc, algo,
                                                       &ws_size));
    RequestWorkspace(&ws, call->ctx, ws_size);

    alpha = CUDNNDType(y->dtype).const_addr<1>();
    beta = CUDNNDType(y->dtype).const_addr<0>();
  }

  ~ConvCUDNN() {
    CUDNN_CALL(cudnnDestroyTensorDescriptor(x_desc));
    CUDNN_CALL(cudnnDestroyFilterDescriptor(w_desc));
    CUDNN_CALL(cudnnDestroyTensorDescriptor(y_desc));
    CUDNN_CALL(cudnnDestroyConvolutionDescriptor(conv_desc));
  }

  void Execute(const CallValues& call) final {
    const auto* args = call->args.as<mnm::op::schema::ConvArgs>();
    const DLTensor* x = args->x;
    const DLTensor* w = args->w;
    const DLTensor* y = call->out;
    CUDNN_CALL(cudnnConvolutionForward(CUDNNThreadEntry::ThreadLocal()->handle, alpha, x_desc,
                                       x->data, w_desc, w->data, conv_desc, algo, ws, ws_size, beta,
                                       y_desc, y->data));
    CUDA_CALL(cudaDeviceSynchronize());
  }

  static OpEnv* make(const CallValues& call) {
    std::unique_ptr<ConvCUDNN> res = std::make_unique<ConvCUDNN>(call);
    return res.release();
  }
};

// TODO(@were): Uncomment below when testing op priority.
// MNM_OP_DISPATCH("mnm.op.conv2d", ConvCUDNN, DevType::kCUDA(), "manual_cudnn");

}  // namespace manual
}  // namespace cudnn
}  // namespace op
}  // namespace mnm
