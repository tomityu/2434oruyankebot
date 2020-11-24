import os
import pprint
import time
import urllib.error
import urllib.request
from datetime import datetime
from logging import getLogger

logger = getLogger(__name__)


def download(url, save_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(save_path, mode='wb') as imagefile:
                imagefile.write(data)
    except Exception as e:
        logger.error(e)


def read(save_path):
    try:
        with open(save_path, mode="rb") as imagefile:
            return imagefile.read()
    except Exception as e:
        logger.error(e)
