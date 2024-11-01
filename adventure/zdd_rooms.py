"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
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
    
class GSITRoom(Room):

    def __init__(self, name, description, items=None):
        super().__init__(name, description, items)
        self.completed_arcade = False

    def run_story(self, user_items):
        self.introduction()
        self.basecamp()

    def introduction(self):
        """Starts story arc of the GSIT-Room"""

        print("You find yourself marching through the long corridor, hearing nothing but your footsteps...")
        for i in range(3):
            time.sleep(1)
            print("...Tap tap...")
        time.sleep(2)
        print("...hmmhmmmm...")
        time.sleep(1)
        print("\nWhat was that??\n")
        time.sleep(3)
        for i in range(3):
            time.sleep(0.5)
            print("...Tap tap...")
        time.sleep(2)
        print("Finally you find yourself in front of a door and enter the gsit room...\n")
        time.sleep(3)
        print("You spot an arcade game and a person reading 'Being and Nothingness' \nby Jean-Paul Sartre in a chair by the window.\n")
        time.sleep(3)
    
    def basecamp(self):
        """The 'lobby' of the GSIT-Room"""

        request = "Would you like to...\n>> talk to the person [t]\n>> approach the arcade[a]\n>> escape the room [e]\n\n>>"
        choice = self.handle_input(request=request, allowed_inputs=['t', 'a', 'e'])
        if choice == 't':
            return self.initial_conversation()
        elif choice == 'a':
            return self.arcade()
        return self.try_escape()
    
    def arcade(self) -> Item:
        pass

    def try_escape(self) -> str:
        pass

    def initial_conversation(self):
        player_name = input("\n'Hello, my dear adventurer! Welcome to the GSIT room! May I know your name, brave soul?'\n>>")
        print(f"\n'Hmmmhmm...I once knew someone named {player_name}. Unfortunately, that poor soul never made it out of here.'")
        time.sleep(3)
        print("'In order to continue your quest, you have to prove to me both your wisdom and your technical knowledge...'")
        time.sleep(3)
        print("'I challenge you to win the arcade game and prove yourself worthy!'")

        request = "'Do you have the courage to accept the challenge and prove your worth? [y/n]\n>>"
        choice = self.handle_input(request=request, allowed_inputs=['y','n'])
        if choice == 'y':
            print("\n'Let the games begin!'")
            return self.arcade()
        print("\n'Too bad! Maybe you need some time to think about it again...'\n")
        return self.basecamp()


    def handle_input(self, request: str, allowed_inputs: list) -> str:
        """
        Handles user input and ensures it is within the allowed inputs.

        Parameters
        ----------
        request (str): What the user will react to
        allowed_inputs (list): A list of valid input options.

        Returns:
        str: A valid input from the allowed inputs.
        """
        
        choice = input(request)
        while choice not in allowed_inputs:
            print(f"Invalid input '{str(choice)}'. Please try again!" )
            choice = input(request)
        return choice

## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
apple_watch=Item("Apple Watch", "A useful device to detect falls", movable=True)
gsit_room = GSITRoom("GSIT Room", "The Morals of Hell")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "gsit": gsit_room
}
