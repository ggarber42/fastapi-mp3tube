import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from typing import Optional
import youtube_dl

app = FastAPI()

@app.get('/')
def index():
    return "hello misha"

@app.get("/music")
async def read_item(q: Optional[str] = None):
    if q:
        url_path = q 
        video_info = youtube_dl.YoutubeDL().extract_info(url = url_path,download=False)
        music_name = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':music_name,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
           ydl.download([video_info['webpage_url']])
        file_path = os.path.join(os.curdir, music_name)
        return FileResponse(path=file_path, filename=music_name, media_type='text/mp4')
    return {"message": "Aqui"}
