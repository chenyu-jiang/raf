# pylint: disable=invalid-name,line-too-long, too-many-lines
# pylint: disable=too-many-arguments,redefined-builtin,redefined-outer-name
# pylint: disable=missing-class-docstring,missing-function-docstring
# pylint: disable=protected-access
"""Auto generated. Do not touch."""
import mnm._ffi.op.imp as ffi
from mnm._core.core_utils import set_module
from . import imp_utils

__all__ = [
    "_allreduce", "abs", "adaptive_avg_pool2d", "adaptive_avg_pool2d_dx", "adaptive_max_pool2d",
    "adaptive_max_pool2d_dx", "add", "all", "any", "argmax",
    "argmin", "argsort", "atan", "avg_pool2d", "avg_pool2d_dx",
    "batch_flatten", "batch_matmul", "batch_norm_infer", "batch_norm_train", "batch_norm_train_dxwb",
    "bias_add", "broadcast_to", "broadcast_to_like", "cast", "cast_like",
    "ceil", "clip", "clip_dx", "collapse_sum_like", "compiler_begin",
    "compiler_end", "concatenate", "concatenate_dx", "conv2d", "conv2d_dw",
    "conv2d_dx", "copy", "cos", "cross_entropy", "cross_entropy_dpred",
    "cross_entropy_dtrue", "dense", "device_copy", "divide", "equal",
    "erf", "erf_dx", "exp", "expand_dims", "floor",
    "full", "gather", "gather_dx", "gather_nd", "gather_nd_dx",
    "get_kept_dims", "get_reduce_axis", "get_valid_counts", "greater", "greater_equal",
    "layer_norm", "layer_norm_dx", "less", "less_equal", "log",
    "log_softmax", "log_softmax_dx", "logical_and", "logical_not", "matmul",
    "matmul_nt", "matmul_tn", "matmul_tt", "max", "max_pool2d",
    "max_pool2d_dx", "maximum", "mean", "mean_dx", "min",
    "minimum", "mod", "multiply", "negative", "nll_loss",
    "nll_loss_dpred", "nll_loss_dtrue", "non_max_suppression", "not_equal", "one_hot",
    "ones", "ones_like", "pad", "power", "prod",
    "relu", "relu_dx", "repeat", "reshape", "reverse",
    "reverse_sequence", "round", "rsqrt", "sequence_mask", "sgd",
    "shape", "sigmoid", "sigmoid_dx", "sign", "sin",
    "smooth_l1_loss", "smooth_l1_loss_dpred", "smooth_l1_loss_dtrue", "softmax", "softmax_dx",
    "sort", "split", "sqrt", "sqrt_dx", "squeeze",
    "stack", "stack_dx", "stream_sync", "strided_slice", "subtract",
    "sum", "take", "take_dx", "tanh", "tanh_dx",
    "transpose", "transpose_dx", "where", "zeros", "zeros_like",
]

@set_module("mnm")
def _allreduce(x):
    x = imp_utils.to_tensor_tuple(x)
    return imp_utils.ret(ffi._allreduce(x))

@set_module("mnm")
def abs(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.abs(x))

@set_module("mnm")
def adaptive_avg_pool2d(x, shape, layout="NCHW"):
    x = imp_utils.to_tensor(x)
    shape = imp_utils.to_int_tuple(shape)
    layout = imp_utils.to_string(layout)
    return imp_utils.ret(ffi.adaptive_avg_pool2d(x, shape, layout))

@set_module("mnm")
def adaptive_avg_pool2d_dx(x, y, dy, shape):
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    shape = imp_utils.to_int_tuple(shape)
    return imp_utils.ret(ffi.adaptive_avg_pool2d_dx(x, y, dy, shape))

@set_module("mnm")
def adaptive_max_pool2d(x, shape, layout="NCHW"):
    x = imp_utils.to_tensor(x)
    shape = imp_utils.to_int_tuple(shape)
    layout = imp_utils.to_string(layout)
    return imp_utils.ret(ffi.adaptive_max_pool2d(x, shape, layout))

@set_module("mnm")
def adaptive_max_pool2d_dx(x, y, dy, shape):
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    shape = imp_utils.to_int_tuple(shape)
    return imp_utils.ret(ffi.adaptive_max_pool2d_dx(x, y, dy, shape))

@set_module("mnm")
def add(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.add(x1, x2, out, where))

@set_module("mnm")
def all(x, axis=(), keepdims=False):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int_tuple(axis)
    keepdims = imp_utils.to_bool(keepdims)
    return imp_utils.ret(ffi.all(x, axis, keepdims))

@set_module("mnm")
def any(x, axis=(), keepdims=False):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int_tuple(axis)
    keepdims = imp_utils.to_bool(keepdims)
    return imp_utils.ret(ffi.any(x, axis, keepdims))

@set_module("mnm")
def argmax(x, axis=(), keepdims=False):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int_tuple(axis)
    keepdims = imp_utils.to_bool(keepdims)
    return imp_utils.ret(ffi.argmax(x, axis, keepdims))

@set_module("mnm")
def argmin(x, axis=(), keepdims=False):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int_tuple(axis)
    keepdims = imp_utils.to_bool(keepdims)
    return imp_utils.ret(ffi.argmin(x, axis, keepdims))

@set_module("mnm")
def argsort(data, axis=-1, is_ascend=True, dtype="int32"):
    data = imp_utils.to_tensor(data)
    axis = imp_utils.to_int(axis)
    is_ascend = imp_utils.to_bool(is_ascend)
    dtype = imp_utils.to_string(dtype)
    return imp_utils.ret(ffi.argsort(data, axis, is_ascend, dtype))

@set_module("mnm")
def atan(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.atan(x))

@set_module("mnm")
def avg_pool2d(x, kernel, stride, padding=0, dilation=1, ceil_mode=False, include_pad=True, layout="NCHW"):
    x = imp_utils.to_tensor(x)
    kernel = imp_utils.to_int_tuple(kernel)
    stride = imp_utils.to_int_tuple(stride)
    padding = imp_utils.to_int_tuple(padding)
    dilation = imp_utils.to_int_tuple(dilation)
    ceil_mode = imp_utils.to_bool(ceil_mode)
    include_pad = imp_utils.to_bool(include_pad)
    layout = imp_utils.to_string(layout)
    return imp_utils.ret(ffi.avg_pool2d(x, kernel, stride, padding, dilation, ceil_mode, include_pad, layout))

@set_module("mnm")
def avg_pool2d_dx(x, y, dy, kernel, stride, padding, dilation, ceil_mode, include_pad):
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    kernel = imp_utils.to_int_tuple(kernel)
    stride = imp_utils.to_int_tuple(stride)
    padding = imp_utils.to_int_tuple(padding)
    dilation = imp_utils.to_int_tuple(dilation)
    ceil_mode = imp_utils.to_bool(ceil_mode)
    include_pad = imp_utils.to_bool(include_pad)
    return imp_utils.ret(ffi.avg_pool2d_dx(x, y, dy, kernel, stride, padding, dilation, ceil_mode, include_pad))

@set_module("mnm")
def batch_flatten(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.batch_flatten(x))

@set_module("mnm")
def batch_matmul(x1, x2):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    return imp_utils.ret(ffi.batch_matmul(x1, x2))

@set_module("mnm")
def batch_norm_infer(x, running_mean, running_var, w=None, b=None, momentum=0.1, eps=1e-05):
    x = imp_utils.to_tensor(x)
    running_mean = imp_utils.to_tensor(running_mean)
    running_var = imp_utils.to_tensor(running_var)
    w = imp_utils.to_tensor(w)
    b = imp_utils.to_tensor(b)
    momentum = imp_utils.to_double(momentum)
    eps = imp_utils.to_double(eps)
    return imp_utils.ret(ffi.batch_norm_infer(x, running_mean, running_var, w, b, momentum, eps))

@set_module("mnm")
def batch_norm_train(x, running_mean, running_var, w=None, b=None, momentum=0.1, eps=1e-05):
    x = imp_utils.to_tensor(x)
    running_mean = imp_utils.to_tensor(running_mean)
    running_var = imp_utils.to_tensor(running_var)
    w = imp_utils.to_tensor(w)
    b = imp_utils.to_tensor(b)
    momentum = imp_utils.to_double(momentum)
    eps = imp_utils.to_double(eps)
    return imp_utils.ret(ffi.batch_norm_train(x, running_mean, running_var, w, b, momentum, eps))

@set_module("mnm")
def batch_norm_train_dxwb(dy, x, w, b, eps):
    dy = imp_utils.to_tensor(dy)
    x = imp_utils.to_tensor(x)
    w = imp_utils.to_tensor(w)
    b = imp_utils.to_tensor(b)
    eps = imp_utils.to_double(eps)
    return imp_utils.ret(ffi.batch_norm_train_dxwb(dy, x, w, b, eps))

@set_module("mnm")
def bias_add(x, bias, axis=1):
    x = imp_utils.to_tensor(x)
    bias = imp_utils.to_tensor(bias)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.bias_add(x, bias, axis))

@set_module("mnm")
def broadcast_to(x, shape):
    x = imp_utils.to_tensor(x)
    shape = imp_utils.to_int_tuple(shape)
    return imp_utils.ret(ffi.broadcast_to(x, shape))

@set_module("mnm")
def broadcast_to_like(x, broadcast_type):
    x = imp_utils.to_tensor(x)
    broadcast_type = imp_utils.to_tensor(broadcast_type)
    return imp_utils.ret(ffi.broadcast_to_like(x, broadcast_type))

@set_module("mnm")
def cast(data, dtype):
    data = imp_utils.to_tensor(data)
    dtype = imp_utils.to_string(dtype)
    return imp_utils.ret(ffi.cast(data, dtype))

@set_module("mnm")
def cast_like(data, dtype_like):
    data = imp_utils.to_tensor(data)
    dtype_like = imp_utils.to_tensor(dtype_like)
    return imp_utils.ret(ffi.cast_like(data, dtype_like))

@set_module("mnm")
def ceil(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.ceil(x))

@set_module("mnm")
def clip(x, a_min, a_max):
    x = imp_utils.to_tensor(x)
    a_min = imp_utils.to_double(a_min)
    a_max = imp_utils.to_double(a_max)
    return imp_utils.ret(ffi.clip(x, a_min, a_max))

@set_module("mnm")
def clip_dx(x, dy, a_min, a_max):
    x = imp_utils.to_tensor(x)
    dy = imp_utils.to_tensor(dy)
    a_min = imp_utils.to_double(a_min)
    a_max = imp_utils.to_double(a_max)
    return imp_utils.ret(ffi.clip_dx(x, dy, a_min, a_max))

@set_module("mnm")
def collapse_sum_like(x, shape):
    x = imp_utils.to_tensor(x)
    shape = imp_utils.to_int_tuple(shape)
    return imp_utils.ret(ffi.collapse_sum_like(x, shape))

@set_module("mnm")
def compiler_begin(x, compiler):
    x = imp_utils.to_tensor(x)
    compiler = imp_utils.to_string(compiler)
    return imp_utils.ret(ffi.compiler_begin(x, compiler))

@set_module("mnm")
def compiler_end(x, compiler):
    x = imp_utils.to_tensor(x)
    compiler = imp_utils.to_string(compiler)
    return imp_utils.ret(ffi.compiler_end(x, compiler))

@set_module("mnm")
def concatenate(x, axis=0):
    x = imp_utils.to_tensor_tuple(x)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.concatenate(x, axis))

@set_module("mnm")
def concatenate_dx(x, axis=0):
    x = imp_utils.to_tensor_tuple(x)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.concatenate_dx(x, axis))

@set_module("mnm")
def conv2d(x, w, stride=1, padding=0, dilation=1, groups=1, layout="NCHW", kernel_layout="OIHW", out_layout="NCHW"):
    x = imp_utils.to_tensor(x)
    w = imp_utils.to_tensor(w)
    stride = imp_utils.to_int_tuple(stride)
    padding = imp_utils.to_int_tuple(padding)
    dilation = imp_utils.to_int_tuple(dilation)
    groups = imp_utils.to_int(groups)
    layout = imp_utils.to_string(layout)
    kernel_layout = imp_utils.to_string(kernel_layout)
    out_layout = imp_utils.to_string(out_layout)
    return imp_utils.ret(ffi.conv2d(x, w, stride, padding, dilation, groups, layout, kernel_layout, out_layout))

@set_module("mnm")
def conv2d_dw(x_or_w, y, dy, shape, stride, padding, dilation, groups):
    x_or_w = imp_utils.to_tensor(x_or_w)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    shape = imp_utils.to_int_tuple(shape)
    stride = imp_utils.to_int_tuple(stride)
    padding = imp_utils.to_int_tuple(padding)
    dilation = imp_utils.to_int_tuple(dilation)
    groups = imp_utils.to_int(groups)
    return imp_utils.ret(ffi.conv2d_dw(x_or_w, y, dy, shape, stride, padding, dilation, groups))

@set_module("mnm")
def conv2d_dx(x_or_w, y, dy, shape, stride, padding, dilation, groups):
    x_or_w = imp_utils.to_tensor(x_or_w)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    shape = imp_utils.to_int_tuple(shape)
    stride = imp_utils.to_int_tuple(stride)
    padding = imp_utils.to_int_tuple(padding)
    dilation = imp_utils.to_int_tuple(dilation)
    groups = imp_utils.to_int(groups)
    return imp_utils.ret(ffi.conv2d_dx(x_or_w, y, dy, shape, stride, padding, dilation, groups))

@set_module("mnm")
def copy(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.copy(x))

@set_module("mnm")
def cos(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.cos(x))

@set_module("mnm")
def cross_entropy(y_true, y_pred):
    y_true = imp_utils.to_tensor(y_true)
    y_pred = imp_utils.to_tensor(y_pred)
    return imp_utils.ret(ffi.cross_entropy(y_true, y_pred))

@set_module("mnm")
def cross_entropy_dpred(y_true, y_pred):
    y_true = imp_utils.to_tensor(y_true)
    y_pred = imp_utils.to_tensor(y_pred)
    return imp_utils.ret(ffi.cross_entropy_dpred(y_true, y_pred))

@set_module("mnm")
def cross_entropy_dtrue(y_true, y_pred):
    y_true = imp_utils.to_tensor(y_true)
    y_pred = imp_utils.to_tensor(y_pred)
    return imp_utils.ret(ffi.cross_entropy_dtrue(y_true, y_pred))

@set_module("mnm")
def dense(x1, x2):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    return imp_utils.ret(ffi.dense(x1, x2))

@set_module("mnm")
def device_copy(data, src_dev_type=0, dst_dev_type=0):
    data = imp_utils.to_tensor(data)
    src_dev_type = imp_utils.to_int(src_dev_type)
    dst_dev_type = imp_utils.to_int(dst_dev_type)
    return imp_utils.ret(ffi.device_copy(data, src_dev_type, dst_dev_type))

@set_module("mnm")
def divide(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.divide(x1, x2, out, where))

@set_module("mnm")
def equal(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.equal(x1, x2, out, where))

@set_module("mnm")
def erf(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.erf(x))

@set_module("mnm")
def erf_dx(x, y, dy):
    x = imp_utils.to_any(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    return imp_utils.ret(ffi.erf_dx(x, y, dy))

@set_module("mnm")
def exp(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.exp(x))

@set_module("mnm")
def expand_dims(x, axis, num_newaxis=1):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int(axis)
    num_newaxis = imp_utils.to_int(num_newaxis)
    return imp_utils.ret(ffi.expand_dims(x, axis, num_newaxis))

@set_module("mnm")
def floor(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.floor(x))

@set_module("mnm")
def full(fill_value, shape, dtype="int32"):
    fill_value = imp_utils.to_tensor(fill_value)
    shape = imp_utils.to_int_tuple(shape)
    dtype = imp_utils.to_string(dtype)
    return imp_utils.ret(ffi.full(fill_value, shape, dtype))

@set_module("mnm")
def gather(data, axis, indices):
    data = imp_utils.to_tensor(data)
    axis = imp_utils.to_int(axis)
    indices = imp_utils.to_tensor(indices)
    return imp_utils.ret(ffi.gather(data, axis, indices))

@set_module("mnm")
def gather_dx(data, axis, indices, dy):
    data = imp_utils.to_tensor(data)
    axis = imp_utils.to_int(axis)
    indices = imp_utils.to_tensor(indices)
    dy = imp_utils.to_tensor(dy)
    return imp_utils.ret(ffi.gather_dx(data, axis, indices, dy))

@set_module("mnm")
def gather_nd(data, indices):
    data = imp_utils.to_tensor(data)
    indices = imp_utils.to_tensor(indices)
    return imp_utils.ret(ffi.gather_nd(data, indices))

@set_module("mnm")
def gather_nd_dx(data, indices, dy):
    data = imp_utils.to_tensor(data)
    indices = imp_utils.to_tensor(indices)
    dy = imp_utils.to_tensor(dy)
    return imp_utils.ret(ffi.gather_nd_dx(data, indices, dy))

@set_module("mnm")
def get_kept_dims(x1, x2):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    return imp_utils.ret(ffi.get_kept_dims(x1, x2))

@set_module("mnm")
def get_reduce_axis(x1, x2):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    return imp_utils.ret(ffi.get_reduce_axis(x1, x2))

@set_module("mnm")
def get_valid_counts(data, score_threshold, id_index=0, score_index=1):
    data = imp_utils.to_tensor(data)
    score_threshold = imp_utils.to_tensor(score_threshold)
    id_index = imp_utils.to_int(id_index)
    score_index = imp_utils.to_int(score_index)
    return imp_utils.ret(ffi.get_valid_counts(data, score_threshold, id_index, score_index))

@set_module("mnm")
def greater(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.greater(x1, x2, out, where))

@set_module("mnm")
def greater_equal(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.greater_equal(x1, x2, out, where))

@set_module("mnm")
def layer_norm(x, axis=-1, eps=1e-05):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int(axis)
    eps = imp_utils.to_double(eps)
    return imp_utils.ret(ffi.layer_norm(x, axis, eps))

@set_module("mnm")
def layer_norm_dx(x, y, dy, axis=-1, eps=1e-05):
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    axis = imp_utils.to_int(axis)
    eps = imp_utils.to_double(eps)
    return imp_utils.ret(ffi.layer_norm_dx(x, y, dy, axis, eps))

@set_module("mnm")
def less(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.less(x1, x2, out, where))

@set_module("mnm")
def less_equal(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.less_equal(x1, x2, out, where))

@set_module("mnm")
def log(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.log(x))

@set_module("mnm")
def log_softmax(x, axis=-1):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.log_softmax(x, axis))

@set_module("mnm")
def log_softmax_dx(x, y, dy, axis=-1):
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.log_softmax_dx(x, y, dy, axis))

@set_module("mnm")
def logical_and(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.logical_and(x1, x2, out, where))

@set_module("mnm")
def logical_not(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.logical_not(x))

@set_module("mnm")
def matmul(x1, x2):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    return imp_utils.ret(ffi.matmul(x1, x2))

@set_module("mnm")
def matmul_nt(x1, x2):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    return imp_utils.ret(ffi.matmul_nt(x1, x2))

@set_module("mnm")
def matmul_tn(x1, x2):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    return imp_utils.ret(ffi.matmul_tn(x1, x2))

@set_module("mnm")
def matmul_tt(x1, x2):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    return imp_utils.ret(ffi.matmul_tt(x1, x2))

@set_module("mnm")
def max(x, axis=(), keepdims=False):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int_tuple(axis)
    keepdims = imp_utils.to_bool(keepdims)
    return imp_utils.ret(ffi.max(x, axis, keepdims))

@set_module("mnm")
def max_pool2d(x, kernel, stride, padding=0, dilation=1, ceil_mode=False, include_pad=True, layout="NCHW"):
    x = imp_utils.to_tensor(x)
    kernel = imp_utils.to_int_tuple(kernel)
    stride = imp_utils.to_int_tuple(stride)
    padding = imp_utils.to_int_tuple(padding)
    dilation = imp_utils.to_int_tuple(dilation)
    ceil_mode = imp_utils.to_bool(ceil_mode)
    include_pad = imp_utils.to_bool(include_pad)
    layout = imp_utils.to_string(layout)
    return imp_utils.ret(ffi.max_pool2d(x, kernel, stride, padding, dilation, ceil_mode, include_pad, layout))

@set_module("mnm")
def max_pool2d_dx(x, y, dy, kernel, stride, padding, dilation, ceil_mode, include_pad):
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    kernel = imp_utils.to_int_tuple(kernel)
    stride = imp_utils.to_int_tuple(stride)
    padding = imp_utils.to_int_tuple(padding)
    dilation = imp_utils.to_int_tuple(dilation)
    ceil_mode = imp_utils.to_bool(ceil_mode)
    include_pad = imp_utils.to_bool(include_pad)
    return imp_utils.ret(ffi.max_pool2d_dx(x, y, dy, kernel, stride, padding, dilation, ceil_mode, include_pad))

@set_module("mnm")
def maximum(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.maximum(x1, x2, out, where))

@set_module("mnm")
def mean(x, axis=(), keepdims=False):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int_tuple(axis)
    keepdims = imp_utils.to_bool(keepdims)
    return imp_utils.ret(ffi.mean(x, axis, keepdims))

@set_module("mnm")
def mean_dx(x, y, dy, axis=(), keepdims=False):
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    axis = imp_utils.to_int_tuple(axis)
    keepdims = imp_utils.to_bool(keepdims)
    return imp_utils.ret(ffi.mean_dx(x, y, dy, axis, keepdims))

@set_module("mnm")
def min(x, axis=(), keepdims=False):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int_tuple(axis)
    keepdims = imp_utils.to_bool(keepdims)
    return imp_utils.ret(ffi.min(x, axis, keepdims))

@set_module("mnm")
def minimum(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.minimum(x1, x2, out, where))

@set_module("mnm")
def mod(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.mod(x1, x2, out, where))

@set_module("mnm")
def multiply(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.multiply(x1, x2, out, where))

@set_module("mnm")
def negative(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.negative(x))

@set_module("mnm")
def nll_loss(y_true, y_pred):
    y_true = imp_utils.to_tensor(y_true)
    y_pred = imp_utils.to_tensor(y_pred)
    return imp_utils.ret(ffi.nll_loss(y_true, y_pred))

@set_module("mnm")
def nll_loss_dpred(dy, y_true, y_pred):
    dy = imp_utils.to_tensor(dy)
    y_true = imp_utils.to_tensor(y_true)
    y_pred = imp_utils.to_tensor(y_pred)
    return imp_utils.ret(ffi.nll_loss_dpred(dy, y_true, y_pred))

@set_module("mnm")
def nll_loss_dtrue(dy, y_true, y_pred):
    dy = imp_utils.to_tensor(dy)
    y_true = imp_utils.to_tensor(y_true)
    y_pred = imp_utils.to_tensor(y_pred)
    return imp_utils.ret(ffi.nll_loss_dtrue(dy, y_true, y_pred))

@set_module("mnm")
def non_max_suppression(data, valid_count, indices, max_output_size, iou_threshold, force_suppress=False, top_k=-1, coord_start=2, score_index=1, id_index=0, return_indices=True, invalid_to_bottom=False):
    data = imp_utils.to_tensor(data)
    valid_count = imp_utils.to_tensor(valid_count)
    indices = imp_utils.to_tensor(indices)
    max_output_size = imp_utils.to_tensor(max_output_size)
    iou_threshold = imp_utils.to_tensor(iou_threshold)
    force_suppress = imp_utils.to_bool(force_suppress)
    top_k = imp_utils.to_int(top_k)
    coord_start = imp_utils.to_int(coord_start)
    score_index = imp_utils.to_int(score_index)
    id_index = imp_utils.to_int(id_index)
    return_indices = imp_utils.to_bool(return_indices)
    invalid_to_bottom = imp_utils.to_bool(invalid_to_bottom)
    return imp_utils.ret(ffi.non_max_suppression(data, valid_count, indices, max_output_size, iou_threshold, force_suppress, top_k, coord_start, score_index, id_index, return_indices, invalid_to_bottom))

@set_module("mnm")
def not_equal(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.not_equal(x1, x2, out, where))

@set_module("mnm")
def one_hot(indices, on_value, off_value, depth, axis=-1, dtype="int32", device="cpu"):
    indices = imp_utils.to_tensor(indices)
    on_value = imp_utils.to_tensor(on_value)
    off_value = imp_utils.to_tensor(off_value)
    depth = imp_utils.to_int(depth)
    axis = imp_utils.to_int(axis)
    dtype = imp_utils.to_string(dtype)
    device = imp_utils.to_string(device)
    return imp_utils.ret(ffi.one_hot(indices, on_value, off_value, depth, axis, dtype, device))

@set_module("mnm")
def ones(shape, dtype="int32", device="cpu"):
    shape = imp_utils.to_int_tuple(shape)
    dtype = imp_utils.to_string(dtype)
    device = imp_utils.to_string(device)
    return imp_utils.ret(ffi.ones(shape, dtype, device))

@set_module("mnm")
def ones_like(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.ones_like(x))

@set_module("mnm")
def pad(x, pad_width, pad_value=0.0, pad_mode="constant"):
    x = imp_utils.to_tensor(x)
    pad_width = imp_utils.to_int_tuple(pad_width)
    pad_value = imp_utils.to_double(pad_value)
    pad_mode = imp_utils.to_string(pad_mode)
    return imp_utils.ret(ffi.pad(x, pad_width, pad_value, pad_mode))

@set_module("mnm")
def power(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.power(x1, x2, out, where))

@set_module("mnm")
def prod(x, axis=(), keepdims=False):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int_tuple(axis)
    keepdims = imp_utils.to_bool(keepdims)
    return imp_utils.ret(ffi.prod(x, axis, keepdims))

@set_module("mnm")
def relu(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.relu(x))

@set_module("mnm")
def relu_dx(x, y, dy):
    x = imp_utils.to_any(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    return imp_utils.ret(ffi.relu_dx(x, y, dy))

@set_module("mnm")
def repeat(x, repeats, axis=None):
    x = imp_utils.to_tensor(x)
    repeats = imp_utils.to_int(repeats)
    axis = imp_utils.to_any(axis)
    return imp_utils.ret(ffi.repeat(x, repeats, axis))

@set_module("mnm")
def reshape(x, shape, reverse=False):
    x = imp_utils.to_tensor(x)
    shape = imp_utils.to_int_tuple(shape)
    reverse = imp_utils.to_bool(reverse)
    return imp_utils.ret(ffi.reshape(x, shape, reverse))

@set_module("mnm")
def reverse(x, axis=0):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.reverse(x, axis))

@set_module("mnm")
def reverse_sequence(x, sequence_length, seq_axis=1, batch_axis=0):
    x = imp_utils.to_tensor(x)
    sequence_length = imp_utils.to_tensor(sequence_length)
    seq_axis = imp_utils.to_int(seq_axis)
    batch_axis = imp_utils.to_int(batch_axis)
    return imp_utils.ret(ffi.reverse_sequence(x, sequence_length, seq_axis, batch_axis))

@set_module("mnm")
def round(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.round(x))

@set_module("mnm")
def rsqrt(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.rsqrt(x))

@set_module("mnm")
def sequence_mask(x, sequence_length, mask_value=0.0, axis=0):
    x = imp_utils.to_tensor(x)
    sequence_length = imp_utils.to_tensor(sequence_length)
    mask_value = imp_utils.to_double(mask_value)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.sequence_mask(x, sequence_length, mask_value, axis))

@set_module("mnm")
def sgd(x, dx, v, learning_rate, mu):
    x = imp_utils.to_tensor(x)
    dx = imp_utils.to_tensor(dx)
    v = imp_utils.to_tensor(v)
    learning_rate = imp_utils.to_double(learning_rate)
    mu = imp_utils.to_double(mu)
    return imp_utils.ret(ffi.sgd(x, dx, v, learning_rate, mu))

@set_module("mnm")
def shape(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.shape(x))

@set_module("mnm")
def sigmoid(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.sigmoid(x))

@set_module("mnm")
def sigmoid_dx(x, y, dy):
    x = imp_utils.to_any(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    return imp_utils.ret(ffi.sigmoid_dx(x, y, dy))

@set_module("mnm")
def sign(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.sign(x))

@set_module("mnm")
def sin(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.sin(x))

@set_module("mnm")
def smooth_l1_loss(y_true, y_pred):
    y_true = imp_utils.to_tensor(y_true)
    y_pred = imp_utils.to_tensor(y_pred)
    return imp_utils.ret(ffi.smooth_l1_loss(y_true, y_pred))

@set_module("mnm")
def smooth_l1_loss_dpred(y_true, y_pred):
    y_true = imp_utils.to_tensor(y_true)
    y_pred = imp_utils.to_tensor(y_pred)
    return imp_utils.ret(ffi.smooth_l1_loss_dpred(y_true, y_pred))

@set_module("mnm")
def smooth_l1_loss_dtrue(y_true, y_pred):
    y_true = imp_utils.to_tensor(y_true)
    y_pred = imp_utils.to_tensor(y_pred)
    return imp_utils.ret(ffi.smooth_l1_loss_dtrue(y_true, y_pred))

@set_module("mnm")
def softmax(x, axis=-1):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.softmax(x, axis))

@set_module("mnm")
def softmax_dx(x, y, dy, axis=-1):
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.softmax_dx(x, y, dy, axis))

@set_module("mnm")
def sort(data, axis=-1, is_ascend=True):
    data = imp_utils.to_tensor(data)
    axis = imp_utils.to_int(axis)
    is_ascend = imp_utils.to_bool(is_ascend)
    return imp_utils.ret(ffi.sort(data, axis, is_ascend))

@set_module("mnm")
def split(x, indices_or_sections=None, axis=0):
    x = imp_utils.to_tensor(x)
    indices_or_sections = imp_utils.to_any(indices_or_sections)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.split(x, indices_or_sections, axis))

@set_module("mnm")
def sqrt(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.sqrt(x))

@set_module("mnm")
def sqrt_dx(x, y, dy):
    x = imp_utils.to_any(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    return imp_utils.ret(ffi.sqrt_dx(x, y, dy))

@set_module("mnm")
def squeeze(x, axis=None):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int_tuple(axis)
    return imp_utils.ret(ffi.squeeze(x, axis))

@set_module("mnm")
def stack(x, axis=0):
    x = imp_utils.to_tensor_tuple(x)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.stack(x, axis))

@set_module("mnm")
def stack_dx(x, axis=0):
    x = imp_utils.to_tensor_tuple(x)
    axis = imp_utils.to_int(axis)
    return imp_utils.ret(ffi.stack_dx(x, axis))

@set_module("mnm")
def stream_sync(x, stream_tag=0):
    x = imp_utils.to_tensor(x)
    stream_tag = imp_utils.to_int(stream_tag)
    return imp_utils.ret(ffi.stream_sync(x, stream_tag))

@set_module("mnm")
def strided_slice(x, begin, end, strides=None, slice_mode="end"):
    x = imp_utils.to_tensor(x)
    begin = imp_utils.to_int_tuple(begin)
    end = imp_utils.to_int_tuple(end)
    strides = imp_utils.to_int_tuple(strides)
    slice_mode = imp_utils.to_string(slice_mode)
    return imp_utils.ret(ffi.strided_slice(x, begin, end, strides, slice_mode))

@set_module("mnm")
def subtract(x1, x2, out=None, where=None):
    x1 = imp_utils.to_any(x1)
    x2 = imp_utils.to_any(x2)
    out = imp_utils.to_any(out)
    where = imp_utils.to_any(where)
    return imp_utils.ret(ffi.subtract(x1, x2, out, where))

@set_module("mnm")
def sum(x, axis=(), keepdims=0):
    x = imp_utils.to_tensor(x)
    axis = imp_utils.to_int_tuple(axis)
    keepdims = imp_utils.to_int_tuple(keepdims)
    return imp_utils.ret(ffi.sum(x, axis, keepdims))

@set_module("mnm")
def take(x, indices, axis=None, mode="clip"):
    x = imp_utils.to_tensor(x)
    indices = imp_utils.to_tensor(indices)
    axis = imp_utils.to_any(axis)
    mode = imp_utils.to_string(mode)
    return imp_utils.ret(ffi.take(x, indices, axis, mode))

@set_module("mnm")
def take_dx(x, y, dy, indices, axis=None, mode="clip"):
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    indices = imp_utils.to_tensor(indices)
    axis = imp_utils.to_any(axis)
    mode = imp_utils.to_string(mode)
    return imp_utils.ret(ffi.take_dx(x, y, dy, indices, axis, mode))

@set_module("mnm")
def tanh(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.tanh(x))

@set_module("mnm")
def tanh_dx(x, y, dy):
    x = imp_utils.to_any(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    return imp_utils.ret(ffi.tanh_dx(x, y, dy))

@set_module("mnm")
def transpose(x, axes=None):
    x = imp_utils.to_tensor(x)
    axes = imp_utils.to_int_tuple(axes)
    return imp_utils.ret(ffi.transpose(x, axes))

@set_module("mnm")
def transpose_dx(x, y, dy, axes=None):
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    dy = imp_utils.to_tensor(dy)
    axes = imp_utils.to_int_tuple(axes)
    return imp_utils.ret(ffi.transpose_dx(x, y, dy, axes))

@set_module("mnm")
def where(condition, x, y):
    condition = imp_utils.to_tensor(condition)
    x = imp_utils.to_tensor(x)
    y = imp_utils.to_tensor(y)
    return imp_utils.ret(ffi.where(condition, x, y))

@set_module("mnm")
def zeros(shape, dtype="int32", device="cpu"):
    shape = imp_utils.to_int_tuple(shape)
    dtype = imp_utils.to_string(dtype)
    device = imp_utils.to_string(device)
    return imp_utils.ret(ffi.zeros(shape, dtype, device))

@set_module("mnm")
def zeros_like(x):
    x = imp_utils.to_any(x)
    return imp_utils.ret(ffi.zeros_like(x))
