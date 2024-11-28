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

                    

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


table_tennis_room = TableTennisRoom("table tennis room", "A room where you can play table tennis.")


class DarkAcademiaRoom(Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.notebook_item = Item(
            "notebook",
            "A tattered notebook filled with cryptic words and phrases.",
            movable=True
        )
        self.notebook_words = ["digital", "computer", "science", "machine", "learning", "data", "artificial", "modern"]

    def enter_room(self, user_items, command_handler=None):
        """
        Called when the player enters the room. Starts the adventure.
        """
        print(f"You enter the {self.name}. {self.description}")
        self.start(user_items)

    def get_correct_sentence(self):
        """
        The correct sentence for the text challenge.
        """
        return "The digital revolution has transformed computer and science fields with artificial intelligence."

    def start(self, user_items):
        """
        Begins the adventure. The player must answer a math question correctly to unlock the notebook.
        """
        print("Welcome to the Dark Academia Room!")
        print("Answer a math question correctly to access the secret tattered notebook.")

        if self.question():
            print("\nCorrect! You now have access to the notebook.")
            user_items.append(self.notebook_item)  # Add the notebook to the player's inventory.
            print("The notebook has been added to your inventory.")
            print("Do you want to discover the secrets of ZDD? (yes/no)")
            if input().lower() == "yes":
                self.text_challenge(user_items)
            else:
                print("Maybe next time. Goodbye!")
        else:
            print("Wrong answer. Access denied. Goodbye!")

    def question(self):
        """
        Asks a math question. Returns True if the answer is correct, otherwise False.
        """
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        print(f"What is {num1} + {num2}?")

        try:
            user_answer = int(input("Your answer: "))
            return user_answer == correct_answer
        except ValueError:
            print("Invalid input.")
            return False

    def text_challenge(self, user_items):
        """
        Provides a text challenge if the player has the notebook. The player fills in the blanks using notebook words.
        """
        if self.notebook_item not in user_items:
            print("You don't have the notebook to attempt this challenge.")
            return

        print("\nFill in the blanks in the following text:")
        text = "The __ revolution has transformed __ and __ fields with __ intelligence."
        completed_text = self.fill_blanks(text, self.notebook_words[:])
        print("\nYour completed text:")
        print(completed_text)

        if completed_text == self.get_correct_sentence():
            print("\nWell done! You completed the text and unlocked the ZDD's secrets.")
        else:
            print("\nUnfortunately, the text is incorrect. The secrets remain hidden.")

    def fill_blanks(self, text, words):
        """
        Fills in the blanks in the given text using words from the notebook.
        """
        gaps = text.count("__")
        print(text)
        for i in range(gaps):
            print(f"\nChoose from: {', '.join(words)}")
            user_word = input(f"Fill gap {i + 1}: ").strip()
            while user_word not in words:
                user_word = input("Invalid word. Choose from the list: ").strip()
            text = text.replace("__", user_word, 1)
            words.remove(user_word)
            print(f"Updated text: {text}")
        return text


class ToiletCellar(Room):
    def __init__(self, name, description):
        super().__init__(name, description)


toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
dark_academia_room = DarkAcademiaRoom("dark_academia_room", "It's a dark room with a lot of books and a computer!")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "dark_academia_room": dark_academia_room,
    "table_tennis_room": table_tennis_room
}