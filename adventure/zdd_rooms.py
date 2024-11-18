"""This is to keep all special rooms of the ZDD."""
from main_classes import Room
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
        pass
    
    def text_waiting_time(self, time):
        # time.sleep(time)
        print(40 * "-")
        # time.sleep(time)
        pass

    def inspect_room(self):
        print("Thick bushes form dense, rustling walls of green.\nLight streams through a skylight, illuminating the jungle below.\nAn intricate plant pot with carved patterns houses a massive plant.\nVines hang from above, their tendrils snaking across surfaces.\nA snake statue stands in the center, its emerald eyes glinting in the light.\n")
        print("You decide to look around.\n")
        for entry in self.riddles:
            print(f"Type '{entry}' to inspect the {entry}")
        choice = input("What do you want to do?: ").lower()
        self.text_waiting_time(2)
        if choice in self.riddles:
            print(f"You apprach the {choice}")
            self.text_waiting_time(2)
        else:
            print("choice not recognized")
        return choice    

    def botanist(self):
        """The botanist gives the player riddles they all have the same

        The botanist has 5 riddles with the same result: "machete"

        this should encourage the player to look around the room and look for clues
        depending on which item the player brings back the botanist will give more clues, or a prize
        """
        opening_prompts = ["Well hello there! It's been a while since anyone came to visit me. I am Dr. Sylas Thorncroft, and perhaps who might you be?\n",
                           "Look who's back already! Came to take another look at things? Remind me of your name please\n",
                           "Can't seem to get enough of the plants, can you? I can relate! Remind me of your name again?.\n",
                           f"Back again for the {self.visited}th time? I still can't remember your name! Tell me again?\n"]
        if self.visited == 1:
            self.player_alias = input(opening_prompts[0] + "Input your name: ")
            self.text_waiting_time(2)
        else:
            self.player_alias = input(opening_prompts[random.randint(1, len(opening_prompts) - 1)] + "Input your name: ")
            self.text_waiting_time(2)
        pass

    def current_riddle(self):
        """depending on which part of the room the player had the most recent interaction with,
        they are prompted with a specific riddle when returning to the botanist
        """
        introduction_to_riddles = f"Look around the room {self.player_alias}! If you see something interesting come back to me!\n"

        filter_for_bool = {key: value for key, value in self.riddle_keys.items() if value[0]} # filters for bools in riddle dict
        
        if not filter_for_bool:
            print(introduction_to_riddles)
        else:
            most_recent_riddle = max(filter_for_bool.items(), key=lambda item: item[1][1]) # find item with highest value (second element in the list
            print(self.riddles[most_recent_riddle[0]])
        pass

    def next_riddle(self, room_section):
        """for every visited room section the riddle_key dict is updated to true, and the inspection number is raised by one.
        -> the visitation order can be tracked, prompting specific riddles depending on the last visited section
        """
        self.inspection_number =+ 1
        self.riddle_keys[room_section] = [True, self.inspection_number]
        print(self.room_section_description[room_section])
        pass

    def botanist_riddle(self, room_section):
        """
        """
        print(f"After inspecting the {room_section}, you return to the old botanist\n")
        print(self.botanist_response[room_section])
        pass
    
    def botanist_request_answer(self):
        print("Do you know the answer?")
        player_y_n = input("Type 'yes' or 'no': ").lower()
        if player_y_n == "yes":
            print("Alright! im glad you've got something!")
            player_answer = input("What is your answer?: ").lower()
            if player_answer == "machete":
                print("Amazing! You solved the riddle. Take this")
                print("\nadd hand machete process here\n")
            else:
                print(f"Sadly {player_answer} isn't the right answer.")
                print("But I'll give you a hint! The answer is the same for all riddles!")
        else:
            print("I'll give you a clue...\nThe answer is the same for all riddles!")
        pass

    def run_story(self, user_items):
        print("You enter an overgrown but spacious room with a massive skylight.\nThere are towering monsteras, vines and vibrant flowers all around you.\nThe air is thick and humid, and there's an eerie sense of calm.\nAn old man with small circular glasses sits on a bench, inspecting a flower.")
        choice = input("Type 'approach' to talk to the botanist.\nType 'leave' to do nothing\nWhat do you want to do?: ")
        if choice == "approach":
            self.botanist()
            while True:
                self.current_riddle()
                next_section = self.inspect_room()
                self.next_riddle(next_section)
                self.botanist_riddle(next_section)
                self.botanist_request_answer()
        elif choice == "leave":
            print("leaving, but not immediately") # NOT FINISHED!!!!
        else:
            print("Invalid input")
        return

## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
jungle_greenhouse = JungleGreenhouse("greenhouse", "Of course there's a greenhouse! The architects really took advantage of the space behind the ZDD building")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "jungle_greenhouse": jungle_greenhouse
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
