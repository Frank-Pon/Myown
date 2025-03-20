import requests
from bs4 import BeautifulSoup
 
url = 'https://www.ptt.cc/bbs/Stock/index.html'
header = {'User-Agent':'Mozilla/5.0'}
cookie = {'over18':'1'}
response = requests.get(url,headers = header,cookies=cookie)
soup = BeautifulSoup(response.text,'html.parser')
titles = soup.find_all('div',class_='title')
 
for title in titles:
    print(title.text.strip())