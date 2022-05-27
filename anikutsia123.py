import csv
import time

import requests
from bs4 import BeautifulSoup

row = []

for i in range(1, 6):
    content = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    ba = BeautifulSoup(content.text, 'html.parser')
    title_blocks = ba.find_all('div', class_='quote')
    for title_block in title_blocks:
        page = f"Page: {i}"
        title = title_block.find('span', class_='text').text
        author = title_block.find('small', class_='author').text
        tags = ' '.join([i.text for i in title_block.find_all('a', class_='tag')])
        row.append([page, title, author, tags])
    time.sleep(15)

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(row)