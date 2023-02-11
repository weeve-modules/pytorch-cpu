import torch

DTYPES = {
    "float32/float": torch.float32,
    "float64/double": torch.float64,
    "float16/half": torch.float16,
    "bfloat16": torch.bfloat16,
    "complex32/chalf": torch.complex32,
    "complex64/cfloat": torch.complex64,
    "complex128/cdouble": torch.complex128,
    "uint8": torch.uint8,
    "int8": torch.int8,
    "int16/short": torch.int16,
    "int32/int": torch.int32,
    "int64/long": torch.int64,
    "bool": torch.bool,
    "quint8": torch.quint8,
    "qint8": torch.qint8,
    "qint32": torch.qint32,
    "quint4x2": torch.quint4x2
}
