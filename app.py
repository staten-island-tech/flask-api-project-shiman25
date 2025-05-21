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
            'id': card.get('multiverseid'),
            'image': card.get('imageUrl')
        })

    return render_template("index.html", cards=cards)

@app.route("/detail")
def detail():
    return render_template("detail.html")




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

    
