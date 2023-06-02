import json
import yt_dlp

class MainPlayer():
    def __init__(self) -> None:
        # self.VID_ID = self.SearchMusic(QUERY)
        self.URL_RAW = 'https://www.youtube.com/watch?v='
        
    def YtDLP_Extract(self,QUERY):
        ydl_opts = {}
        self.URL = self.URL_RAW + self.SearchMusic(QUERY)
        
        yt_data_list = []
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.URL, download=False)
            yt_data = ydl.sanitize_info(info)
            self.yt_id = yt_data["id"]
            self.yt_title = yt_data["title"]
            self.yt_channel = yt_data["channel"]
            self.yt_duration = yt_data["duration"]
            self.yt_view_count = yt_data["view_count"]
            self.yt_webpage_url = yt_data["webpage_url"]
            self.yt_tags = yt_data["tags"]
            self.yt_comment_count = yt_data["comment_count"]
            self.yt_like_count = yt_data["like_count"]
            self.yt_upload_date = yt_data["upload_date"]
            self.yt_acodec = yt_data["acodec"]
            self.yt_categories = yt_data["categories"]

            max_tbr = 0
            for data in yt_data["formats"]:
                if data.get("fps") is None:
                    tbr = data.get("tbr", 0)
                    if tbr > max_tbr:
                        max_tbr = tbr
                        yt_audio_url = data["url"]
                        
            
            yt_data_list.append({
                    "id"           :   self.yt_id,
                    "title"        :   self.yt_title,
                    "channel"      :   self.yt_channel,
                    "duration"     :   self.yt_duration,
                    "view_count"   :   self.yt_view_count,
                    "webpage_url"  :   self.yt_webpage_url,
                    "tags"         :   self.yt_tags,
                    "comment_count":   self.yt_comment_count,
                    "like_count"   :   self.yt_like_count,
                    "upload_date"  :   self.yt_upload_date,
                    "acodec"       :   self.yt_acodec,
                    "categories"   :   self.yt_categories,
            })
            
            print(yt_data_list)
    
    def SearchMusic(self, QUERY):
        ydl = yt_dlp.YoutubeDL()
        search_results = ydl.extract_info(f"ytsearch:{QUERY}", download=False)
        videos = search_results.get('entries', [])
        
        
        return videos[0]["id"]
            
            
run = MainPlayer()
# run.SearchMusic("I Want a asian cheek weeknd")

run.YtDLP_Extract("Careless Whisper")