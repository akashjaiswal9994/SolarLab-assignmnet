import request
from bs4 import BeautifulSoup
import json


res=request.get("https://en.wikipedia.org/wiki/India")

soup = BeautifulSoup(res.content,'html.parser')
print(soup.prettify())


