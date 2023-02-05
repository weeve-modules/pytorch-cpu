import requests

from os import getenv
from pathlib import Path
from logging import getLogger
from api import setup_logging

setup_logging()
log = getLogger("download_model")

def download_model():
    if not getenv("MODEL_DOWNLOAD_URL", "") == "":
        try:
            # create directory to store the model
            Path("model").mkdir(parents=True, exist_ok=True)

            # download the model from the given url
            log.info(f"Downloading model from: {getenv('MODEL_DOWNLOAD_URL')} ...")
            resp = requests.get(getenv("MODEL_DOWNLOAD_URL"), allow_redirects=True)

            # save the model
            log.info(f"Saving the model inside Docker container in: model/{getenv('MODEL_FILENAME')} ...")
            open(f"model/{getenv('MODEL_FILENAME')}", 'wb').write(resp.content)

            log.info("Successfully downloaded the model.")

        except Exception as e:
            log.error(f"Exception when downloading the model: {e}")
