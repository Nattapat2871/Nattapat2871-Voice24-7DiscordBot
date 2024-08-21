from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running. Join us at https://discord.gg/fxHSfme4ch"

def run():
    app.run(host='0.0.0.0', port=8080)

def server_on():
    t = Thread(target=run)
    t.start()
