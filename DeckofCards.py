

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		
class Deck:
	def __init__(self):
		self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
		self.value = ['Ace', '2','3','4','5','6','7','8','9','10','Jack','Queen','King']
		self.deck = [Card(value, suit) for value in self.value for suit in self.suits]