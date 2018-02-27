
import sys
import random

#to call a class from a .py file i need to say "from" to specify which file and then "import" then the specific class
from DeckofCards import Deck
watchdog = 0

while watchdog <= 4:
    Shuf = input('Shuffle? Enter Y (yes) or N (no): ')
    if Shuf == "Y" or Shuf == "y" or Shuf == "N" or Shuf == "n":
        break
    elif watchdog <=2:
        print('Wrong Input. Please Try Again...')
        watchdog += 1
    elif watchdog > 2 and watchdog < 4:
        print('I remember when I first learned to read. Please enter Y or N')
        watchdog += 1
    else:
        print('Since you apparently can\'t read. I\'m a chunky monkey from funky town')
        print('\n\nExiting Program')
        sys.exit()
watchdog = 0

while watchdog <= 4:
    while True:
        try:
            Draw = int(input('How many cards would you like to draw. Up to 10 cards at a time: '))
            break
        except:
            Draw = -1
            break
        
    if  Draw >= 1 and int(Draw) <= 10:
        break
    elif watchdog <=2:
        print('Wrong Input. Please Try Again...')
        watchdog += 1
    elif watchdog > 2 and watchdog < 4:
        print('If you can read, did you make it this far just by luck?')
        watchdog += 1
    else:
        print('Well, you tried...')
        print('\n\nExiting Program')
        sys.exit()

counter = 0

deck = Deck()

#deck in this def is not a public variable. Cannot be used outside
def shuffledatbigdeck(deck):
    random.shuffle(deck)
    return
#shuffle
if Shuf == "Y":
    shuffledatbigdeck(deck.deck)
    while counter < Draw:
        print('\n* ', deck.deck[counter].value,'of', deck.deck[counter].suit)
        counter += 1
#no shuffle
else:
    while counter < Draw:
        print('\n* ', deck.deck[counter].value,'of', deck.deck[counter].suit)
        counter += 1



    