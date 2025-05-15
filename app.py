import requests

response = requests.get("https://api.magicthegathering.io/v1/cards")
data = response.json()
cards = data.get("cards", [])

# Get all cards
cards = Card.all()

# Get cards on a specific page / pageSize
cards = Card.where(page=50).where(pageSize=50).all()