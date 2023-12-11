from bs4 import BeautifulSoup
import requests

url = "https://tsn.ua/ru"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

news_articles = soup.find_all('article')

with open('news_data.txt', 'w', encoding='utf-8') as file:
    for article in news_articles:
        # Заголовок
        title_element = article.find('h3', class_='c-card__title')
        title = title_element.text.strip() if title_element else 'N/A'

        # Посилання
        link_element = article.find('a', class_='c-card__link')
        link = link_element['href'] if link_element else 'N/A'

        # Дата публікації
        date_element = article.find('time')
        date = date_element['datetime'] if date_element else 'N/A'

        # Перегляди
        views_element = article.find('dd', class_='c-bar__label i-before i-before--spacer-r-sm i-views')
        views = views_element.text.strip() if views_element else 'N/A'
        
        file.write(f"Title: {title}\nLink: {link}\nDate: {date}\nViews: {views}\n\n")
