from bs4 import BeautifulSoup
import requests
import csv

html = requests.get('http://coreyms.com').text

soup = BeautifulSoup(html, 'lxml')

csv_file = open('tutorial.csv', 'w+')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title','Description','Video link'])

content = soup.find('main', class_='content')

for article in content.find_all('article'):
    title = article.header.h2.a.text
    print(title)

    entry_content = article.find('div', class_="entry-content")
    description = entry_content.p.text
    print(description)

    try:
        video_id = article.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]
        video_link = f'https://youtube.com/watch/v={video_id}'
    except Exception:
        video_link = 'Not Available'

    print(video_link)
    print()

    csv_writer.writerow([title, description, video_link])

csv_file.close()