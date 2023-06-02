import requests
import json
from bs4 import BeautifulSoup
import datetime

url = 'https://kworb.net/spotify/toplists.html'


  
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://kworb.net/'
}
    



res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
a_elements = soup.find_all('tr')

data = []
def topArtist():

    cnt = 0

      
    for name in a_elements:
      if cnt >= 11:
            break

      if name.a is not None:
        artist,track = ((name.a.text).split('-'))    
        stream = name.find('td',class_=lambda value: value != "text").text


        data.append({
            "artist": artist,
            "track": track,
            "streams": stream,
        })

    
        cnt +=1


      json_data = {
        "date": str(datetime.date.today()) ,
        "results": data[0:11]  
    }


    json_output = json.dumps(json_data,indent=4)

    with open("data/topartist.json", "w") as file:
        json.dump(json_data, file)



# topArtist()
# print(data)