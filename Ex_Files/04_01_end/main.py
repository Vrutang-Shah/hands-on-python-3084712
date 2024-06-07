# import requests

# response = requests.get(
#     "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

# last_twenty_years = response.json()[1][:20]

# for year in last_twenty_years:
#     display_width = year["value"] // 10_000_000
#     print(f'{year["date"]}: {year["value"]}', "=" * display_width)

import requests
from pprint import pprint
import json

response = requests.get("http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

# print(response.status_code)
# pprint(response.json()[1][:20])
# print(response.text)

last_20_year_data = response.json()[1][:20]

# pprint(json.dumps(response.json()[1][:20], indent = 4))

# print(type(data["value"]))

for data in last_20_year_data:
    # print(isinstance(data['value'], int))
    if isinstance(data["value"], int):
        display = data["value"] // 10000000
        print(f'{data["date"]}: ', "=" * display)
        
    # x = data['value']
    # pprint(x)
    # display = data["value"] // 10000000
    # print(f'{data["date"]}: ', '=' * display)
    