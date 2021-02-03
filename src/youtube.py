from apiclient.discovery import build


class Youtube:
    def __init__(self, api_key, youtube_api_service_name, youtube_api_version):
        self.api_key = api_key
        self.youtube = build(youtube_api_service_name,
                             youtube_api_version, developerKey=api_key)

    def execute_search_list(self, q, event_type):
        return self.youtube.search().list(
            part='id,snippet',
            q=q,
            safeSearch='none',
            type='video',
            maxResults=50,
            eventType=event_type
        ).execute()

    def execute_videos_list(self, video_id):
        return self.youtube.videos().list(
            part='liveStreamingDetails',
            id=video_id
        ).execute()
