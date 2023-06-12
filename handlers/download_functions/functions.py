import requests
import json


def instagram(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {
        "url": link}

    headers = {
        "X-RapidAPI-Key": "42d6f07749mshb9b66ec144acdc4p132b88jsn786d4996054d",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()

    return response
