import zdd_rooms


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        return f"{self.name}: {self.description}"

# Die Library-Klasse, die von Room erbt:
class Library(Room):
    def __init__(self):
        super().__init__(
            name="Enchanted Library",
            description=(
                "You step into the Enchanted Library. The smell of old parchment and magic fills the air. "
                "Between the glowing books, you spot some letters tucked away."
            )
        )
        self.letters = [
            {"content": "The key lies within the oak tree.", "taken": False},
            {"content": "Beware of the shadow in the north.", "taken": False},
        ]

    def interact(self, action):
        if action == "read letters":
            readable_letters = [
                letter["content"]
                for letter in self.letters
                if not letter["taken"]
            ]
            if readable_letters:
                return "\n".join(readable_letters)
            else:
                return "All the letters have been read."
        elif action == "take letters":
            for letter in self.letters:
                letter["taken"] = True
            return "You have taken all the letters."
        else:
            return "You can 'read letters' or 'take letters'. Please choose one."

# Jetzt die Testszenarien für die Library-Klasse

def test_library():
    # Erstelle eine Instanz der Library
    library = Library()

    # Beschreibe die Bibliothek
    print("Library Description:")
    print(library.describe())

    # Versuche, die Briefe zu lesen
    print("\nReading letters:")
    print(library.interact("read letters"))

    # Versuche, die Briefe zu nehmen
    print("\nTaking letters:")
    print(library.interact("take letters"))

    # Versuche erneut, die Briefe zu lesen, nachdem sie genommen wurden
    print("\nTrying to read letters again:")
    print(library.interact("read letters"))

    # Versuche erneut, die Briefe zu nehmen, die bereits genommen wurden
    print("\nTrying to take letters again:")
    print(library.interact("take letters"))

# Führe den Test aus
test_library()
