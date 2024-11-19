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

import random

import random

import random

class DarkAcademiaRoom(Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.notebook = ["digital", "computer", "science", "machine", "learning", "data", "artificial", "modern"]
        
        """
        Initialize the DarkAcademiaRoom with a name, description, and a list of words 
        for the text challenge.
        """

    def get_correct_sentence(self):
        """
        Returns the correct sentence that the player needs to match by filling in the blanks.
        This sentence is used for comparison after the player completes the text challenge.
        """
        return "The digital revolution has transformed computer and science fields with artificial intelligence."

    def start_adventure(self):
        """
        Starts the adventure by greeting the player and asking them to solve a math question
        to unlock the notebook. After the math question is answered correctly, the player can 
        choose to solve the text challenge or not.
        """
        print("Welcome to the Dark Academia Room!")
        print("Answer a math question correctly to access the secret tattered notebook.")
        
        if self.ask_math_question():
            print("\nCorrect! You now have access to the notebook.")
            print("Do you want to solve the text challenge? (yes/no)")
            if input().lower() == "yes":
                self.text_challenge()
            else:
                print("Maybe next time. Goodbye!")
        else:
            print("Wrong answer. Access denied. Goodbye!")

    def ask_math_question(self):
        """
        Asks the player a simple math question (addition of two random numbers between 1 and 10).
        If the player answers correctly, the function returns True. Otherwise, it returns False.
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

    def text_challenge(self):
        """
        Presents the player with a text challenge where they need to fill in the blanks 
        with words from the notebook. After filling in the blanks, the text is checked 
        against the correct sentence.
        """
        text = "The __ revolution has transformed __ and __ fields with __ intelligence."
        print(f"\nFill in the blanks:\n{text}")
        completed_text = self.fill_blanks(text, self.notebook)
        print("\nYour completed text:")
        print(completed_text)
        
        if completed_text == self.get_correct_sentence():
            print("\nGreat job! You completed the text and unlocked the ZDD's secrets.")
        else:
            print("\nText completed, but it didn't match the expected sentence. Keep trying!")

    def fill_blanks(self, text, words):
        """
        Fills in the blanks in the text using the words provided. The player chooses a word 
        for each blank from the available list. The function keeps track of the words used 
        and updates the text until all blanks are filled.
        """
        gaps = text.count("__")
        for i in range(gaps):
            print(f"\nChoose from: {', '.join(words)}")
            user_word = input(f"Fill gap {i + 1}: ").strip()
            while user_word not in words:
                user_word = input("Invalid word. Choose from the list: ").strip()
            text = text.replace("__", user_word, 1)
            words.remove(user_word)
            print(f"Updated text: {text}")
        return text



toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
dark_academia_room = DarkAcademiaRoom("dark_academia_room", "It's a dark room with a lot of books and a computer")

ALL_ROOMS = {
        "toilet_cellar": toilet_cellar,
        "dark_academia_room": dark_academia_room
}