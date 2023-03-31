#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup

# Load the URL
url = 'https://www.cbssports.com/nfl/stats/'
page = requests.get(url)

# Parse the page with BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Find the table with the data
table = soup.find('table', {'class': 'data'})

# Iterate through the table and print out the player stats
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    print(f"{cols[0].text:25s}{cols[2].text:15s}{cols[3].text:15s}{cols[7].text:5s}")
    


# In[ ]:


import requests
from bs4 import BeautifulSoup

# Load the URL
url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
page = requests.get(url)

# Parse the page with BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Find the table with the data
table = soup.find('table', {'class': 'W(100%) M(0)'})

# Iterate through the table and print out the stock data
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    print(f"{cols[0].text:10s}{cols[4].text:10s}")

