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
        print("You find yourself marching through the long corridor, hearing nothing but your footsteps...")
        for i in range(3):
            time.sleep(1)
            print("...Tap tap...")
        time.sleep(2)
        print("...hmmhmmmm...")
        time.sleep(1)
        print("\nWhat was that??\n")
        time.sleep(3)
        print("A shiver runs down your spine and you start walking faster, the quiet, distant humming still in your ears")
        time.sleep(3)
        for i in range(3):
            time.sleep(0.5)
            print("...Tap tap...")
        time.sleep(2)
        print("\nFinally, at the end of your way the is a double door. You take one last look at the hallway, but you see nothing and no one")
        time.sleep(5)
        print("You pull yourself together and enter the gsit room...")
        time.sleep(3)
    
    def basecamp(self):
            print("You look around the room and spot an arcade game and \na person reading 'Being and Nothingness' by Jean-Paul Sartre in a chair by the window.")
            time.sleep(1)
            choice=input("Would you like to...\n>> talk to the person [t]\n>> approach the arcade[a]\n>> escape the room [e]\n\n>>")
            while choice not in ['t', 'a', 'e']:
                print(f"Invalid input '{choice}." )
                choice=input("You can...\n>> talk to the person [t]\n>> approach the arcade [a]\n>> lescape the room [e]\n>>")
            if choice == 't':
                return self.start_conversation()
            elif choice == 'a':
                return self.arcade()
            else:
                return self.decline_escape()


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
