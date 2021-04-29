import os
from googleapiclient.discovery import build

API_KEY = os.environ['API_KEY']

youtube = build('youtube','v3',developerKey=API_KEY)

response = youtube.search().list(
        q="futebol",
        order="viewCount",
        part="id,snippet",
        maxResults=50,
        regionCode="BR"
   
         
        ).execute()
all_videos = response["items"]


title = [video['snippet']['title'] for video in all_videos]
desc = [video['snippet']['description'] for video in all_videos]
imageVideo = [video['snippet']['thumbnails']['high']['url'] for video in all_videos]
videoId = [video['id']['videoId'] for video in all_videos]



  


      
         
    
    
  

