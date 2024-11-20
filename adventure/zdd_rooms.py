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


class ShinyAmulet(Item):
    """ A shiny amulet found in the Leaky Room.
        When present in the inventory while meeting the octopus, the game against it can be skipped.
    """
    def __init__(self):
        super().__init__(
            name="shiny amulet",
            description="A silver amulet, which looks shiny despite being in the saltwater for who knows how long.",
            movable=True
        )


class LeakyRoom(Room):
    """ An aquarium taking up a full room on the 3rd floor.
        Here the player can swim with some fish and explore the room for items
        or dive to play a rock-paper-scissors type game against an octopus.
        Removing the plug the octopus sits on transports the player to the cellar toilet.
    """
    
    def run_story(self, user_items):
        print("You see a puddle leaking out from under one of the doors\nand decide to investigate.")
        print("SPLASH")
        sleep(3)
        print("You fell directly into a giant aquarium filling the entire space!")
        print("...")
        print("A curious cowfish begins mimicking your movements!")
        print("Do you want to keep following it?")

        while True:
            action = input("Type 'swim' to swim with the fish or 'dive' to explore the bottom of the room.\nYou can also type 'leave' to swim to the rooms entrance.\n>>").lower()

            if action == "swim":
                print("There are all kinds of colourfull fish in the water.")
                print("After a while, the cowfish comes up to you again.")
                while True:
                    following_action = input("Type 'cowfish' to keep swimming with your little friend,\nor 'seahorses' to make some new ones.\n>>").lower()
                    
                    if following_action == "cowfish":
                        if "shiny amulet" not in [item.name for item in user_items]:
                            print("After some time, Daisy (the cowfish, which you named just now)\nleads you to a rock crevice.")
                            print("There you find a shiny amulet. You decide to pick it up.")
                            # adds shiny amulet to inventory
                            user_items.append(ShinyAmulet())
                            sleep(1)
                        else:
                            print("You decide to play with Daisy for a bit.")
                            print("After some fun swimming with her, you return to the entrance.")
                        break
                        
                    elif following_action == "seahorses":
                        print("You decide to swim to a rock with some coral and a bunch of seahorses on and around it.")
                        print("After watching the seahorses gallop (?) around for a while, you decide to swim\nback to the entrance.")
                        break

                    else:
                        print("Invalid action!")


            elif action == "dive":
                print("You dive to the bottom of the aquarium and find a giant plug.")
                print("An octopus is sitting on it and it does not seem like it wants to budge.")
                if "shiny amulet" in [item.name for item in user_items]:
                    sleep(3)
                    print("Suddenly the octopus takes the shiny amulet from your pocket!")
                    print("Thief... At least the plug is free now.")
                    # removes shiny amulet from inventory
                    user_items[:] = [item for item in user_items if item.name != "shiny amulet"]
                else:
                    print("The octopus looks at you, condescendingly.")
                    sleep(1)
                    if self.rock_seagrass_seaglass():
                        print("You win! The octopus moves away from the plug.")
                    else:
                        print("The octopus wins... Maybe you can try again later.")
                        break

                while True:
                    following_action = input("Type 'pull' to pull the plug or 'leave' to return to the surface:\n>>").lower()
                    if following_action == "pull":
                        print("You pull the plug. The aquarium drains, and you are transported to...")
                        print("The toilet in the cellar!")
                        print("After the wild ride down here you anticipate that something even crazier\nmight happen any moment.")
                        print("...")
                        return ALL_ROOMS["toilet_cellar"].run_story(user_items)
                    elif following_action == "leave":
                        break
                    else:
                        print("Invalid action!")

            elif action == "leave":
                break

            else:
                print("Invalid action!")

        return user_items


    def rock_seagrass_seaglass(self):
        """Rock-paper-scissors type game played against the octopus."""
        print("You see the octopus lay out some rocks, seagrass and seaglass.")
        print("It seems it wants to challenge you to a game,\nwhich reminds you of rock-paper-scissors.")
        sleep(1)
        print("The match is on!")

        choices = ["rock", "seagrass", "seaglass"]
        while True:
            player_choice = input(">> Choose 'rock', 'seagrass', or 'seaglass': ").lower()
            if player_choice not in choices:
                print("Invalid choice! Please choose 'rock', 'seagrass', or 'seaglass'.")
                continue

            octopus_choice = random.choice(choices)
            sleep(1)
            print(f"The octopus chooses {octopus_choice}!")

            # tie
            if player_choice == octopus_choice:
                print("It's a tie! Try again.")
            # player wins
            elif (player_choice == "rock" and octopus_choice == "seaglass"):
                print("You smash the octopusses seaglass into tiny pieces!")
                return True
            elif (player_choice == "seagrass" and octopus_choice == "rock"):
                print("You envelop the octopusses rock with your seagrass!")
                return True
            elif (player_choice == "seaglass" and octopus_choice == "seagrass"):
                print("You cut the octopusses seagrass with the sharp edge of your glass!")
                return True
            # player loses  
            else:
                return False  
   


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


# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

leaky_room = LeakyRoom("leaky room", "An aquarium taking up a full room on the 3rd floor.")
table_tennis_room = TableTennisRoom("table tennis room", "A room where you can play table tennis.")


ALL_ROOMS = {
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "toilet_cellar": toilet_cellar,

    "leaky_room": leaky_room,
    "table_tennis_room": table_tennis_room
}

