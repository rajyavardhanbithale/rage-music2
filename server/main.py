
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import Optional

from datetime  import datetime
import datetime as dt
import pytz
import create
import time
import os
import orjson

from scraper import spotifyTopTrackDay
from scraper import spotifyTopArtist



from spotifyData import getDetailsFront
from spotifyData import getDetailsArtist

from fastapi.responses import FileResponse

app = FastAPI()

origins = [
    "http://127.0.0.1:3000"  # Replace with your Next.js application's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Add OPTIONS method
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    username: str
    email: str
    password: str
    time: str = None
    ip: str = None

#create
@app.post("/signin/")
async def create_item(item: Item, request:Request):

    item.time = datetime.now(pytz.utc).isoformat()
    item.ip = request.client.host
    
    
    create.addData(item.dict())
    return {"opreation":"created"}


@app.get("/service/tracks")
async def servetracks():
    if os.path.exists("data/toptracks.json"):
    
        pass
    else:
        
        spotifyTopTrackDay.toptracks() 
               
    with open('data/toptracks.json', 'r') as tt:
        data_raw =tt.read()

        tt_data = orjson.loads(data_raw)
        
        if str(dt.date.today()) != tt_data["date"]:
            spotifyTopTrackDay.toptracks()
    
    return tt_data

@app.get("/service/artist")
async def serveArtist():
    if os.path.exists("data/topartist.json"):
    
        pass
    else:
        
        spotifyTopArtist.topArtist() 
               
    with open('data/topartist.json', 'r') as tt:
        data_raw =tt.read()

        tt_data = orjson.loads(data_raw)
        
        if str(dt.date.today()) != tt_data["date"]:
            spotifyTopArtist.topArtist()
    
    return tt_data

#============================ MAIN =================
@app.get("/top/tracks")
async def toptracks():
    
    if os.path.exists("data/processedTopTracks.json"):
        pass
    
    else:
        spotifyTopTrackDay.toptracks() 
        with open('data/toptracks.json', 'rb') as tt:
            data_raw =tt.read()
            
            data = orjson.loads(data_raw)
            print("get")
            print(data["date"])
            
            try:
                if str(dt.date.today()) == data["date"]:

                    for items in data["results"]:
                        #print(item["track"])
                        spotifyTopTrackDay.toptracks()
                        getDetailsFront.getdata(items["track"],items["artist"])
            except:
                spotifyTopTrackDay.toptracks()
                getDetailsFront.getdata(items["track"],items["artist"])
                
                
                
                
    with open('data/processedTopTracks.json', 'r') as tt:
        data_raw =tt.read()
        tt_data = orjson.loads(data_raw)
        

    return tt_data



@app.get("/top/artist")
async def topArtist():
    
    if os.path.exists("data/processedTopArtist.json"):
        pass

        
    
    else:
        spotifyTopArtist.topArtist() 
        with open('data/topartist.json', 'rb') as tt:
            data_raw =tt.read()
            
            data = orjson.loads(data_raw)
            print("get")
            print(data["date"])
            
            try:
                if str(dt.date.today()) == data["date"]:

                    for items in data["results"]:
                        #print(item["track"])
                        spotifyTopArtist.topArtist()
                        getDetailsArtist.getdata(items["track"],items["artist"],items["streams"])
            except:
                spotifyTopArtist.topArtist()
                getDetailsArtist.getdata(items["track"],items["artist"],items["streams"])
                
                
                
                
    with open('data/processedTopArtist.json', 'r') as tt:
        data_raw =tt.read()
        tt_data = orjson.loads(data_raw)
        

    return tt_data


#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/audio/{filename}")
async def get_audio_file(filename: str):
    file_path = f"{filename}.mp3"  # Replace with the actual path to your audio files
    return FileResponse(file_path, media_type="audio/mp3")



@app.get("/track/")
async def get_track():
    pass