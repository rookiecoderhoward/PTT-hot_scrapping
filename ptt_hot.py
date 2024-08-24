import requests
from bs4 import BeautifulSoup

root_url = 'https://disp.cc/b/'

r = requests.get('https://disp.cc/b/PttHot')
soup = BeautifulSoup(r.text, 'html.parser')
# for span in soup.findall('span', class_ = 'listTitle')
for span in soup.select('#list span.listTitle'): # CSS selector
    href = span.find('a').get('href') # or span.find('a')['href']
    if href == 'PttHot/59l9':
        break
    url = root_url + href
    title = span.text
    print(f'{url}\n{title}')


