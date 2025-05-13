import requests

response = requests.get("https://api.magicthegathering.io/v1/cards")
data = response.json()
cards = data.get("cards", [])

# Get all cards
cards = Card.all()

# Filter Cards
# You can chain 'where' clauses together. The key of the hash
# should be the URL parameter you are trying to filter on
cards = Card.where(supertypes='legendary') \
            .where(types='creature') \
            .where(colors='red,white') \
            .all()

# Get cards on a specific page / pageSize
cards = Card.where(page=50).where(pageSize=50).all()