import requests
from bs4 import BeautifulSoup
import json

def get_data(url):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
    }

    # with open('index.html','r', encoding='utf-8') as file:
    #     src = file.read()
    src = requests.get(url, headers).content
    print(src)

    soup = BeautifulSoup(src, 'lxml')
    movies = soup.find_all(class_="EventList__Event-sc-14wck6-3 dKUEol event rental large")
    movies_pk = soup.find_all(class_="EventList__Event-sc-14wck6-3 dKUEol event rental pushkin-card large")

    dictionary = {}
    for movie in (movies + movies_pk):
        soupMovie = BeautifulSoup(src, 'lxml')

        text_time_session = {}
        image_string = ''

        #gets movie's name
        name = movie.find_all('a', class_='event-name')
        for name_ in name:
            text_name = name_.text
            text_name = text_name.replace("  ", "")
            text_name = text_name.replace('\n', " ")

        #gets movie's img
        image = movie.find('div',class_='Poster-sc-mn9zap-1 kAKPQC event-poster').find('img').get('src')
        for image_text in image:
            image_string += image_text
            image_string = image_string.replace('22x32/filters:quality(80):blur(2)/','')

        text_time_session.update({"img":image_string})
            
        #gets movie's data
        time_session = movie.find_all("div", class_='EventSchedule__Schedule-sc-1crhtam-0 fgDpKR schedule')
        for time_session_ in time_session:
            container = time_session_.find_all('div', class_='facility')

            # gets all sinema
            for obj in container:
                sinema_name = obj.find("span", class_="facility-address")
                branch_data = obj.find_all('div', class_='Show-sc-rhge3d-2 gDYwMv show')

                text_time_session.update({sinema_name.text:{}})

            # gets time and cost
            for data_session in branch_data:
                time = data_session.find('div', class_ = "show-time")
                cost = data_session.find('div', class_ = "Show__Price-sc-rhge3d-0 kmWvJz price")
                
                time_text = time.text.strip()
                cost_text = cost.text.strip()

                text_time_session[sinema_name.text].update({time_text: cost_text})

        # cupdate json file with data
        dictionary.update({text_name : text_time_session})
        #print(dictionary)

    # inject the data into the json file
    json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)
    with open("data.json", "w", encoding='utf-8') as outfile:
        outfile.write(json_object)

#get_data(f'https://kinosmena.ru/?date=2023/01/{18}&facility=smena')