from datetime import datetime
from pytchat import VideoInfo
from twitter import Twitter, OAuth
from twitter_text import parse_tweet
from channel_list import channels
from color import Color
from keys import TW_ACCESS_TOKEN, TW_ACCESS_TOKEN_SECRET, TW_API_KEY, TW_API_SECRET
from logging import getLogger

logger = getLogger(__name__)

ENCODE = 'utf-8'
SHORTEST_LENGTH = 20
LIMIT_LENGTH = 280


def tweet(chat, video_id, video_info):
    try:
        video_info = VideoInfo(video_id=video_id)
    except Exception as e:
        logger.error(e)
    video_title = video_info.get_title()
    author_name = channels[chat.author.channelId]['name']
    tag = channels[video_info.get_channel_id()]['tag']

    if chat.type == 'textMessage':
        content = generate_text_content(
            chat, author_name, chat.message, video_id, video_title, tag)
    elif chat.type == 'superChat':
        content = generate_superchat_content(
            chat, author_name, chat.message, video_id, video_title, tag)
    elif chat.type == 'superSticker':
        content = generate_supersticker_content(
            chat, author_name, chat.message, video_id, video_title, tag)
    else:   # newSponsor
        content = generate_newsponsor_content(
            chat, author_name, chat.message, video_id, video_title, tag)

    logger.info(f'---')
    logger.info(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    logger.info(content)
    logger.info(f'---')

    if '#ひみつ' in content:
        logger.info('秘密にしてほしいみたい')
    else:
        t = Twitter(auth=OAuth(
            TW_ACCESS_TOKEN, TW_ACCESS_TOKEN_SECRET, TW_API_KEY, TW_API_SECRET))
        try:
            statusUpdate = t.statuses.update(status=content)
        except Exception as e:
            logger.error(e)


def generate_text_content(chat, author_name, message, video_id, video_title, tag):
    content = f'{author_name}「{message}」\n'
    content += '\n'
    content += f'{video_title}\n'
    content += f'https://www.youtube.com/watch?v={video_id}\n'
    content += tag
    return check_content(content, generate_text_content, chat, author_name, message, video_id, video_title, tag)


def generate_superchat_content(chat, author_name, message, video_id, video_title, tag):
    content = ''
    if message:
        content += f'💰{chat.amountString} superchat!!💰\n'
        content += '\n'
        content += f'{author_name}「{message}」\n'
    else:
        content += f'💰{author_name} posted superchat!! {chat.amountString}💰\n'
    content += '\n'
    content += f'{video_title}\n'
    content += f'https://www.youtube.com/watch?v={video_id}\n'
    content += tag
    return check_content(content, generate_superchat_content, chat, author_name, message, video_id, video_title, tag)


def generate_supersticker_content(chat, author_name, message, video_id, video_title, tag):
    content = f'💕{author_name} posted supersticker!! {chat.amountString}💕\n'
    content += '\n'
    content += f'[{chat.renderer["sticker"]["accessibility"]["accessibilityData"]["label"]}]\n'
    content += '\n'
    content += f'{video_title}\n'
    content += f'https://www.youtube.com/watch?v={video_id}\n'
    content += tag
    return check_content(content, generate_supersticker_content, chat, author_name, message, video_id, video_title, tag)


def generate_newsponsor_content(chat, author_name, message, video_id, video_title, tag):
    content = f'⭐{author_name} became new sponsor!!⭐\n'
    content += '\n'
    content += f'{video_title}\n'
    content += f'https://www.youtube.com/watch?v={video_id}\n'
    content += tag
    return check_content(content, generate_newsponsor_content, chat, author_name, message, video_id, video_title, tag)


def check_content(content, generate_content, chat, author_name, message, video_id, video_title, tag):
    parsed_tweet = parse_tweet(content)
    if parsed_tweet.valid:
        return content
    else:
        truncated_message, truncated_video_title = truncate_content(
            message, video_title, parsed_tweet.weightedLength - LIMIT_LENGTH)
        return generate_content(chat, author_name, truncated_message, video_id, truncated_video_title, tag)


def truncate_content(message, video_title, exceeded_length):
    video_title_length = parse_tweet(video_title).weightedLength
    if exceeded_length < video_title_length - SHORTEST_LENGTH:
        return message, truncate(video_title, video_title_length - exceeded_length)
    else:
        message_length = parse_tweet(message).weightedLength
        return truncate(message, message_length - (exceeded_length - (video_title_length - SHORTEST_LENGTH))), truncate(video_title, SHORTEST_LENGTH)


def truncate(str, num_bytes):
    while parse_tweet(str).weightedLength > num_bytes - 2:
        str = str[:-1]
    return str + '…'
