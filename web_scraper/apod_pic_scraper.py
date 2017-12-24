from bs4 import BeautifulSoup
import requests
import os

html = requests.get('https://apod.nasa.gov/apod/archivepix.html').text

soup = BeautifulSoup(html,'lxml').find('b')

i=1
for each in soup.find_all('a'):
    daily_link = each['href']
    daily = requests.get(f'https://apod.nasa.gov/apod/{daily_link}').text
    daily_soup = BeautifulSoup(daily, 'lxml')

    try:
        center = daily_soup.find('center')
        img_src = center.img['src']
        img_name = img_src.split('/')[-1]

        r = requests.get(f'https://apod.nasa.gov/apod/{img_src}', stream=True)

        with open(os.path.join('images', img_name), 'wb') as fd:
            print(f'Downloading {img_name}...')
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
    except Exception:
        print(f'skipping image for {daily_link}')

    i+=1
    if i== 11:
        break

print('Done')