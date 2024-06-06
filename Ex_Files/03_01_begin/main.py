import csv
from pprint import pprint

import os
cwd = os.getcwd()
print(cwd)

input_path = os.path.join(cwd, r"Ex_Files/03_01_begin/laureates.csv")
print(input_path)

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

# with open(input_path, "r") as f:
#     reader = csv.DictReader(f)
#     laureates = list(reader)
#     print(laureates)
#     print("____")
#     # pprint(laureates)
#     # print("____")

# for laureate in laureates:
#     if laureate["surname"] == "Einstein":
#         pprint(laureate)
#         print("____")
#         print(laureate)
#         break


# Using Pandas
import pandas as pd

from tabulate import tabulate

df = pd.read_csv(input_path)
# pd.set_option('display.max_columns', 1)
print(df)
print(tabulate(df, headers="firstrow", tablefmt="grid"))
  
# chunk_size = 5
# i = 0
# for chunk in pd.read_csv(input_path, chunksize= chunk_size, usecols=['name', 'surname']):
#   if i == 3:
#     pprint(chunk, width = 1, depth = 1)
#   i = i + 1
#   if i > 5:
#     break
  
#   Using Numpy

# import numpy as np

# data = np.genfromtxt(input_path, delimiter = ',', dtype=None, names = True, encoding=None, usecols=['name', 'surname'])
# pprint(data, width=1, depth=100)