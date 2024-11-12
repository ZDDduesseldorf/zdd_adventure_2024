"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item, Item
import random



class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            # Remove book from inventory
            return [x for x in user_items if x.name != "old book"]
        return user_items
    
class MensaTummyAches(Room):
    def __init__(self, name, description, item):
        self.next_room = self
        self.allowed_to_leave = True
        
        super().__init__(name, description, item)
    # TODO: After returning from the Mensa, the leave/ inspect message should be overwritten
        
    def run_story(self, user_items):
        print("What's that sound? You hear a loud rumbling.")
        print("A strong wind starts blowing.")
        print("The wind lifts you off your feet!")
        print("You're swept through a dark tunnel, twisting and turning.")
        print("Finally, the wind subsides, and you find yourself in a bustling hall.")
        print("You open your eyes to see a huge crowd of people queuing for food.")
        print("\nWelcome to the MENSA OF THE TUMMY ACHES!\n")

        print("Your stomach grumbles; you're quite hungry.")
        print("But this place is known for its perils and... interesting cuisine.")

        print("There are three main courses available today:")
        print("1. A hearty meat-containing meal.")
        print("2. A fresh vegetarian dish.")
        print("3. The infamous stew of the day.")

        meal_choice = input("Which meal do you want to choose? (1, 2, or 3): ")

        if meal_choice == "1":
            print("\nYou choose the meat meal and approach the line.")
            print("But the line stretches out into infinity.")
            print("Do you want to:")
            print("a. Wait patiently.")
            print("b. Take a daring shortcut to cut the whole line.")
            meat_choice = self.input_hander(["a", "b"])
            if meat_choice == "a":
                print("\nYou decide to wait. Time seems to slow down.")
                print("Finally, you get your meal and find a seat.")
                print("The meal is satisfying, and you feel content.")
            elif meat_choice == "b":
                print("\nYou spot a narrow path through the cash register.")
                print("Seizing the opportunity, you slip through and cut the entire line!")
                print("People are baffled, but before they can react, you're at the counter.")
                print("Do you want to:")
                print("i. Act natural and order your meal confidently.")
                print("ii. Distract everyone with a spontaneous performance.")
                action_choice = self.input_hander(["i", "ii"])
                
                if action_choice == "i":
                    print("\nYou act as if nothing happened.")
                    print("The chef, impressed by your boldness, serves you generously and hands you a healing mate.")
                    user_items.append(self.items[0])
                    print("You enjoy your meal, feeling a bit mischievous.")
                elif action_choice == "ii":
                    print("\nYou break into a dance, diverting attention.")
                    print("The crowd is entertained, and any resentment fades away.")
                    print("You receive your meal and a round of applause!")
        elif meal_choice == "2":
            print("\nYou opt for the vegetarian dish and join the line.")
            print("The line is reasonable, and you reach the counter quickly.")
            print("You get your meal and find a seat by the window.")
            print("The meal is fresh and revitalizing.")
            print("You feel ready to take on any challenges ahead.")
        elif meal_choice == "3":
            print("\nYou choose the infamous stew of the day.")
            print("The vegan stew has a peculiar aroma.")
            print("Do you want to:")
            print("a. Take a cautious sip.")
            print("b. Dive right in and eat heartily.")
            stew_choice = self.input_hander(["a", "b"])
            if stew_choice == "a":
                print("\nYou take a small sip.")
                print("It's incredibly salty! Your mouth feels like a desert.")
                print("You might be experiencing salt poisoning!")
                
                if "healing mate" in [x.name for x in user_items]:
                    print("Do you want to:")
                    print("i. Drink water quickly.")
                    print("ii. Use the 'Healing Mate' you found.")
                    salt_choice = self.input_hander(["i", "ii"])
                    if salt_choice == "i":
                        print("\nYou gulp down water, but it doesn't help much.")
                        print("Your vision blurs, and you feel faint.")
                        print("You wake up right back at the end of the line, still hungry.")
                        self.allowed_to_leave = False
                        return user_items
                    elif salt_choice == "ii":
                        print("\nYou sip the 'Healing Mate' you find in your bag.")
                        print("The saltiness fades, and you feel much better!")
                        print("Crisis averted, you proceed with your adventure.")
                        user_items = [x for x in user_items if x.name != "healing mate"]
                else:
                    print("\nYou gulp down water, but it doesn't help much.")
                    print("Your vision blurs, and you feel faint.")
                    print("You wake up right back at the end of the line, still hungry.")
                    # user not allowed to leave from here on
                    self.allowed_to_leave = False
                    return user_items
            elif stew_choice == "b":
                print("\nYou dive in and eat heartily.")
                print("The stew tastes great at first, but then the saltiness hits you.")
                print("You realize you've made a great mistake!")
                self.allowed_to_leave = False
                self.next_room = random.choice([instant for room_name, instant in ALL_ROOMS.items() if self.name not in room_name])
                print(f"In dramatic fashion, you faint and wake up in the {self.next_room.name}")
                return user_items
        else:
            print("\nConfused, you wander aimlessly and accidentally step into thickened sauce!")
            print("You're stuck! It's like quicksand.")
            print("Do you want to:")
            print("a. Call for help.")
            print("b. Try to wiggle free.")
            sauce_choice = self.input_hander(["a", "b"])
            if sauce_choice == "a":
                print("\nYou call out for help.")
                print("A kind chef helps you out and offers you a healing mate to freshen up.")
                user_items.append(self.items[0])
                print("Grateful, you accept the healing mate.")
            elif sauce_choice == "b":
                print("\nYou wiggle vigorously.")
                print("You free yourself but slip and slide into a table.")
                print("Embarrassed but unharmed, you decide to proceed cautiously.")
                print("You decide to head back to where you came from.")
                return user_items

        print("\nWith your adventure in the Mensa coming to an end, you decide it's time to head back.")
        
        
        if "healing mate" in [x.name for x in user_items]:
            print("Do you want to:")
            print("1. Follow the exit signs.")
            print("2. Use the 'Healing Mate' to teleport yourself to a random room.")
            final_choice = self.input_hander(["1", "2"])


            if final_choice == "1":
                print("\nYou follow the exit signs, navigating through the crowd.")
                print("After a few twists and turns, you find the exit.")

            elif final_choice == "2":
                print("\nYou take a sip of the 'Healing Mate.'")
                print("A warm sensation washes over you.")
                print("You feel your eyes slowly close.")
                self.next_room = random.choice([instant for room_name, instant in ALL_ROOMS.items() if self.name not in room_name])
                self.allowed_to_leave = False
                print(f"As you open up your eyes, you find yourself in the {self.next_room.name}.")
                user_items = [x for x in user_items if x.name != "healing mate"]
                return user_items
            
                
        print("\nYou follow the exit signs, navigating through the crowd.")
        print("After a few twists and turns, you find the exit.") 
        print("You became the hero you were always meant to be.")
        print("Not the one the Mensa deserves, but the one it needs.")
        print("In a flash, you're back in the cellar, refreshed and satisfied.")
        
        
        
        return user_items
    
    def input_hander(self, choices: list):
        if len(choices) > 2:
            choice_str =  "".join([f"{choice}, " for choice in choices[:-1]]) + f"or {choices[-1]}"
        else:
            choice_str = f"{choices[0]} or {choices[1]}"
        usr_input = input(f"Enter your choice ({choice_str}): ")
        if usr_input in choices:
            self.print_devider()
            return usr_input
        else:
            print("Please enter a valid choice!")
            return self.input_hander(choices)
        
    def print_devider(self):
        print(60 * "-")
## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
mate = Item("healing mate", "A healing mate against salt poisoning.", movable=True)
mensa_tummy_aches = MensaTummyAches("mensa", "The dome of tummy aches", mate)
# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "mensa_tummy_aches": mensa_tummy_aches
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
