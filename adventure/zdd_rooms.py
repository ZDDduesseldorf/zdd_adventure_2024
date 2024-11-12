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

## ----------------------------------------------------------------
## List here all rooms
class StudyRoom(Room):
    def run_story(self, user_items):
        print("You enter the study room filled with books and an old chalkboard.")
        print("A puzzle is scribbled on the board: What has keys but can't open locks?")
        answer = input("What is your answer?: ").lower()
        if answer == "piano":
            print("Correct! A hidden compartment opens and reveals an old map.")
            map_item = Item("old map", "An old map that hints at secret pathways in the ZDD.", movable=True)
            if map_item not in user_items:
                user_items.append(map_item)
                print("You've taken the old map.")
        else:
            print("That's not correct. The room remains quiet.")
        return user_items
    
study_room = StudyRoom("study room", "A quiet room with shelves of books and an old chalkboard.")
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "study_room": study_room
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
