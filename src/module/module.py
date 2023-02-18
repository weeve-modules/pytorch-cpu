"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

import os
import torch
from logging import getLogger
from .dtypes import DTYPES

log = getLogger("module")

ORDERED_LABELS = [label.strip() for label in os.getenv("ORDERED_LABELS", "").split(',')]
OUTPUT_LABEL = os.getenv("OUTPUT_LABEL", "")
INPUT_DTYPE = os.getenv("INPUT_DTYPE", "float32/float") # float32/float is a default PyTorch dtype

log.info(f"Loading the model in CPU mode ...")
DEVICE = torch.device("cpu")
if os.getenv("MODEL_DOWNLOAD_URL"):
    log.debug("Loading the model downloaded into the docker container: model/downloaded_model.pt ...")
    MODEL = torch.load(f"model/downloaded_model.pt", map_location=DEVICE)
else:
    log.debug(f"Loading the model mounted by volume to the docker container: {os.getenv('MODEL_FILEPATH')} ...")
    MODEL = torch.load(f"{os.getenv('MODEL_FILEPATH')}", map_location=DEVICE)
log.info("Model loaded successfully.")

def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        if type(received_data) == list:
            X = torch.tensor([[data[label] for label in ORDERED_LABELS] for data in received_data], dtype=DTYPES[INPUT_DTYPE], device=DEVICE)
            y_hat = MODEL(X).data.tolist()
            processed_data = [{OUTPUT_LABEL: y[0]} for y in y_hat]
        else:
            X = torch.tensor([received_data[label] for label in ORDERED_LABELS], dtype=DTYPES[INPUT_DTYPE], device=DEVICE).reshape(1,-1)
            processed_data = {OUTPUT_LABEL: MODEL(X).item()}

        return processed_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
