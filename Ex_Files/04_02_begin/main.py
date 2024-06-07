from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello Vrutang!"

# app.run(debug = True)
app.run()
