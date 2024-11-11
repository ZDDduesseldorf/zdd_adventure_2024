"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item


class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            # Remove book from inventory
            return [x for x in user_items if x.name != "old book"]
        return user_items
    
    
class MireviLab(Room):
    def __init__(self, name, description, items=None):
        super().__init__(name, description, items)
        self.code_found = False
        self.correct_code = "9989"
    
    def run_story(self, user_items):
        print("You enter the Mirevi lab.")
        print("You feeel weirdly light. In the Mirevi Lab the floor is a bit more bouncy.")
        print("Why is that?")
        print("You begin to investigate....")
        
        # Hint about the code
        print("You find a piece of paper with a code on it. It says'10000 - the Building number of the ZDD'.")
        print("You wonder what that means. You decide to keep it.")
        self.code_found = True
        
        print("You find a VR headset on the Table. Its tempting to put it on.")
        action = input("Do you want to put on the VR headset? (yes/no): ").lower()
        if action == "yes":
            print("You put on the VR headset and suddenly find yourself in a virtual world.")
            self.run_virtual_world()
        else:
            print("You decide not to put on the VR headset.")
        return user_items
        
    def run_virtual_world(self):
        print("You find yourself in a virtual world. After looking around you find something that looks like... a door?")
        print("You walk towards it and but it's locked. Nex to it is a Keypad.")
        
        # Check if the user has the code
        if self.code_found:
            attempt = input("You decide to try a code. What code do you want to try?: ")
            if attempt == self.correct_code:
                print("The door Clicks open. You've unlocked it.")
                print("You take off the VR headset and find yourself back in the Mirevi Lab. With the door now open.")
                print("But since when was there a door there? Also, where is the keypad?")
                print("Was it all in your head?")
            else:
                print("Incorrect code: The door remains locked.")
                print("You take off the VR headset and find yourself back in the Mirevi Lab. You decide to investigate once more.")
        else:
            print("You don't have the code to unlock the door. You decide to take off the VR headset.")
            print("You decide to investigate once more.")
        
        
        

## ----------------------------------------------------------------
## List here all rooms

# Define Items
vr_headset = Item("VR headset", "Trying to escape reality with a virtual one might not work this time... or will it?", movable=True)

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
mirevi_lab = MireviLab("mirevi-lab", "You enter the Mirevi lab.", vr_headset)
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")




ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "mirevi_lab": mirevi_lab
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}