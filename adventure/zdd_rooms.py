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
    
class LaboratoryOfLostCodes(Room):
    """A mysterious laboratory filled with old equipment, dusty computers, and hidden secrets."""

    def __init__(self, items=None):
        super().__init__(
            name="Laboratory of Lost Codes",
            description="The room is dimly lit, filled with old equipment and dusty computers. "
                        "The air feels charged with untapped potential. "
                        "Some corners seem too dark to explore without additional light.",
            
        )
        self.computers_examined = 0
        self.devices_activated = 0
        self.wires_connected = 0
        self.hidden_UML_found = False

    def run_story(self, user_items):
        """Custom logic for the Laboratory of Lost Codes."""
        print("You hear the faint hum of ancient machines powering up.")
        print("Around you are several dusty computers, strange devices, and tangled wires.")
        print("Some corners of the room are shrouded in darkness.")

        while True:
            options = ["'examine computers'", "'turn on device'", "'connect wires'", "'inspect'", "'leave'"]

            print(f">> {', '.join(options)}")
            action = input("What would you like to do? ").lower()

            if action == "examine computers":
                self.examine_computers()
            elif action == "turn on device":
                self.activate_device()
            elif action == "connect wires":
                self.connect_wires()
            elif action == "inspect":
                print(self.get_detail())
            elif action == "leave":
                print("You leave the Laboratory of Lost Codes...")
                break
            else:
                print("Invalid command! Try again.")

        return user_items

    def examine_computers(self):
        """Logic for examining computers."""
        self.computers_examined += 1
        if self.computers_examined == 1:
            print("You dust off the screen and find an old piece of code: 'while(True): explore()'.")
        elif self.computers_examined == 2:
            print("A cryptic message appears: 'The answers lie in the Simulator'.")
        else:
            print("Most of the computers seem broken. Nothing new to find.")

    def activate_device(self):
        """Logic for turning on devices."""
        self.devices_activated += 1
        if self.devices_activated == 1:
            print("You hear a faint whirring sound. A hidden message appears on a screen: 'Connection Required'.")
        elif self.devices_activated == 2:
            print("The device lights up, and a compartment opens to reveal an old key.")
        else:
            print("No more devices respond to your attempts to activate them.")

    def connect_wires(self):
        """Logic for connecting wires."""
        self.wires_connected += 1
        if self.wires_connected == 1:
            print("A loud click echoes as a hidden machine powers on.")
        elif self.wires_connected == 2:
            print("The room trembles slightly, and a secret compartment opens, revealing a strange artifact.")
        else:
            print("The wires are too tangled to do anything further.")

    def get_detail(self):
        """Provide detailed information about the Laboratory."""
        return super().get_detail() + " The room feels alive with secrets waiting to be discovered."

## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

laboratory_of_lost_codes = LaboratoryOfLostCodes()


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "laboratory_of_lost_codes": laboratory_of_lost_codes
}
