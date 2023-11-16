import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"

headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "5fe7636e94msh3134839d77bc18ep1a5075jsn67a9b9c4bb81",
    "X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}


# test payload
# payload = "image_url=https%3A%2F%2Fobjectcut.com%2Fassets%2Fimg%2Fraven.jpg"

async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    # logging.info(response.json()['response']['image_url'])
    return response.json()['response']['image_url']
