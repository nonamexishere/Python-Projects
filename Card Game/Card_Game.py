import random
import time
class Card:
    def __init__(self,kind,value):
        self.kind = kind
        self.value  = value
    def getCard(self):
        return f'{self.value} of {self.kind}'
    
class Deck:
    def __init__(self):
        self.kinds = ["Spades", "Diamonds", "Hearts", "Clubs"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.rounds_played = 0
        self.score = 0
        self.myCards = []
        self.botCards = []    
        self.cards = []
        for i in self.kinds:
            for j in self.values:
                a = Card(i,j)
                self.cards.append(a.getCard())

    def remainingCards(self):
        print(f'Number of cards remaining {len(self.myCards)}!')

    def shuffleDeck(self):
        random.shuffle(self.cards)

    def showCards(self):
        print("Your Cards: ")
        if len(self.myCards) >= 3:
            third = int((len(self.myCards)+2) / 3)
            for i in range(third):
                print(f'{self.myCards[i]}', end="\t")
            print("")
            for i in range(third,2*third):
                print(f'{self.myCards[i]}', end="\t")
            print("")
            for i in range(2*third,len(self.myCards)):
                print(f'{self.myCards[i]}', end="\t")
            print("")
        else:
            for i in self.myCards:
                print(f'{i}')
        print("Opponent's Cards: ")
        if len(self.botCards) >= 3:
            third = int((len(self.botCards)+2) / 3)
            for i in range(third):
                print(f'{self.botCards[i]}', end="\t")
            print("")
            for i in range(third,2*third):
                print(f'{self.botCards[i]}', end="\t")
            print("")
            for i in range(2*third,len(self.botCards)):
                print(f'{self.botCards[i]}', end="\t")
            print("")
        else:
            for i in self.botCards:
                print(f'{i}')

    def dealCards(self,amount):
        i = 0 
        while i < amount:
            a = random.choice(self.cards)
            self.myCards.append(a)
            self.cards.remove(a)
            b = random.choice(self.cards)
            self.botCards.append(b)
            self.cards.remove(b)
            i+=1

    def playCard(self,choice):
        if choice in self.myCards:
            choice_of_bot = random.choice(self.botCards)
            print("")
            print("**********************************************************")
            print(f'You played {choice} and the opponent played {choice_of_bot}')
            if self.values.index(choice.split()[0]) > self.values.index(choice_of_bot.split()[0]):
                print("*********************** You won! ***********************")
                self.score += 1
                self.rounds_played += 1
                print(f'Rounds played: {self.rounds_played} \n Your score: {self.score}')
                self.myCards.remove(choice)
                self.botCards.remove(choice_of_bot)
            elif self.values.index(choice.split()[0]) < self.values.index(choice_of_bot.split()[0]):
                print("*********************** Bot wins :( ***********************")
                self.rounds_played += 1
                print(f'Rounds played: {self.rounds_played} \n Your score: {self.score}')
                self.myCards.remove(choice)
                self.botCards.remove(choice_of_bot)
            else:
                print("*********************** It is tie! ***********************")
                self.score += 1/2
                self.rounds_played += 1
                print(f'Rounds played: {self.rounds_played} \n Your score: {self.score}')
                self.myCards.remove(choice)
                self.botCards.remove(choice_of_bot)
            if len(self.myCards) > 0:
                self.remainingCards()
                self.showCards()
                new_choice = input("Please select a new card: ")
                self.playCard(new_choice)
            else:
                self.remainingCards()
                print("The game is over!")
                print(f"Your score: {self.score} Your opponent's score: {self.rounds_played - self.score}")
                if self.score > (self.rounds_played - self.score):
                    print("You are the CHAMPION!!")
                elif self.score < (self.rounds_played - self.score):
                    print("Bot won, maybe next time")
                else:
                    print("Friendship won :)")
        else:
            self.showCards()
            new_choice = input("Please select a proper card: ")
            self.playCard(new_choice)

    def startGame(self):
        print("Your game is about the start")
        print("Loading 12%")
        time.sleep(1)
        print("Loading 53%")
        time.sleep(2)
        print("Let's goo!!")
        # amount = int(input("How many round are you willing to play:(26 Maximum - 1 Minimum) "))
        try:
            amount = int(input("How many round are you willing to play(min 1 max 26): "))
            if amount > 26:
                amount = 26
            elif amount < 1:
                amount = 1
        except:
            print("Please enter a number")
        self.dealCards(amount)
        self.showCards()
        first_choice = input("Which card is your choice: ")
        self.playCard(first_choice)
    
deck = Deck()
deck.startGame()
