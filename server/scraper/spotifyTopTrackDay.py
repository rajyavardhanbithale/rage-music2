import requests
import json
from bs4 import BeautifulSoup
import datetime

url = 'https://kworb.net/spotify/country/in_daily.html'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://kworb.net/'
}


res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
tr_elements = soup.find_all('tr')


def toptracks():
    data = []
    counter = 0

    for tr in tr_elements:
        if counter >= 11:
            break

        song_element = tr.find(
            'a', href=lambda href: href and '/track/' in href)
        if song_element:
            song = song_element.get_text(strip=True)
        else:
            song = ""

        singer_element = tr.find(
            'a', href=lambda href: href and '/artist/' in href)
        if singer_element:
            singer = singer_element.get_text(strip=True)
        else:
            singer = ""

        # collaborators_element = tr.find('a', string=lambda text: text and text.startswith('(w/'))
        # if collaborators_element:
        #     collaborators = collaborators_element.get_text(strip=True)[3:].strip()
        # else:
        #     collaborators = ""

        data.append({
            "track": song,
            "artist": singer,
        })

        counter += 1

    json_data = {
        "date": str(datetime.date.today()),
        "results": data[1:11]
    }

    json_output = json.dumps(json_data, indent=4)

    with open("data/toptracks.json", "w") as file:
        json.dump(json_data, file)


toptracks()
