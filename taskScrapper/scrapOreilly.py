import requests
from bs4 import BeautifulSoup
import json
from time import sleep

# Создаем список для хранения данных
data = []

base_url = "https://www.oreilly.com/radar/"

# Отправляем GET-запрос
response = requests.get(base_url)

# Проверка успешности запроса
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все элементы с классом 'defSection'
    news_items = soup.find_all('div', class_='defSection')

    # Проходим по каждому элементу и извлекаем данные
    for item in news_items:
        # Находим элемент с классом 'textCTA-small' внутри текущего 'defSection'
        link_element = item.find('a', class_='textCTA-small')
        if link_element:
            # Извлекаем текст из ссылки
            text = link_element.text
            # Добавляем данные в список
            data.append({'text': text})

    # Сохраняем данные в JSON файл
    with open('oreilly.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

    print("Data has been saved to 'oreilly.json'.")

else:
    print(f"Error {response.status_code}: Unable to fetch the page.")
