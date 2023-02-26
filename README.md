# PyTorch CPU

|           |                                                                               |
| --------- | ----------------------------------------------------------------------------- |
| Name      | pytorch-cpu                                                                   |
| Version   | v1.0.0                                                                        |
| DockerHub | [weevenetwork/pytorch-cpu](https://hub.docker.com/r/weevenetwork/pytorch-cpu) |
| Authors   | Jakub Grzelak                                                                 |

- [PyTorch CPU](#pytorch-cpu)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Use your pre-trained PyTorch model with weeve modules. This module supports only CPU models and we plan to make a separate module to run PyTorch with CUDA. The model should be available to the module via a downloadable URL or it should be stored in the edge device local filesystem. The module will take input data and then compose a tensor with data in the order assigned to the Ordered Labels environment variable. Later, the module will input that tensor into the model.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name               | Environment Variables | type   | Description                                                                                                                                                                                                                                                                                                                               |
| ------------------ | --------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model Download URL | MODEL_DOWNLOAD_URL    | string | If model is stored online, then provide a download URL to parse the model. Leave empty field to search for the model in the local filesystem (see Model Filepath configuration field).                                                                                                                                                    |
| Model Filepath     | MODEL_FILEPATH        | string | If model is stored in the local filesystem of the edge device or node (above field for the URL was left empty), then provide a path to the model file.                |
| Model Input dtype  | INPUT_DTYPE           | string | [dtype](https://pytorch.org/docs/stable/tensors.html#data-types) of the input tensor to the model: `float32/float`, `float64/double`, `float16/half`, `bfloat16`, `complex32/chalf`, `complex64/cfloat`, `complex128/cdouble`, `uint8`, `int8`, `int16/short`, `int32/int`, `int64/long`, `bool`, `quint8`, `qint8`, `qint32`, `quint4x2` |
| Ordered Labels     | ORDERED_LABELS        | string | Input data labels in the order of feeding into the model. Later a tensor will be created to feed that data into the model in the given order.                                                                                                                                                                                             |
| Output Label       | OUTPUT_LABEL          | string | The output label at which data is dispatched.                                                                                                                                                                                                                                                                                             |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| EGRESS_URLS           | string | HTTP ReST endpoints for the next module        |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
```

## Input

Input to this module is:

-   JSON body single object, example:

```json
{
    "temperature": 12,
    "volume": 1.3,
    "pressure": 0.32
}
```

-   array of JSON body objects, example:

```json
[
    {
        "temperature": 12,
        "volume": 1.3,
        "pressure": 0.32
    },
    {
        "temperature": 13,
        "volume": 2.1,
        "pressure": 0.34
    }
]
```

## Output

Output of this module is

-   JSON body single object, example:

```json
{
    "prediction": 14.323
}
```

-   array of JSON body objects, example:

```json
[
    {
        "prediction": 14.323
    },
    {
        "prediction": 13.45
    }
]
```
