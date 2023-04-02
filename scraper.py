import requests
from bs4 import BeautifulSoup



class scraper:
    def __init__(self, url):
        self.url = url
        self.res = requests.get(self.url)
        self.items = []

    def get_data(self, html):
        soup = BeautifulSoup(html, "html.parser")
        articles = soup.find_all(class_=["relative", "z-10"])

        for item in articles:
            headline_element = item.select_one("h2 a")
            author_element = item.select_one(".inline-block a")
            date_element = item.select_one(".inline-block span")

            if headline_element != None or author_element != None or date_element != None:


                try:
                    headline = headline_element.text
                    link = f"https://www.theverge.com{headline_element.get('href')}"
                    splitted_link = link.split("/")
                    author = author_element.text

                    try:
                        date = f"{splitted_link[3]}/{splitted_link[4]}/{splitted_link[5]}"
                    except IndexError:
                        date = date_element.text
                        continue

                except AttributeError:
                    continue

                self.items.append({
                    "headline":headline,
                    "URL":link,
                    "author":author,
                    "date":date
                })




