import requests
from bs4 import BeautifulSoup
import json


res=requests.get("https://en.wikipedia.org/wiki/India")

soup = BeautifulSoup(res.content,'html.parser')
#python assignment/scrap.pyprint(soup.prettify())


def get_infobox(url):
       response = requests.get(url)
       bs = BeautifulSoup(response.content,'html.parser')

       table = bs.find('table', {'class' :'infobox ib-country vcard'})
       result = {}
       row_count = 0
       if table is None:
         pass
       else:
         for tr in table.find_all('tr'):
             if tr.find('th'):
                 pass
             else:
                 row_count += 1
         if row_count > 1:
             if tr is not None:
               result[tr.find('td').text.strip()] = tr.find('td').text
         return result

print(get_infobox("https://en.wikipedia.org/wiki/India"))        