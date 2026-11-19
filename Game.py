from Card import *
from Player import *
class Game:

    card_player = []

    card_computer = []

    Player_1 = Player("Nati",card_player)  
    Player_2 = Player("Computer",card_computer)
    @staticmethod
    def add_card():  
          shapes = ["H","D","S","C"]
          numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]
          for shape in shapes:
            for number in numbers:
                Card.cards.append(Card(number,shape))
    
    @staticmethod
    def Shuffling_cards():
       for i in range(20):
          for card in Card.cards:
            rand_1 = random.randint(0,51)
            rand_2 = random.randint(0,51)
            card_10 = Card.cards[rand_1]
            Card.cards[rand_1] = Card.cards[rand_2]
            Card.cards[rand_2] = card_10
       return Card.cards 

    @staticmethod
    def Dealing_cards():
       count = 0
       cards = Game.Shuffling_cards()
       for card in cards:
          if count % 2 == 0:
             Game.card_player.append(card)
             count +=1
          else:
             Game.card_computer.append(card)
             count += 1 

     


    def turn():
        if Game.Player_1.Deck_of_cards == [] or Game.Player_2.Deck_of_cards == []:
              print("There is a winner; the game cannot continue. Please start a new game.")
        else:   
           print("=========TURN========")
           print("player: ",Game.Player_1.Deck_of_cards[0])
           print("computer: ",Game.Player_2.Deck_of_cards[0])
           card_player = Game.Player_1.Deck_of_cards[0]
           card_computer = Game.Player_2.Deck_of_cards[0]   
           if card_player.value  > card_computer.value:
                Game.Player_1.Deck_of_cards.append(card_computer) 
                Game.Player_2.Deck_of_cards.pop(0)
                print("player won the round!")
                print("player cards: ",len(Game.Player_1.Deck_of_cards)," | computer cards: ",len(Game.Player_2.Deck_of_cards)) 
           elif card_player.value  < card_computer.value:
               Game.Player_2.Deck_of_cards.append(card_player)
               Game.Player_1.Deck_of_cards.pop(0)
               print("computer won the round!")
               print("computer cards: ",len(Game.Player_2.Deck_of_cards)," | player cards: ",len(Game.Player_1.Deck_of_cards)) 
           else:
               Game.Player_1.Deck_of_cards.pop(0)
               Game.Player_1.Deck_of_cards.append(card_player)
               Game.Player_2.Deck_of_cards.pop(0)
               Game.Player_2.Deck_of_cards.append(card_player)
               print("It's a draw!")
               print("player cards: ",len(Game.Player_1.Deck_of_cards)," | computer cards: ",len(Game.Player_2.Deck_of_cards))
           print("***********************************")


    def menu_game():
        print("""
***********************
1. New turn
2. Exit
            """)

    def start_game():        
       Game.add_card()
       Game.Dealing_cards()
       while True:
          Game.menu_game()
          choice = input("Enter your choice: ")
          if choice == "1":
             Game.turn()             
          elif choice == "2":
             exit() 
          else:
              print("Press 1 to play, or 2 to exit.") 
          

      