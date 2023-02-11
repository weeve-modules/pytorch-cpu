import requests

from os import getenv
from pathlib import Path
from logging import getLogger
from api import setup_logging

setup_logging()
log = getLogger("download_model")

def download_model():
    model_url = getenv("MODEL_DOWNLOAD_URL")
    if model_url:
        try:
            # create directory to store the model
            Path("model").mkdir(parents=True, exist_ok=True)

            # download the model from the given url
            log.info(f"Downloading model from: {model_url} ...")
            resp = requests.get(model_url, allow_redirects=True)

            # save the model
            if resp.status_code == 200:
                log.info(f"Saving the model inside Docker container in: model/{getenv('MODEL_FILENAME')} ...")
                open(f"model/{getenv('MODEL_FILENAME')}", 'wb').write(resp.content)

                log.info("Successfully downloaded the model.")
            else:
                log.error(f"Could not download the model. {resp.status_code} - {resp.reason}")

        except Exception as e:
            log.error(f"Exception when downloading the model: {e}")
