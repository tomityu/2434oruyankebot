import os
from datetime import datetime
from channel_list import channels
from chat_monitor import ChatMonitor
from color import Color
from exclude_list import exclude_list
from logging import getLogger
import subprocess

logger = getLogger(__name__)


def search_live_streaming(youtube_service, q, event_type, monitoring_dict, terminated_list):
    logger.info(
        f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} | {event_type} search start.")
    search_response = youtube_service.execute_search_list(q, event_type)
    temp_count = len(monitoring_dict)
    for item in search_response['items']:
        if item['snippet']['channelId'] in channels:
            video_id = item['id']['videoId']
            try:
                if is_valid_streaming(video_id, monitoring_dict, terminated_list):
                    if event_type == 'upcoming':
                        videos_response = youtube_service.execute_videos_list(
                            video_id)
                        if 'actualEndTime' in videos_response['items'][0]['liveStreamingDetails']:
                            terminated_list.append(video_id)
                            continue
                    logger.info(
                        f"New {event_type}! | {video_id} | {item['snippet']['channelTitle']} | {item['snippet']['title']}")
                    monitoring_dict[video_id] = {
                        'channel': item['snippet']['channelTitle'], 'title': item['snippet']['title']}
                    subprocess.check_call(
                        ['python3', 'src/chat_monitor.py', video_id, item['snippet']['title'], item['snippet']['channelId']])
            except Exception as e:
                logger.error(e)
                logger.error(video_id)
                continue
    count = len(monitoring_dict) - temp_count
    if count:
        logger.info(f'{count} new {event_type}s found!')
    else:
        logger.info(f'There was no new {event_type}.')


def print_monitoring_dict(monitoring_dict):
    logger.info('---monitoring_dict---')
    for key, value in monitoring_dict.items():
        logger.info(f"{key} | {value['channel']} | {value['title']}")
    logger.info(f'---{len(monitoring_dict)} items---')


def is_valid_streaming(video_id, monitoring_dict, terminated_list):
    return (not video_id in monitoring_dict) and (not video_id in terminated_list) and (not video_id in exclude_list)
