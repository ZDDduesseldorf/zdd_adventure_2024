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

class ArchiveOfForgottenPlans(Room):
    """
    Contains all the possible actions that can be done in the room.
    The actions are search dusty shelves, analyze old maps, turn on the projector or leave the room
    """
    def run_story(self, user_items):
        print("A room filled with faded documents and worn architectural plans.")

        while True:
            print()
            choice = input ("What do you want to investigate? A: search dusty shelves, B: analyze old maps, C: turn on projector, D: leave" )

            if choice == "A":
                self.search_dusty_shelves(user_items)

            elif choice == "B":
                self.analyze_old_maps()
                

            elif choice == "C":
                self.turn_projector_on()

            elif choice == "D":
                break

            else:
                print("Wrong input, please choose again!")
        return user_items
    
    """
    All the different methods for the actions in the room.
    search_dusty_shelves -> if you don't have the blueprint fragment in your inventory you will find it here. If you have it in your inventory
                            it says that you can't find anything else
    analyze_old_maps -> prints a riddle the users "finds" on old maps, the riddle gives the answer to the password of the projector
    turn_projector_on -> Asks the answer/password found in the old maps, if the password is correct the projector turns on and shows a picture of
                            the blueprints of the ZDD. Else it tells you to find the password somewhere.
    """
    
    def search_dusty_shelves(self, user_items):
        if "blueprint fragment" in [x.name for x in user_items]:
            print("We have already searched here. There seems to be only dust left.")
        else:
            print("You find a fragment of a blueprint. Maybe it leads somewhere?")
            blueprint_fragment = Item("blueprint fragment", "a fragment of the ZDD blueprints", movable=True)
            user_items.append(blueprint_fragment)
            
        
    def analyze_old_maps(self):
        print("You find maps of the old campus of the HSD. On the back of one of them you find a riddle...")
        print("He’s known for his great lectures—students all agree. His name sounds a bit like ""uber,"" but knowledge is the key. Who is he?")

    def turn_projector_on(self):
        print("It seems the projector is password protected. Do you want to guess?")
        password = input("Your guess:")

        if "Huber" in password:
            print("The projector turns on... and reveals the blueprints of the ZDD on the wall.")
        else:
            print("Thats not correct, maybe you can find it somewhere!")

            
## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")


# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
archive_of_forgotten_plans = ArchiveOfForgottenPlans("Archive of Forgotten Plans", "Room where you can find old and new plans of the university", "blueprint fragment")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "archive_of_forgotten_plans": archive_of_forgotten_plans
}
