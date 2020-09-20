from tweet_poster import tweet
from channel_list import channels, Region
from pytchat import LiveChatAsync, VideoInfo
from concurrent.futures import CancelledError
import asyncio


class ChatMonitor:
    def __init__(self, video_id, video_info):
        self.video_id = video_id
        self.video_info = video_info

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
        for c in chatdata.items:
            # print(f"{c.datetime} [{c.author.name}]- {c.message}")
            if c.author.channelId in channels and \
                (channels[c.author.channelId]['region'] == Region.JPN or
                 channels[self.video_info.get_channel_id()]['region'] == Region.JPN):

                tweet(c, self.video_id, self.video_info)
            await chatdata.tick_async()
