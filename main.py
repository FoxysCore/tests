from flask import Flask
from threading import Thread
from time import sleep
from requests import get

app = Flask('')


@app.route('/')
def home():
  return "I'm alive"


def run():
  app.run(host='0.0.0.0', port=80)
