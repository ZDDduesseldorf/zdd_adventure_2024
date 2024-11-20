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

class AtelierStudio(Room):

    def inspect_paintings(self):
        
        """
        Inspects the paintings in the art studio.
        There are 3 paintings in the art studio. The player can choose which ones to inspect.
        """

        inspect_story = (
            "You decide to inspect the paintings in the art studio and notice there are three different artworks. \n"
            "Type 'painting1' to inspect the first painting.\n"
            "Type 'painting2' to inspect the second painting.\n"
            "Type 'painting3' to inspect the third painting.\n"
            "Type 'stop' to stop looking at the paintings."
            )
        print(inspect_story)

        while True:
            painting_choice = input("Which painting would you like to inspect? (painting1/painting2/painting3/stop): ").lower()

            if painting_choice == "painting1":
                print("You look at the first painting and see this...")
                print(r"""
    %%%
   =====
  &%&%%%&
  %& < <% 
   &\__/
    \ |____
   .', ,  ()
  / -.  _)| 
 |_(_.    |
 '-'\  )  |
 mrf )    |
    /  .  ).
   /    _. |
 /'---':.-'|
(__.' /    /
 \   ( /  /
  \ /  _  | 
   \  |  '|
   | . \  |
   |(     | 
   |  \ \ |
    \  )\ |
   __)/ / \
--"--(_.Ooo'----""")
                print("This painting looks like the Venus de Milo. Why would someone who is such a good artist study data science?")
            elif painting_choice == "painting2":
                print("You look at the second painting and see this...")
                print(r"""      
                _____
             ,-"     "-.
            / o       o \
           /   \     /   \
          /     )-"-(     \
         /     ( 6 6 )     \
        /       \ " /       \
       /         )=(         \
      /   o   .--"-"--.   o   \
     /    I  /  -   -  \  I    \
 .--(    (_}y/\       /\y{_)    )--.
(    ".___l\/__\_____/__\/l___,"    )
 \                                 /
  "-._      o O o O o O o      _,-"
      `--Y--.___________.--Y--'
         |==.___________.==| hjw
         `==.___________.==' `97""")
                print("This painting is very strange. You notice the artist left a comment in the bottom-left corner:\n")
                print("'I saw this through the telescope in the ZDD and was never the same again...'")
            elif painting_choice == "painting3":
                print("You look at the third painting and see this...")
                print(r"""      
       _________
      /         \
     /           \
    |    O   O    |
    |      ^       |
    |     '-'      |
     \___________/ 
        /       \
       /         \
      |           |
      |           |
       \_________/ """)
                print("What the hell is this supposed to be? It looks like a child's drawing!")
                print("You notice a small note on the bottom right corner:\n")
                print("'I'm a data scientist, not an artist.'\n You agree.")
            elif painting_choice == "stop":
                break
            else:
                print("This painting doesn't exist. Please enter one of the choices above.")

    def paint_something(self, user_items):
        """
        Paints a picture in the art studio.

        The player can choose to paint a picture of a computer, a cat, or a person.
        If the player chooses to paint a picture the function will add the painting to the inventory.
        """
        paint_something_story = ("You suddenly feel the urge to be creative. Maybe you were meant to be an artist all along."
                                 "Type computer to paint a computer.\n"
                                 "Type cat to paint a cat.\n"
                                 "Type person to paint a person.\n"
                                 "Type stop to stop painting."
                                 )
        print(paint_something_story)

        while True:
            painting_choice = input("What are you goint to paint? (computer/cat/person/stop): ").lower()

            if painting_choice == "computer":
                print("Like a real data scientist you decide to paint a computer.")
                print("These are the fruits of your creativity:")
                print(r"""   
   _______________                        |*\_/*|________
  |  ___________  |     .-.     .-.      ||_/-\_|______  |
  | |           | |    .****. .****.     | |           | |
  | |   0   0   | |    .*****.*****.     | |   0   0   | |
  | |     -     | |     .*********.      | |     -     | |
  | |   \___/   | |      .*******.       | |   \___/   | |
  | |___     ___| |       .*****.        | |___________| |
  |_____|\_/|_____|        .***.         |_______________|
    _|__|/ \|_|_.............*.............._|________|_
   / ********** \                          / ********** \
 /  ************  \                      /  ************  \
--------------------                    --------------------""")
                print("You are suprised by your sudden romanticism. But your are happy with the result.")
                computer_painting = Item("computer painting", "a painting of two computers", movable=True)
                user_items.append(computer_painting)

            elif painting_choice == "cat":
                print("You decide to paint a cat. Not very creative but you are a data scientist not an artist.")
                print("These are the fruits of your creativity:")
                print(r"""       
                        _
                       | \
                       | |
                       | |
  |\                   | |
 /, ~\                / /
X     `-.....-------./ /
 ~-. ~  ~              |
    \             /    |
     \  /_     ___\   /
     | /\ ~~~~~   \ |
     | | \        || |
     | |\ \       || )
    (_/ (_/      ((_/""")
                print("You painted a cat! It looks great!")
                cat_painting = Item("cat painting", "a painting of a cat", movable=True)
                user_items.append(cat_painting)

            elif painting_choice == "person":
                print("You decide to go all out and paint a whole person. It seems like you are feeling very creative today.")
                print("These are the fruits of your creativity:")
                print(r"""       
                      O
                     /|\
                     / \ """)
                print("Now this is really embarassing! You should stick to data science. You also don't want to keep this painting.")
                print("You throw the painting in the trash before anyone can see it.")
            elif painting_choice == "stop":
                break
            else:
                print("Invalid choice. Please try again.")

        return user_items
            

    def run_story(self, user_items):
    
        """
        When the player enters the room, they are presented with a story and choices to make.
        The player can choose to inspect the paintings or leave the room.
        """

        atelier_story = (
            "You slowly open the door and enter the room. It is an art studio!\n"
            "Why do we even have an art studio? I thought we were a data science lab?\n"
            "As you try to make sense of it all, you notice some canvases are already painted.\n"
            "You wonder - should you look at the paintings or just leave?\n"
            "Type 'look' to look at the other paintings.\n"
            "Type 'paint' to paint something."
            "Type 'leave' to leave the room."
            )
        print(atelier_story)

        while True:
            user_choice = input("What would you like to do? (look/paint/leave): ").lower()

            if user_choice == "look":
                self.inspect_paintings()
            elif user_choice == "paint":
                self.paint_something(user_items)
            elif user_choice == "leave":
                break
            else:
                print("Sadly that's impossible. Please enter one of the choices above.")

        
        

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
atelier_studio = AtelierStudio("atelier studio", "A space full of confusion and creativity.")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room

    "table_tennis_room": table_tennis_room,
    "atelier_studio": atelier_studio
}
