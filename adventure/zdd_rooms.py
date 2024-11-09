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

## ----------------------------------------------------------------
## List here all rooms

class DarkRoom(Room):
    def run_story(self, user_items):
        print("The room is pitch dark. You can barely see anything.")
        if "flashlight" in [x.name for x in user_items]:
            print("You use the flashlight to light up the room and see an old painting on the wall.")
        else:
            print("You stumble around in the dark and decide it might be wise to come back with a light source.")
        return user_items

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
dark_room = DarkRoom("dark room", "A room shrouded in complete darkness.")  # New room instance

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "dark_room": dark_room
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
