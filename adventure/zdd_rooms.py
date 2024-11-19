"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
from time import sleep
import random


class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            # Remove book from inventory
            return [x for x in user_items if x.name != "old book"]
        return user_items

## ----------------------------------------------------------------
## List here all rooms


class TableTennisRoom(Room):

    training_score = 0
    skills = []

    

    def play_match(self):
        """
        Simulates a table tennis match between the player and the robot.

        First, the player and the robot decide who has the first serve by
        choosing a number between 1 and 2. If the player's number matches the
        random number, the player has the first serve.

        Then the actual match begins. The player's winning probability is
        determined by their training score. The player wins if their winning
        probability is higher or equal to a random number between 0 and 4.
        """
        print()
        print("To start the match, we need to choose who has the first serve.")
        print("If your number is equal to a random number between 1 and 2, you get the first serve.")
        first_serve_input = input("Choose number 1 or 2: ")
        first_serve = random.randint(1, 2)

        if first_serve == int(first_serve_input):
            print("You have the first serve! Good luck!")

        else:
            print("The robot has the first serve! Good luck!")

        winning_probability = self.training_score
        random_number = random.randint(0, 4)

            
        if winning_probability >= random_number:
            sleep(3)
            print("You won the match! Congratulations!")
                    

        elif winning_probability < random_number:
            sleep(3)
            print("The robot won the match! Better luck next time.")
            print("Maybe you should train a bit more.")
                    

    def train(self):
        """
        Train a specific table tennis skill to improve the player's chance of winning a match.

        The player can choose to train either 'attack', 'defense', or 'service'. If the player
        chooses to train a skill that they already have, they will be asked to choose another
        skill to train.

        The training process takes 3 seconds and will increase the player's training score by 1.
        """
        print()
        print("You decide to train to improve your game.")

        while True:
            training_choice = input("What would you like to train? 'attack', 'defense', or 'service': ")

            if training_choice in self.skills:
                print("You already trained your", training_choice + "!")
                print("I think you should focus on another skill instead.")

            else:
                print("OK let's improve your", training_choice + "!")
                sleep(3)
                self.training_score += 1
                self.skills.append(training_choice)
                print("Wow your", training_choice + " looks really good now!")
                break

            

    def run_story(self, user_items):

        """
        main loop
        When the player enters the room, they are asked if they want to play a match or train.
        If they choose to play a match or tain, they need to have a racket in their inventory. 
        If they don't have a racket, they are asked if they want to buy one.
        If they choose to leave the room, the function will break the loop and return the user_items.

        """
        
        print("Welcome to the ZDD Table Tennis Room where you can play table tennis.")
        print("Here you can play a match against a robot or train to improve your game.")


        while True:
            print()
            choice = input ("You're in the ZDD Table Tennis Room. Would you like to play a match, train or leave the room? (match/train/leave): ")

            if choice == "match":
               
                if "table tennis racket" in [item.name for item in user_items]:
                    self.play_match()

                elif "table tennis racket" not in [item.name for item in user_items]:	
                    print("You don't have a racket. You need a racket to play table tennis.")
                    racket_input = input("Would you like to borrow a racket? (yes/no): ")

                    if racket_input == "yes":
                        table_tennis_racket = Item("table tennis racket", "a table tennis racket", movable=True)
                        user_items.append(table_tennis_racket)
                        print("You borrowed a racket. Let's play a match!")
                        self.play_match()

                    elif racket_input == "no":
                        print("Sorry, you can't play table tennis without a racket.")

                    else:
                        print("Invalid choice. Please try again.")

            
            elif choice == "train":

                if "table tennis racket" in [item.name for item in user_items]:
                    self.train()
                    

                elif "table tennis racket" not in [item.name for item in user_items]:
                    print("You need a racket to train.")
                    racket_input = input("Would you like to borrow a racket? (yes/no): ")

                    if racket_input == "yes":
                        table_tennis_racket = Item("table tennis racket", "a table tennis racket", movable=True)
                        user_items.append(table_tennis_racket)
                        print("You borrowed a racket. Now we can start the training session!")
                        self.train()
                        

                    elif racket_input == "no":
                        print("Sorry, you can't play table tennis without a racket.")

                    else:
                        print("Invalid choice. Please try again.")
                        

            elif choice == "leave":
                break

            else:
                print("Invalid choice. Please try again.")

class LibraryRoom(Room):
    """
    Represents a library room filled with bookshelves and armchairs.
    Players can browse shelves or select books with hidden letters.
    """
    def __init__(self, name, description, items=None):
        super().__init__(name, description, items)

    def run_story(self, user_items):
        """
        Contains the story and interactions for the library room.
        Players can browse shelves or select a book.
        """
        print("\nYou enter a warm, inviting room filled with bookshelves and soft armchairs.")
        while True:
            print("\nOptions:")
            print("1. Browse the shelves.")
            print("2. Select a book.")
            print("3. Leave the library.")
            action = input("What would you like to do? (1/2/3): ").strip()
            
            if action == "1":
                self.browse_shelves()
            elif action == "2":
                user_items = self.select_book(user_items)
            elif action == "3":
                print("You leave the library, feeling more knowledgeable.")
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        return user_items

    def browse_shelves(self):
        """
        Simulates browsing shelves where players discover hidden notes.
        """
        print("\nYou wander along the shelves, admiring the variety of books.")
        print("Tucked between the pages of an old book, you find a handwritten note.")
        print("The note reads: 'Knowledge is the key to all doors.'")

    def select_book(self, user_items):
        """
        Allows players to select a book or letter to take with them.
        Adds the item to the player's inventory if selected.
        """
        book = Item("ancient tome", "A mysterious ancient tome filled with cryptic symbols.", movable=True)
        letter = Item("letters", "A collection of personal letters tucked between books.", movable=True)

        while True:
            print("\nAvailable items:")
            print("1. Ancient Tome")
            print("2. Letters")
            print("3. None")
            choice = input("Which item would you like to take? (1/2/3): ").strip()

            if choice == "1":
                if book.is_movable(user_items):
                    user_items.append(book)
                    print("You take the Ancient Tome with you.")
                    break
            elif choice == "2":
                if letter.is_movable(user_items):
                    user_items.append(letter)
                    print("You take the Letters with you.")
                    break
            elif choice == "3":
                print("You decide not to take anything.")
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        return user_items
                    

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


table_tennis_room = TableTennisRoom("table tennis room", "A room where you can play table tennis.")
library = LibraryRoom("library", "A warm and inviting corner filled with bookshelves and soft armchairs.")
ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room

    "table_tennis_room": table_tennis_room,
    "library": library
}
