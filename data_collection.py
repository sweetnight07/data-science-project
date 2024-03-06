import sqlite3

import requests
from bs4 import BeautifulSoup

# TODO: piping plover analyze rising sea levels and high temperature 

BIRDS_EBIRD_LINK = 'https://api.ebird.org/v2/data/obs/KZ/recent'

BIRDS_API_KEY = '22hppic79e3v'

# # make a request to the url
# req = requests.get(BIRDS_EBIRD_LINK)

import requests

import requests

payload={}
headers = {
  'X-eBirdApiToken': '{{22hppic79e3v}}'

}

req = requests.request("GET", BIRDS_EBIRD_LINK, headers=headers, data=payload)
if req.status_code == 200:
    print('request successful')
    birds_data = BeautifulSoup(req.content, 'html.parser')
else:
    print('request not successful')

print(req.text)


# # Create connection to database
# conn = sqlite3.connect('data.db')
# c = conn.cursor()

# # Delete tables if they exist
# c.execute('DROP TABLE IF EXISTS "birds";')
# # c.execute('DROP TABLE IF EXISTS "quotes";')

# # Create tables in the database to store the collected data.
# # change to have primary keys
# c.execute('''CREATE TABLE IF NOT EXISTS birds (
#                 symbol TEXT PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 location TEXT NOT NULL
#              )''')

# # Add data to the tables in the database. REMEMBER TO COMMIT
# for row in birds_data.find_all('tr')[1:]:  # skip the header row
#     cells = row.find_all('td')

#     # find the name within the link
#     a_tag = cells[1].find('a')
#     if a_tag:
#         name = a_tag.text
#     else:
#         name = None

#     # find the values for each of the cells in the table and add to the database
#     symbol = cells[2].text.strip()
#     price = float(cells[3].text.replace(",", ""))
   
#     # cleans the percent change
#     change_percentage = cells[5].text 
#     change_percentage = change_percentage.replace("+", "")
#     change_percentage = float(change_percentage.replace("%", ""))

#     # cleans the volume
#     volume = cells[6].text 
#     if "K" in volume:
#         volume = int(float(volume.replace("K", "")) * 1000)
#     elif "M" in volume:
#         volume = int(float(volume.replace("M", "")) * 1000000)

#     state = cells[7].text.lower().strip()

#     # Make a request to the API endpoint for the symbol
#     jan_response = requests.get(STONKS_API_URL + "/" + symbol + "/chart/date/2023-01-20")
#     month_response = requests.get(STONKS_API_URL + "/" + symbol + "/chart/1m")

#     # Check if the request was successful
#     if jan_response.status_code == 200 & month_response.status_code == 200:
#             # turns response into json
#             jan_data = jan_response.json()
#             month_data = month_response.json()

#             close = jan_data['close'] #close from jan_data

#             # parses through month data
#             month_entries = month_data['charts']
#             month_price = 0
#             for entry in month_entries:
#                  month_price = month_price + float(entry['close'])

#             avg_price = float(month_price/len(month_entries))

#     # adds data to the companies table
#     c.execute("INSERT INTO birds (name, symbol, location) VALUES (?, ?, ?)", (name, symbol, state)) 


# # commits changes to the table
# conn.commit()
