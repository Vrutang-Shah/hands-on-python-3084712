import csv
import json
from pprint import pprint
import os

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

# einstein_json = json.dumps(EINSTEIN)
# back_to_dict = json.loads(einstein_json)
# print(einstein_json)
# pprint(back_to_dict)

cwd = os.getcwd()
input_path_csv = os.path.join(cwd, r"Ex_Files/03_01_begin/laureates.csv")
input_path_json = os.path.join(cwd, r"Ex_Files/03_01_begin/laureates.json")

with open(input_path_csv, "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# print(laureates)


# 1. you can access parts of strings the same way you do lists
#      hey[2] == "y"
# 2. You can add to a list using
#      my_list.append("something")

laureates_beginning_with_a = []
# LinkedIn learner code here
# i = 0
for each in laureates:
    # print(each['name'])
    # i = i + 1
    # if i > 2:
    #     break

    if each['name'][0] == 'A':
        laureates_beginning_with_a.append(each)

# print(laureates_beginning_with_a)


with open(input_path_json, "w") as f:
    json.dump(laureates_beginning_with_a, f, indent=2)
