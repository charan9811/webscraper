import csv
import database
from datetime import date

db = database.database("./main/vergeData.db")
headers = ['Id', 'URL', 'Headline', 'Author', 'Date']
def to_csv():
    with open(f'./main/{date.today()}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in db.send_data().fetchall():
            writer.writerow(row)