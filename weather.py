import requests
from bs4 import BeautifulSoup

search = "weather in jakarta"
url = f"https://www.google.com/search?&q={search}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers)

s = BeautifulSoup(r.text, "html.parser")

update = s.find("span", id="wob_tm").text
print(update)