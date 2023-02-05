"""
Exporting methods
"""
from .log import setup_logging

from module.download_model import download_model
download_model()

from .request_handler import request_handler
