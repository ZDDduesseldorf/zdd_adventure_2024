"""This is to keep all special rooms of the ZDD."""
from main_classes import Room


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
            "thick bushes": "What is can be symbol of independence, carried by those who carve their own path?", 
            "skylight": "What glints in the moonlight, a silent guardian by night?",
            "intricate plant pot": "What can be an artist's brush on a canvas of a garden?", 
            "vines": "It cuts through vines without a sound, yet speaks volumes when needed. What is it?",
            "snake statue": "Sharp as a serpent's tooth, yet not venomous. What am I?"  
        }
        self.room_section_description = {
            "thick bushes": "The thick bushes form an almost impenetrable wall of green, their broad leaves glistening with moisture.",     
            "skylight": "The massive skylight above floods the room with natural light, casting shimmering patterns on the leaves below.",
            "intricate plant pot": "A beautifully carved plant pot sits in a corner, its surface covered in swirling, almost hypnotic patterns. Inside, a peculiar plant with spindly stems and tiny, jewel-like flowers grows, as if thriving under someone's careful watch.",
            "vines": "Long, winding vines drape from the ceiling and walls, their tendrils snaking across the floor like ancient guardians.",
            "snake statue": "In the center of the room stands a stone statue of a coiled snake, its eyes made of gleaming emeralds that seem to follow your every move."
        }
        pass

    def two_choices(self, choice_1, choice_2):
        while True:
            player_input = input(f">> Type '{choice_1}' for {choice_1}\n>> Type '{choice_2}' for {choice_2}\n")
            if choice_1 == player_input:
                return True
            elif choice_2 == player_input:
                return False
            else:
                print("Invalid Input! Try again.")
            
    def inspect_room(self):
        print("Thick bushes form dense, rustling walls of green.\nLight streams through a skylight, illuminating the jungle below.\nAn intricate plant pot with carved patterns houses a massive plant.\nVines hang from above, their tendrils snaking across surfaces.\nA snake statue stands in the center, its emerald eyes glinting in the light.")
        print(40 * "-")
        print("You decide to look around.")
        for entry in self.riddles:
            print(f"Type '{entry}' to inspect the {entry}")
        choice = input()
        print()
        if choice in self.riddles:
            print(f"You apprach the {choice}")
        else:
            print("choice not recognized")
        return choice

    def botanist(self):
        """The botanist gives the player riddles they all have the same

        The botanist has 5 riddles with the same result: "machete"

        this should encourage the player to look around the room and look for clues
        depending on which item the player brings back the botanist will give more clues, or a prize
        """
        print(40 * "-")
        opening_prompts = ["Well hello there! It's been a while since anyone came to visit me. I am Dr. Sylas Thorncroft, and perhaps who might you be?\n",
                           "Look who's back already! Came to take another look at things? Remind me of your name please\n"]
        if self.visited == 1:
            self.player_alias = input(opening_prompts[0])
        else:
            self.player_alias = input(opening_prompts[1])
        pass

    def current_riddle(self):
        """depending on which part of the room the player had the most recent interaction with,
        they are prompted with a specific riddle when returning to the botanist
        """
        print(40 * "-")
        introduction_to_riddles = f"Look around the room {self.player_alias}! If you see something interesting come back to me!"

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
        print(f"After inspecting the {room_section}, you return to the old botanist")
        pass
    
    def run_story(self, user_items):
        print("""You enter an overgrown but spacious room with a massive skylight.\nThere are towering monsteras, vines and vibrant flowers all around you.\nThe air is thick and humid, and there's an eerie sense of calm.\nAn old man with small circular glasses sits on a bench, inspecting a flower.""")
        choice = input("Type 'approach' to talk to the botanist.\nType 'leave' to do nothing\n")
        if choice == "approach":
            self.botanist()
            while True:
                self.current_riddle()
                next_section = self.inspect_room()
                self.next_riddle(next_section)
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
