from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://api.magicthegathering.io/v1/cards")
    data = response.json()
    mtg_list = data['cards']
        
    cards = []
    images = []
    for card in mtg_list:
        cards.append(card['name'])
        images.append(card.get("imageUrl"))
        
        cards.append({
            'name': card['name'],
        })

    return render_template("index.html", cards=cards)

@app.route("/detail/card.name")
def detail():
    response = requests.get(f"https://api.magicthegathering.io/v1/cards")
    data = response.json()
    card = data.get()
    name = card['name'],
    id = card.get('multiverseid'),
    image = card.get('imageUrl')

    return render_template("detail.html", card=
        image = image,
        
                           
        )

if __name__ == '__main__':
    app.run(debug=True) 
""" 
from flask import Flask, render_template
import requests
app = Flask(__name__)



response = requests.get("https://api.magicthegathering.io/v1/cards")
data = response.json()
mtg_list = data['cards']
        
cards = []
image=[]
for card in mtg_list:
        cards.append(card)
        image.append(card.get('imageUrl'))

print(image)
        #print(card['name'])     """

    
