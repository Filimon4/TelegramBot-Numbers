import requests
from bs4 import BeautifulSoup
import re
import json

def get_data(url):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    with open('index.html','r', encoding='utf-8') as file:
        src = file.read()
    # src = requests.get(url, headers)
    # soup = BeautifulSoup(src.text, 'lxml')

    soup = BeautifulSoup(src, 'lxml')
    movies = soup.find_all(class_="EventList__Event-sc-14wck6-3 dKUEol event rental large")
    for movie in movies:
        with open("movie.html", 'r', encoding='utf-8') as f:
             moiveHtml = f.read()
        print('--------------------------------')
        soupMovie = BeautifulSoup(moiveHtml, 'lxml')
        name = soupMovie.find_all('a', class_='event-name')
        for name_ in name:
            text_name = name_.text
            text_name = text_name.replace("  ", "")
            print(text_name)   

    
        date_tab = soupMovie.find_all(class_="day-tab")
        for date_tab_ in date_tab:
            text_date_tab = date_tab_.text
    
            print(text_date_tab)
    
        time_session = soupMovie.find_all(class_='show-time')
        for time_session_ in time_session:
            text_time_session = time_session_.text

            print(text_time_session)













    # soup = BeautifulSoup(src, 'lxml')
    # name = soup.find_all('a', class_='event-name')
    # for name_ in name:
    #     text_name = name_.text
    #     text_name = text_name.replace("  ", "")
    #     print(text_name)   

    
    # date_tab = soup.find_all(class_="day-tab")
    # for date_tab_ in date_tab:
    #     text_date_tab = date_tab_.text
    
    #     print(text_date_tab)
    
    # time_session = soup.find_all(class_='show-time')
    # for time_session_ in time_session:
    #     text_time_session = time_session_.text

    #     print(text_time_session)

get_data('https://kinosmena.ru/')