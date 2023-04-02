import scraper
import database
import tocsv

count = 0
scrape = scraper.scraper("https://www.theverge.com")
scrape.get_data(scrape.res.text)
db = database.database("./main/vergeData.db")
for item in scrape.items:
    if db.find_data(item['headline']):
        db.fill_data(count,item)
        count += 1

db.close_connection()

tocsv.to_csv()

print("done")