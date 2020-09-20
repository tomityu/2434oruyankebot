from youtube import Youtube
from keys import YOUTUBE_API_KEYS
from logging import getLogger

logger = getLogger(__name__)

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


class YoutubeServices:
    def __init__(self):
        self.index = 0
        self.youtube_services = []
        for api_key in YOUTUBE_API_KEYS:
            self.youtube_services.append(
                Youtube(api_key, YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION))

    def execute_search_list(self, q, event_type):
        try:
            result = self.youtube_services[self.index].execute_search_list(
                q, event_type)
            logger.info(
                f'index: {self.index}, YOUTUBE_API_KEY: {self.youtube_services[self.index].api_key}')
        except Exception as e:
            logger.error(e)
            if self.index == len(YOUTUBE_API_KEYS) - 1:
                self.index = 0
            else:
                self.index += 1
            return self.execute_search_list(q, event_type)
        return result
