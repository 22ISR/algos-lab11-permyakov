import requests

response = requests.get("http://www.omdbapi.com/?apikey=[505480d7]&")
if response.status_code == 200:
    print("Success:", response.json())

