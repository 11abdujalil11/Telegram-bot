import requests

url = "https://picsart-remove-background2.p.rapidapi.com/removebg"

payload = {"format": "PNG"}
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "5fe7636e94msh3134839d77bc18ep1a5075jsn67a9b9c4bb81",
    "X-RapidAPI-Host": "picsart-remove-background2.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response)
