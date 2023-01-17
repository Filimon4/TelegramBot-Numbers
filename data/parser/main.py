import requests
from bs4 import BeautifulSoup
import re
def get_data(url):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    with open('index.html','r', encoding='utf-8') as file:
        src = file.read()
    # src = requests.get(url, headers)
    # soup = BeautifulSoup(src.text, 'lxml')


    soup = BeautifulSoup(src, 'lxml')
    name = soup.find_all('a', class_='event-name')
    for name_ in name:
        text_name = name_.text
        text_name = text_name.replace("  ", "")
        

    
    date_tab = soup.find_all(class_="day-tab")
    for date_tab_ in date_tab:
        text_date_tab = date_tab_.text
        match = re.match(r"([a-z]+)([0-9]+)", text_date_tab, re.I)
        if match:
            text_date_tab = match.groups()
        
            print(text_date_tab)


get_data('https://kinosmena.ru/')