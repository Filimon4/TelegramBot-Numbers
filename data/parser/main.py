import requests
from bs4 import BeautifulSoup

def get_data(url):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    req = requests.get(url, headers)
    print(req.text)
    # with open('index.html', 'w') as file:
    #     file.write(req.text)


    # with open('index.html') as file:
    #     src = file.read()

    # soup = BeautifulSoup(src, 'lxml')
    # articles = soup.find_all()
get_data('https://kolizeum.ru/')