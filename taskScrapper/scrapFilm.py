import requests
from bs4 import BeautifulSoup
import json

url = "https://ru.wikipedia.org/wiki/100_%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85_%D1%86%D0%B8%D1%82%D0%B0%D1%82_%D0%B8%D0%B7_%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%B7%D0%B0_100_%D0%BB%D0%B5%D1%82_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_AFI"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []

    # Находим таблицу с цитатами
    table = soup.find('table', class_='wikitable')

    for row in table.find_all('tr')[1:]:
        # Получаем ячейку с годом выпуска фильма
        cells = row.find_all('td')

        if len(cells) >= 7:
            year_cell = cells[6]

            # Извлекаем год из ячейки
            year_text = year_cell.get_text(strip=True)
            year = int(year_cell.text.strip())

            # Если год после 1995, добавляем цитату в список
            if year > 1995:
                quote_cell = cells[1]
                quote = quote_cell.text.strip()
                data.append({"year": year, "quote": quote})

    # Сохраняем данные в JSON-файл
    with open("quotes.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

    print("Data has been saved to 'quotes.json'.")

else:
    print(f"Error {response.status_code}: Unable to fetch the page.")
