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

        name = card.get('name')
        
        id = card.get('multiverseid')
        if id:
            id = int(id.strip("'"))
            cards.append({'name': name, 'id': id})

    return render_template("index.html", cards=cards)

@app.route("/detail/card/<int:id>")
def detail(id):
    response = requests.get(f"https://api.magicthegathering.io/v1/cards/{id}")
    data = response.json()  

    mtg_list = data['cards']
    cards = []
    image= []
    for card in mtg_list:
        image.append(card.get('imageUrl'))
        cards.append(card)
        #image.append("No Image")
        

    return render_template("detail.html",card = card, image = image)
if __name__ == '__main__':
    app.run(debug=True) 