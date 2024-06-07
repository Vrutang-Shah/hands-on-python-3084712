import csv
from flask import Flask, render_template, jsonify
import os

# folderpath = os.path.join(os.getcwd(), "Ex_Files/04_02_begin")

# laureates_path = os.path.join(os.getcwd(), "Ex_Files/04_02_begin/laureates.csv")
# print(laureates_path)

# app = Flask(__name__)

# with open("laureates.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     laureates = list(reader)


# @app.route("/")
# def index():
#     # template found in templates/index.html
#     return render_template(folderpath + "/index.html")


# @app.route("/laureates/")
# def laureate():
#     return jsonify(laureates)

# app.run()

# app.run(debug=True)

app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")

def laureate():
    return (laureates)

# def index():
#     # template found in templates/index.html
#     return render_template("index.html")


# @app.route("/laureates/")
# def laureate():
#     return jsonify(laureates)


app.run(debug=True)
