import requests
import json


def all_downloader(link):
    import requests

    url = "https://all-media-downloader.p.rapidapi.com/download"

    payload = {"url": link}

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "42d6f07749mshb9b66ec144acdc4p132b88jsn786d4996054d",
        "X-RapidAPI-Host": "all-media-downloader.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers).json()

    return response


# print(all_downloader("https://pin.it/656aKfH"))
