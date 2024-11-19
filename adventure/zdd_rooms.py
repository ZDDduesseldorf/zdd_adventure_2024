"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
import random
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


class Rooftopbar(Room):
    """
    Represents a rooftop bar where the player can mix drinks, admire the stars, and interact with the bartender.
    """
    def __init__(self, name, description, items):
        super().__init__(name, description, items)
        self.telescope =  Item("telescope", "A high-tech telescope that brings the stars closer than ever. Perfect for stargazing!", movable=True)    
        self.bar_visited_ever = False

    def run_story(self, user_items):  
        """
        Provides an initial description of the bar, varying depending on whether the player has visited before.
        """
        if self.visited == 1: 
            print("You step out onto the rooftop and are greeted by the cool evening breeze. It looks like nobody is here...")
            time.sleep(3)
            print("But then you see some glowing lights behind some tall and thick bushes. As you come closer you hear voices and... is that music?")
            print("You step through the bushes.\nFairy lights are strung across the railings, casting a warm glow on the ˚. ✦.ZDD ROOFTOP BAR!˳·˖✶")
            print("A bit astonished you look around:")
            print("To your left, a bar counter is stocked with colorful bottles of all shapes and sizes.")
            print("To your right, lounge chairs and cozy sofas are arranged around fire pits, perfect for a quiet evening of stargazing.")
        else:  
            print("You step out onto the rooftop again. The cool evening breeze feels familiar, and the sound of soft music welcomes you back.")
            print("Fairy lights twinkle as always, and the bar is lively with chatter and laughter.")

        return self.main_menu(user_items)
 
    def main_menu(self, user_items):
        """
        Displays a menu for the player to choose between going to the bar, stargazing, or other options.
        """
        while True:
            print("Type 'bar' to go to the bar, 'stargaze' to admire the sky, or 'other' for some other options.")

            choice = input("What would you like to do? ").lower()
            if choice == "bar":
                return self.mix_drink(user_items)
            elif choice == "stargaze":
                return self.admire_ascii_art(user_items)
            elif choice == "other":
                return user_items
            else:
                print("Invalid choice! Please try again.")
       
    def mix_drink(self, user_items):
        """
        Allows the player to mix a drink, 
        with different dialogues based on whether it's their first visit or if they have the telescope.
        """
        if not self.bar_visited_ever:
            print("You approach the bar for the first time, marveling at the colorful bottles and warm ambiance.")
            print("The bartender greets you with a cheerful smile: 'Welcome to the ZDD Rooftop Bar! Ready to mix a masterpiece? He challenges you'")      
            self.bar_visited_ever = True
        elif self.telescope in user_items:
            print("The bartender recognizes you and gives a friendly wave. 'Back for more fun? The telescope suits you well!'")
            print("This time, you can just relax and enjoy a drink.")
            return self.enjoy_drink(user_items)
        else:
            print("You return to the bar, and the bartender gives a knowing nod. 'Ah, trying your hand at mixing again? Let's see what you've got!'")

    # drink mixing
        while True:
            print("Choose three ingredients for your cocktail:")

            ingredients = ["lemon", "vodka", "mint", "rum", "sugar", "strawberry", "orange juice", "coconut milk", "tequila"]
            print(", ".join([f"{ingredient}" for i, ingredient in enumerate(ingredients)]))

            selected = []
            for i in range(3):
                choice = input(f"Type your ingredient {i+1}: ").lower()
                if choice not in ingredients:
                    print(f"'{choice}' is not a valid ingredient. Please choose from the list.")
                    continue
                selected.append(choice)

            if len(selected) < 3:
                continue 

            print(f"You mix {selected[0]}, {selected[1]}, and {selected[2]}...")

            # check if drink is masterpiece
            hard_liquor = {"vodka", "rum", "tequila"}
            if len(hard_liquor.intersection(selected)) == 3:  
                print("The bartender takes a sip and gasps in delight: 'This is a MASTERPIECE!'")
                print("As a reward, the bartender hands you a shiny telescope!")
                user_items.append(self.telescope)
                print(("You thank him, look at the telescope and know exactly what to do."))
                time.sleep(5)
                return self.main_menu(user_items)
            else:
                print("The bartender shrugs: 'It's... okay. You should try again when you think strong enough!'")
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry != "yes":
                    print("You decline and return to your other options.")
                    return self.main_menu(user_items)

    def enjoy_drink(self, user_items):
        """
        Lets the player enjoy a drink if they already have the telescope.
        """
        available_drinks = ["espresso martini", "mojito", "margarita", "cosmopolitan", "old fashioned"]
        print("The bartender offers you a menu of drinks:")
        print(", ".join(available_drinks))

        while True:
            choice = input("Type the name of the drink you want to enjoy: ").lower()
            if choice in available_drinks:
                print(f"You sip on your {choice}, enjoying the atmosphere and chatting with others at the bar.")
                retry = input("Do you want another drink? (yes/no): ").lower()
                if retry != "yes":
                    print("You step away from the bar, feeling refreshed.")
                    return self.main_menu(user_items)
            else:
                print("That drink isn't on the menu. Please choose a valid option.")
   
    
    def admire_ascii_art(self, user_items):
        """
        Displays ASCII art of the stars, with a more detailed version if the player owns the telescope.
        """
        ascii_art = [" °•.°• ✯★*°°.•°★• ☄☆", "  .  *  *   . *       *"]
        ascii_art_telescope = [
            r"""
             .     .       .  .   . .   .   . .    +  .
               .     .  :     .    .. :. .___---------___.  
                    .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
                 .  :       .  .  .:../:            . .^  :.:\.
                     .   . :: +. :.:/: .   .    .        . . .:\
              .  :    .     . _ :::/:               .  ^ .  . .:\
               .. . .   . - : :.:./.                        .  .:\
               .      .     . :..|:                    .  .  ^. .:|
                 .       . : : ..||        .                . . !:|
               .     . . . ::. ::\(                           . :)/  
              .   .     : . : .:.|. ######              .#######::|
               :.. .  :-  : .:  ::|.#######           ..########:|
              .  .  .  ..  .  .. :\ ########          :######## :/
               .        .+ :: : -.:\ ########       . ########.:/
                 .  .+   . . . . :.:\. #######       #######..:/
                   :: . . . . ::.:..:.\           .   .   ..:/
                .   .   .  .. :  -::::.\.       | |     . .:/
                   .  :  .  .  .-:.:.::.\             ..:/
              .      -.   . . . .: .:::.:.\.           .:/
             .   .   .  :      : ....::_:..:\   ____.  :/
                .   .  .   .:. .. .  .: :.:.:\       :/
                 +   .   .   : . ::. :.:. .:.|\  .:/|
                 .         +   .  .  ...:: ..|  --.:|
        """,
            r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠣⣔⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠞⠁⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⡰⠋⠀⠀⠀⠀⠀⣿⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠄⢀⣀⣠⠤⠄⠤⣤⠰⠆⠓⠁⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣇⡁⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⡅⡀⠀⠀⠀⠀⠀⠀⢠⣔⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣖⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣷⠅⠀⠀⠀⠀⠀⣰⣿⣟⡟⠀⠀⠀⣠⣤⣄⠀⠀⠀⠀⠘⠯⣆⢄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡿⠀⠀⠀⠀⢠⣿⡟⡼⠁⠀⠀⣰⣿⡟⡟⠀⠀⠀⠀⠀⠀⠈⠑⠮⣔⡠⢀⠀⠀⠀
⠀⠀⠀⢸⡟⠀⠀⠀⠀⣼⣿⣱⠁⠀⠀⢰⣿⡿⣹⠁⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠉⠓⢦⣆⡀
⠀⠀⠀⠸⡁⠀⠀⠀⠀⠹⠿⠁⠀⠀⠀⣾⣿⢷⠇⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⠶⣀⠆⣆⣾⢰
⠀⠀⠀⠯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⠞⠀⠀⠀⠀⠀⢀⠈⡈⡄⢥⣘⣴⡶⢾⠺⠑⠁
⠀⠀⣸⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣀⢦⣴⡽⡛⠏⠃⠈⠀⠀⠀⠀
⠀⢰⡎⠔⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡄⣱⡼⠋⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣝⠠⡁⠤⡂⠴⡐⡠⢀⠀⡀⠀⠀⠀⠀⠀⠀⡀⢐⢰⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠡⠞⠚⠲⠣⠭⠍⠁⠣⠗⡜⡢⢄⠀⡂⡡⢄⠌⡥⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⢆⠺⡐⡑⠎⠮⡱⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢴⣁⢎⢒⡡⣹⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢈⡊⡔⣻⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢵⡧⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """,
            r"""
          .          .
       .          .
         /\_/\
        ( o.o )    
         > ^ <
        """,
        r"""
⠀⠀⢀⣀⡀⠘⢀⣀⠀⣀⠀⠀⠀⠀⣠⡀
⠠⡪⠁⠄⢀⠟⠁⠀⠀⠀⠈⠢⠀⠀⠙⠁
⠀⠑⠄⡑⢌⡀⠀⠀⠀⠀⠀⠀⡗⠠⡀⠀
⠀⠀⠀⠈⠒⡬⢐⠢⠄⣀⠀⢠⠃⠱⡈⠢
⠀⠀⠀⠀⠀⠈⠒⠨⠥⠶⠆⠩⠭⠥⠤⠐
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢰⡧⠀⠀⠀⠀
        """,
        ]
        print("You take a seat at one of the cozy sofas. The warm flame of the fire pit infront welcomes you.")
        while True:
            print("Type 'gaze' to admire the stars, 'back' to return to your choices at the rooftop bar.")
            
            action = input("What would you like to do? ").lower()
            if action == "back":
                print("You stand up and take a few steps back to look at your options.")
                return self.main_menu(user_items)
            elif action == "gaze":
                if self.telescope in user_items:
                    print("It's time to admire the nightsky. Using your telescope, you notice the stars forming intricate patterns:")
                    for i in range(2):
                        print(ascii_art_telescope[random.randint(0,3)])
                        time.sleep(2)
                else:
                    print("You admire the beautiful ASCII art in the sky:")
                    for art in ascii_art:
                        print(art)
                        time.sleep(2)
 
            print("It's a truly relaxing experience.")

## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
rooftop = Rooftopbar("rooftop", "It's kinda chilly out here.", None)


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    'rooftop': rooftop
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
