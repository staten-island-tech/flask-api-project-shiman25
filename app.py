from flask import Flask, render_template
import requests
app = Flask(__name__)




response = requests.get("https://api.magicthegathering.io/v1/cards")
data = response.json()
    
cards = data["cards"]
for card in cards:

    if card["cmc"] < 5:
        print(card['name'])