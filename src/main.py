#!/usr/bin/env python
import sys
import time
import signal
from multiprocessing import Manager
from youtube_services import YoutubeServices
from live_streaming_monitor import search_live_streaming, print_monitoring_dict
from logging import getLogger, basicConfig, Formatter, INFO
from logging.handlers import TimedRotatingFileHandler


if __name__ == '__main__':
    basicConfig(
        level=INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/2434oruyankebot.log'
    )
    logger = getLogger(__name__)
    try:
        youtube_service = YoutubeServices()
        monitoring_dict = Manager().dict()
        terminated_list = Manager().list()
        q = 'にじさんじ OR Nijisanji OR 月ノ美兎 OR 笹木咲 OR 葛葉 OR 雨森小夜 OR リゼ OR kanae OR 社築 OR 加賀美 OR 黛 OR 舞元 OR 剣持刀也 OR 三枝 OR イブラヒム OR 不破 OR Gilzaren OR JuvveL OR 天開司 OR ふぇありす OR 瀬戸'
        flip = True

        def handler(signum, frame):
            global flip
            search_live_streaming(
                youtube_service, q, 'live', monitoring_dict, terminated_list)
            if flip:
                search_live_streaming(
                    youtube_service, q, 'upcoming', monitoring_dict, terminated_list)
            flip = not flip
            print_monitoring_dict(monitoring_dict)
            logger.info(f"terminated_list count: {len(terminated_list)}")
        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, 0.1, 300)
        while True:
            time.sleep(1)
    except Exception as e:
        logger.error(e)
