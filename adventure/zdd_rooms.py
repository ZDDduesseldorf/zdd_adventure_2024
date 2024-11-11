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
    
    
class Pigsty(Room):
    def __init__(self, name, description):
        self.brother_saved = False
        super().__init__(name, description)
        
    def show_items(self, user_items):
        if not self.brother_saved:
            print("There is nothing of particular interest...")
            return user_items
        return super().show_items(user_items)

        
    def run_story(self, user_items):
        from pigsty_dialogue import pig_dialogue, dialogue_options, additonal_dialogue
        inp_lst = []
        print("Stumbling into the pigsty, the world suddenly feels smaller.\nYou try to look at your hands but they have become pig feet.\nYou now have become a pig.")
        print("But you understand that there is some kind of magic going on. You cant't leave now. Not as a pig.")
        print("You feel a sharp pain in your stomach. You are starving.\nYou look around the pigsty and see another pig.")
        print("A memory as light as a feather suddenly appears in the back of your mind. That is your pig brother\nYou must stop him from eating the oates that the humans gave him.")
        print("He worships the humans as tall skinny gods. But you know better.\nYou know they only want to fatten him up for the butcher.")
        print("You can only leave the room with the oats. If you have them, he will not eat them.")
        print("Slowly you begin walking towards him...\n'YOU: Brother, may i have some oats?'")
        for i in range(5):
            print("HIM:",pig_dialogue[i])
            for idx,j in enumerate(dialogue_options[i]):
                print(f"    {idx}.: {j}")
            while True:
                try:
                    inp = int(input(">: "))
                    if inp < 0 or inp > len(dialogue_options[i]):
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid number.")
            inp_lst.append(inp)
            print("YOU:", dialogue_options[i][int(inp)], additonal_dialogue[i])
        if inp_lst == [1, 1, 3, 1, 2]:
            print("HIM: Hmm. I can now see that you were trying to save me. For now I will spare you some oats, brother. As you have shared them with me from time to time.")
            print("You have finally stopped him from eating the oats. You have saved your pig brother...")
            self.brother_saved = True
        else:
            print("Still in dibelieve you hear your brother eating away at the oats. You have failed to save your pig brother.")
        print("You feel your fingers and feet tingling as you turn back to human and leave the room.")
        return user_items
    
## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
oats = Item("oats", "some oats")
pigsty = Pigsty("pigsty", "Why does the ZDD have a pigsty???")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "pigsty" : pigsty
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
