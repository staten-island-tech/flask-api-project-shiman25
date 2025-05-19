from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://api.magicthegathering.io/v1/cards")
    data = response.json()
    mtg_list = data['cards']
        
    cards = []
    
    for card in mtg_list:
        cards.append(card)
        #print(card['name'])
    
        
    return render_template("index.html", cards=cards)

if __name__ == '__main__':
    app.run(debug=True) 