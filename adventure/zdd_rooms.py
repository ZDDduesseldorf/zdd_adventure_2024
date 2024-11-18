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
    
class LaboratoryOfLostCodes(Room):
    """A mysterious laboratory filled with old equipment, dusty computers, and hidden secrets."""

    def __init__(self, items=None):
        super().__init__(
            name="Laboratory of Lost Codes",
            description="The room is dimly lit, filled with old equipment and dusty computers. "
                        "The air feels charged with untapped potential. "
                        "Some corners seem too dark to explore without additional light.",
            items=items or [Flashlight()]
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
            if any(isinstance(item, Flashlight) for item in user_items):
                options.insert(-1, "'use flashlight'")
            if any(isinstance(item, Flashlight) for item in self.items):
                options.insert(-1, "'take flashlight'")

            print(f">> {', '.join(options)}")
            action = input("What would you like to do? ").lower()

            if action == "examine computers":
                self.examine_computers()
            elif action == "turn on device":
                self.activate_device()
            elif action == "connect wires":
                self.connect_wires()
            elif action == "use flashlight" and any(isinstance(item, Flashlight) for item in user_items):
                self.use_flashlight(user_items)
            elif action == "take flashlight" and any(isinstance(item, Flashlight) for item in self.items):
                self.take_flashlight(user_items)
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
    
    def take_flashlight(self, user_items):
        """Logic to take the flashlight from the room."""
        flashlight = next((item for item in self.items if isinstance(item, Flashlight)), None)
        if flashlight:
            self.items.remove(flashlight)
            user_items.append(flashlight)
            print("You take the flashlight and place it in your inventory.")
        else:
            print("There's no flashlight here to take.")

    def use_flashlight(self, user_items):
        """Use the flashlight to reveal hidden details."""
        flashlight = next((item for item in user_items if isinstance(item, Flashlight)), None)
        if not flashlight:
            print("You don't have a flashlight to use.")
            return
        if not flashlight.use():
            print("The flashlight battery is dead. You'll need to recharge it to use it again.")
            return

        if not self.hidden_UML_found:
            self.hidden_UML_found = True
            print("The beam of the flashlight cuts through the gloom, revealing a hidden drawer beneath a desk. Inside, you uncover a strange UML diagram of a Particle Life Simulator.")
        else:
            print("The flashlight illuminates the room, but you don't find anything new.")
    
class Flashlight(Item):
    """Represents a flashlight with additional functionality for a game."""
    def __init__(self, name="Old Flashlight", description="A dusty flashlight that might reveal hidden secrets.", movable=True, battery_level=100):
        """
        Constructs a new Flashlight item.

        Parameters
        ----------
        name : str
            Name of the flashlight item.
        description : str
            Description of the flashlight.
        movable : bool
            Determines whether the flashlight can be added to the inventory.
            Defaults to True.
        battery_level : int
            Initial battery level of the flashlight. Defaults to 100.
        """
        super().__init__(name, description, movable)
        self.battery_level = battery_level  # Battery level starts at 100

    def use(self):
        """Use the flashlight, draining battery and revealing hidden details."""
        if self.battery_level <= 0:
            print("The flashlight is out of battery and won't turn on.")
            return False
        self.battery_level -= 10  # Reduce battery level by 10 per use
        print("You turn on the flashlight. The beam illuminates the surroundings.")
        if self.battery_level <= 0:
            print("The flashlight dims and the battery runs out.")
        return True

    def recharge(self):
        """Recharge the flashlight's battery to full."""
        self.battery_level = 100
        print("The flashlight's battery is fully recharged.")

    def get_status(self):
        """Check the current battery level of the flashlight."""
        print(f"The flashlight's battery is at {self.battery_level}%.")

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
