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


url = 'https://lh3.googleusercontent.com/5wOB_7MitsAPQG1vpCYSSLOLHdiRIwwsf97yfzW63YZihVf0B6MulS65DRFeftFul6rd6BNCxZ5h0wrIvkA=s40-rp'
save_path = f'./images/{datetime.now()}.png'
download(url, save_path)
