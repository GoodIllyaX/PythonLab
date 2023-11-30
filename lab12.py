from selenium import webdriver
from bs4 import BeautifulSoup
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string

driver = webdriver.Chrome()

news_sites = ["https://www.bbc.com", "https://www.cnn.com"]

for site in news_sites:
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            archive_url = f"{site}/archive/{year}/{month}"

            driver.get(archive_url)

            page_source = driver.page_source

            soup = BeautifulSoup(page_source, 'html.parser')

            news_text = soup.select('ваш_селектор_тексту')

            news_text = ' '.join([paragraph.get_text() for paragraph in news_text])

            translator = str.maketrans('', '', string.punctuation)
            news_text = news_text.translate(translator)

            words = nltk.word_tokenize(news_text.lower())

            stop_words = set(stopwords.words('english'))
            words = [word for word in words if word.isalpha() and word not in stop_words]

            word_frequency = Counter(words)

            print(f"Site: {site}, Year: {year}, Month: {month}")
            print("Top 10 words:", word_frequency.most_common(10))

driver.quit()
