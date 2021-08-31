from tweet_poster import tweet
from channel_list import channels, Region
from pytchat import LiveChatAsync
from concurrent.futures import CancelledError
import asyncio


class ChatMonitor:
    def __init__(self, video_id, video_title, host_channel_id):
        self.video_id = video_id
        self.video_title = video_title
        self.host_channel_id = host_channel_id

    def start(self):
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.monitor())
        except CancelledError:
            pass

    async def monitor(self):
        livechat = LiveChatAsync(self.video_id, callback=self.fetchcallback)
        while livechat.is_alive():
            await asyncio.sleep(3)

    async def fetchcallback(self, chatdata):
        for chat in chatdata.items:
            # print(
            #     f"{chat.datetime} [{chat.author.name}]- {chat.message} - {self.video_title}")
            # for key, value in chat.__dict__.items():
            #     print(key, ':', value)
            if self.is_valid_chat(chat):
                tweet(chat, self.video_id, self.video_title, self.host_channel_id)
            await chatdata.tick_async()

    def is_valid_chat(self, chat):
        return chat.author.channelId in channels and \
            (channels[chat.author.channelId]['region'] == Region.JPN or
             channels[self.host_channel_id]['region'] == Region.JPN)
