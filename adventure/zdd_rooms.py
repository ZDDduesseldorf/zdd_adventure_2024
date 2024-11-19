"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
import random
import time

class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            # Remove book from inventory
            return [x for x in user_items if x.name != "old book"]
        return user_items

class JungleGreenhouse(Room):
    """A new room filled with towering plants, vines, vibrant flowers and distant noises of hidden creatures.
    It creates the illusion of stepping into a tropical jungle. Located in a large greenhouse at the back of the ZDD building.

    Interactions:

    Riddle!
    A wooden bench with an old botanist sitting on it.
    The botanist gives the player a riddle to solve, claiming that solving it will unlock a secret of the greenhouse.
    The riddle could tie into the greenhouse's environment, encouraging players to interact with specific elements for clues.
    
    Watering plants: players can water certain plants using a watering can to reveal hints or interact with the environment.
    Might also trigger distractions like vines swaying or mist clouding the vision.
    """
    def __init__(self, name, description, items=None):
        """ inherited: name (str), description (str), visited (int)
        """
        super().__init__(name, description, items)
        self.riddle_status = False
        self.inspection_number = 0
        self.machete = Item("machete", "a very sharp but used machete", movable=True)
        self.water_of_youth = Item("Water of Youth", "Water from the foutain of youth from the jungle greenhouse.", movable=True)
        self.riddle_keys = {
            "thick bushes": [False, 0],
            "skylight": [False, 0],
            "intricate plant pot": [False, 0],
            "vines": [False, 0],
            "snake statue": [False, 0]
        }
        self.riddles = {
            "thick bushes": "What is can be symbol of independence, carried by those who carve their own path?\n",
            "skylight": "What glints in the moonlight, a silent guardian by night?\n",
            "intricate plant pot": "What can be an artist's brush on a canvas of a garden?\n",
            "vines": "It cuts through vines without a sound, yet speaks volumes when needed. What is it?\n",
            "snake statue": "Sharp as a serpent's tooth, yet not venomous. What am I?\n"
        }
        self.room_section_description = {
            "thick bushes": "The thick bushes form an almost impenetrable wall of green, their broad leaves glistening with moisture.\n",
            "skylight": "A massive skylight above floods the room with natural light, casting shimmering patterns on the leaves below.\n",
            "intricate plant pot": "A beautifully carved plant pot sits in a corner, its surface covered in swirling, almost hypnotic patterns. Inside, a peculiar plant with spindly stems and tiny, jewel-like flowers grows, as if thriving under someone's careful watch.\n",
            "vines": "Long, winding vines drape from the ceiling and walls, their tendrils snaking across the floor like ancient guardians.\n",
            "snake statue": "In the center of the room stands a stone statue of a coiled snake, its eyes made of gleaming emeralds that seem to follow your every move.\n"
        }
        self.botanist_response = {
            "thick bushes": "Don't you think those strong branches are the most amazing thing?\nHere's your riddle:\n",     
            "skylight": "I adore that window, wether it's the sun or moonlight pouring through.\nAnyway here's the riddle:\n",
            "intricate plant pot": "I see you found the plant pot! I could stare at those patterns for hours...\nHere's your riddle:\n",
            "vines": "Whenever I see those vines I have to fight the urge to swing from them.\nAnyway, here's your riddle:\n",
            "snake statue": "When I was a kid I used to be terrified of that weird snake, but as I've grown older, I've grown to appreciate the attention to detail.\nAnyway, here's your riddle:\n"
        }
        return

    def run_story(self, user_items):
        print("You enter an overgrown but spacious room with a massive skylight.\nThere are towering monsteras, vines and vibrant flowers all around you.\nThe air is thick and humid, and there's an eerie sense of calm.\nAn old man with small circular glasses sits on a bench, inspecting a flower.")
        self.loop_counter = 0
        while True:
            self.text_waiting_time(2)
            choice = input("Type 'approach' to talk to the botanist.\nType 'leave' to do leave\nWhat do you want to do?: ")
            if choice == "approach":
                if self.loop_counter == 0:
                    self.loop_counter += 1
                    self.text_waiting_time(2)
                    self.botanist_introduction()
                    self.hidden_room(user_items)
                    while not self.riddle_status:
                        self.current_riddle()
                        next_section = self.inspect_room()
                        self.next_riddle(next_section)
                        self.botanist_riddle(next_section)
                        self.botanist_request_answer()
                        if self.riddle_status:
                            print("Look here kid, you see that little crevase behind the snake statue?\nGo ahead, take my old machete that I have hidden over there.")
                            self.text_waiting_time(2)
                            user_items.append(self.machete)
                            print("You picked up the Item 'machete'")
                            self.text_waiting_time(2)
                        else:
                            print("I'll give you a prize if you get it right!")
                else:
                    self.hidden_room(user_items)
                    while not self.riddle_status:
                        self.current_riddle()
                        next_section = self.inspect_room()
                        self.next_riddle(next_section)
                        self.botanist_riddle(next_section)
                        self.botanist_request_answer()
                        if self.riddle_status:
                            print("Look here kid, you see that little crevase behind the snake statue?\nGo ahead, take my old machete that I have hidden over there.")
                            self.text_waiting_time(2)
                            user_items.append(self.machete)
                            print("You picked up the Item 'machete'")
                            self.text_waiting_time(2)
                        else:
                            print("I'll give you a prize if you get it right!")
                            self.text_waiting_time(2)
            elif choice == "leave":
                self.text_waiting_time(2)
                print("Heading to the door...")
                return user_items
            else:
                self.text_waiting_time(1)
                print("Invalid input")
                self.text_waiting_time(1)

    def text_waiting_time(self, wait_time):
        """
        delays printing of the next line for easier reading
        """
        time.sleep(wait_time/3) # shortening of the waiting time, adjust to liking
        print(40 * "-")
        return

    def inspect_room(self):
        """
        Main room description
        the player is prompted with 5 points of interest around the room, and can choose to approach them individually 
        """
        while True:
            print("Thick bushes form dense, rustling walls of green.\nLight streams through a skylight, illuminating the jungle below.\nAn intricate plant pot with carved patterns houses a massive plant.\nVines hang from above, their tendrils snaking across surfaces.\nA snake statue stands in the center, its emerald eyes glinting in the light.\n")
            print("You decide to look around.\n")
            for entry in self.riddles:
                print(f"Type '{entry}' to inspect the {entry}")
            print()
            choice = input("What do you want to do?: ").lower()
            self.text_waiting_time(2)
            if choice in self.riddles:
                print(f"You apprach the {choice}")
                self.text_waiting_time(2)
                return choice
            elif choice == "leave":
                print("exiting")
                return    
            else:
                print("Invalid input, try again")                   

    def botanist_introduction(self):
        """
        This function introduces the player to the botanist.
        depending on the visitation number, the player is prompted with different sentences
        """
        opening_prompts = ["Well hello there! It's been a while since anyone came to visit me. I am Dr. Sylas Thorncroft, and perhaps who might you be?\n",
                           "Look who's back already! Came to take another look at things?\n",
                           "Can't seem to get enough of the plants, can you? I can relate!?\n",
                           f"Back again for round {self.visited}?\n"]
        if self.visited == 1:
            self.player_alias = input(opening_prompts[0] + "Input your name: ")
            self.text_waiting_time(2)
            return
        else:
            print(opening_prompts[random.randint(1, 3)])
            self.player_alias = "stranger"
            return

    def current_riddle(self):
        """
        depenting on which room section the player chose to inspect in self.inspect_room() the player is confronted with the coresponding riddle 
        """
        introduction_to_riddles = f"Look around the room {self.player_alias}! If you see something interesting come back to me!\n"

        filter_for_bool = {key: value for key, value in self.riddle_keys.items() if value[0]} # filters for bools in riddle dict
        
        if not filter_for_bool:
            print(introduction_to_riddles)
        else:
            self.text_waiting_time(2)
            # most_recent_riddle = max(filter_for_bool.items(), key=lambda item: item[1][1]) # find item with highest value (second element in the list)
            # print(self.riddles[most_recent_riddle[0]])
        return

    def next_riddle(self, room_section):
        """for every visited room section the riddle_key dict is updated to true, and the inspection number is raised by one.
        -> the visitation order can be tracked, prompting specific riddles depending on the last visited section
        """
        self.inspection_number =+ 1
        self.riddle_keys[room_section] = [True, self.inspection_number]
        print(self.room_section_description[room_section])
        return

    def botanist_riddle(self, room_section):
        """This function prompts a riddle in accorance with the room section that was visited previously
        """
        print(f"After inspecting the {room_section}, you return to the old botanist.\n")
        print(self.botanist_response[room_section])
        print(self.riddles[room_section])
        return
    
    def botanist_request_answer(self):
        """This function handles the answers to the riddles, and provides hints accordingly.
        """
        while True:
            
            print("Do you know the answer?")
            player_y_n = input("Type 'yes' or 'no': ").lower()
            if player_y_n == "yes":
                print("Alright! im glad you've got something!")
                player_answer = input("What is your answer?: ").lower()
                if player_answer == "machete":
                    self.riddle_status = True
                    print("Good job on sloving the riddle! Very impressive!")
                    return
                else:
                    print(f"Sadly {player_answer} isn't the right answer.")
                    print("But I'll give you a hint! The answer is the same for all riddles!")
                    return
            elif player_y_n == "no":
                self.loop_counter += 1
                self.text_waiting_time(2)
                print("I'll give you a clue...\nThe answer is the same for all riddles!")
                if self.loop_counter == 3:
                    print()
                    print("Here's another hint: it's a very sharp object")
                elif self.loop_counter == 4:
                    print()
                    print("Here's another hint: usually its about the same size as an arm")
                elif self.loop_counter >= 5:
                    print()
                    print("Here's another hint: it's a tool used in the jungle")
                return
            else:
                print("Invalid input, try again.")

    def hidden_room(self, user_items):
        """A secret room in the greenhouse that can be accessed if the user carries a machete in their inventory
        """
        while True:
            if self.machete in user_items:
                self.text_waiting_time(2)
                print("Woha! With that machete you've got there you could really clean up those vines!")
                print()
                print("Type 'cut vines' to cut the vines")
                print("Type 'leave' to leave")
                user_input = input("What would you like to do?: ").lower()
                if user_input == "cut vines":
                    print()
                    print("You approach the vines, and with a quick swoosh...")
                    self.text_waiting_time(1)
                    print("You cut through the vines!")
                    print()
                    print("The hole in the vines reveals a tiny fountain")
                    self.text_waiting_time(5)
                    print(".")
                    self.text_waiting_time(1)
                    print(".")
                    self.text_waiting_time(1)
                    print(".")
                    self.text_waiting_time(1)
                    print("You see a little container lying next to the fountain")
                    print("Would you like to grab the container and fill it with the water?")
                    user_input2 = input("Type 'yes' to grab and 'no' to leave: ").lower()
                    if user_input2 == "yes":
                        self.text_waiting_time(2)
                        print("You found 'Water of youth'!")
                        print("Would you like to add it to you inventory?")
                        user_input3 = input("Type 'yes' to grab and 'no' to leave drop it and leave: ").lower()
                        if user_input3 == "yes":
                            user_items.append(self.water_of_youth)
                            print("Water from the fountain of youth added to inventory")
                            return user_items
                    else:
                        print()
                        return user_items
                elif user_input == "leave":
                    print("Exiting secret room")
                    self.text_waiting_time(2)
                    return user_items
                else:
                    print("Invalid input, try again")
                    self.text_waiting_time(2)
            else:
                return user_items    
            
## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.") 
greenhouse = JungleGreenhouse("greenhouse", "An overgrown greenhouse at the back of the building")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "greenhouse": greenhouse
}