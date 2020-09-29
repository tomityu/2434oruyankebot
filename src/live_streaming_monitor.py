import os
from datetime import datetime
from channel_list import channels
from chat_monitor import ChatMonitor
from color import Color
from exclude_list import exclude_video_ids
from pytchat import VideoInfo
from logging import getLogger

logger = getLogger(__name__)


def search_live_streaming(youtube_service, q, event_type, monitoring_list):
    logger.info(
        f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} | {event_type} search start.")
    search_response = youtube_service.execute_search_list(q, event_type)
    temp_count = len(monitoring_list)
    for item in search_response['items']:
        if item['snippet']['channelId'] in channels:
            video_id = item['id']['videoId']
            try:
                video_info = VideoInfo(video_id=video_id)
                if is_valid_streaming(video_id, monitoring_list, video_info):
                    logger.info(
                        f"New {event_type}! | {video_id} | {item['snippet']['channelTitle']} | {item['snippet']['title']}")
                    monitoring_list[video_id] = {
                        'channel': item['snippet']['channelTitle'], 'title': item['snippet']['title']}
                    pid = os.fork()
                    if pid == 0:  # No pid. so this is child process!
                        ChatMonitor(video_id, video_info).start()
                        monitoring_value = monitoring_list.pop(video_id)
                        logger.info(
                            f"Livestreaming has terminated! => {datetime.now().strftime('%Y/%m/%d %H:%M:%S')} | {video_id} | {monitoring_value['channel']} | {monitoring_value['title']}")
                        print_monitoring_list(monitoring_list)
                        os._exit(status=0)
            except Exception as e:
                logger.error(e)
                logger.error(video_id)
                continue
    count = len(monitoring_list) - temp_count
    if count:
        logger.info(f'{count} new {event_type}s found!')
    else:
        logger.info(f'There was no new {event_type}.')


def print_monitoring_list(monitoring_list):
    logger.info('---monitoring_list---')
    for key, value in monitoring_list.items():
        logger.info(f"{key} | {value['channel']} | {value['title']}")
    logger.info(f'---{len(monitoring_list)} items---')


def is_valid_streaming(video_id, monitoring_list, video_info):
    return (not video_id in monitoring_list) and (not video_id in exclude_video_ids) and (not video_info.get_duration())
