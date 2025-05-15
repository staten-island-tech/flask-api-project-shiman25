from flask import Flask, render_template
import requests
app = Flask(__name__)




@app.route('/')
def index():
    response = requests.get("https://api.magicthegathering.io/v1/cards")
    data = response.json()
    
    for card in data:
        print(card)

