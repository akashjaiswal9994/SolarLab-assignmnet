import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/india"
response = requests.get(url)


html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
infobox_table = soup.find("table", {"class": "infobox ib-country vcard"})
data = {}
for tr in infobox_table.find_all("tr"):
   print(tr.text)
'''
import requests
from bs4 import BeautifulSoup
import json


def scrape_country_info(country_name):
    # Make a request to the Wikipedia page for the country
    response = requests.get(f'https://en.wikipedia.org/wiki/{country_name}')

    # Parse the HTML of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the information about the country
    table = soup.find('table', {'class': 'infobox ib-country vcard'})

    # Initialize an empty dictionary to store the data
    data = {}

    # Loop through all the rows in the table
    for row in table.find_all('tr'):
        # Get the name and value of the data point
        name = row.find('th').text
        value = row.find('td').text

        # Add the data point to the dictionary
        data[name] = value

    # Return the data as a JSON object
    return data

country_data = scrape_country_info('Spain')
json_data = json.dumps(country_data)  

print(json_data)'''