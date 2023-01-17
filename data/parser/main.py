import requests
from bs4 import BeautifulSoup
import json

def get_data(url):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    # with open('index.html','r', encoding='utf-8') as file:
    #     src = file.read()
    src = requests.get(url, headers)
    

    soup = BeautifulSoup(src.text, 'lxml')
    movies = soup.find_all(class_="EventList__Event-sc-14wck6-3 dKUEol event rental large")
    dictionary = {}
    for movie in movies:
        print('--------------------------------')
        soupMovie = BeautifulSoup(src, 'lxml')
        name = movie.find_all('a', class_='event-name')
        for name_ in name:
            text_name = name_.text
            text_name = text_name.replace("  ", "")
            print(text_name)
            

    
        time_session = movie.find_all(class_='Show-sc-rhge3d-2 gDYwMv show')
        text_time_session = []
        for time_session_ in time_session:
            text_time_session.append(time_session_.text)
            print(text_time_session)

        dictionary[text_name] = text_time_session

    soup = BeautifulSoup(src, 'lxml')
    movies_pk = soup.find_all(class_="EventList__Event-sc-14wck6-3 dKUEol event rental pushkin-card large")
    for movie_pk in movies_pk:
        print('--------------------------------')
        name = movie_pk.find_all('a', class_='event-name')
        for name_ in name:
            text_name = name_.text
            text_name = text_name.replace("  ","")
            print(text_name)   
    
        time_session = movie_pk.find_all(class_='Show-sc-rhge3d-2 gDYwMv show')
        text_time_session = []
        for time_session_ in time_session:
            text_time_session.append(time_session_.text)

            print(time_session_.text)
        
        image = movie_pk.find('div',class_='Poster-sc-mn9zap-1 kAKPQC event-poster').find('img').get('src')
        for image_text in image:
            image_text = image.text
            print(image_text)
            


        dictionary[text_name] = text_time_session

        
        
    json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)
    with open("sample.json", "w", encoding='utf-8') as outfile:
        outfile.write(json_object)



get_data(f'https://kinosmena.ru/?date=2023/01/{17}')