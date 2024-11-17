"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
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
    
class CrocodileCage(Room):
    def run_story(self, user_items):
        self.items = user_items
        print("You see a crocodile cage. The crocodile is sleeping. Do you want to wake it up and feed him?")
        input_1 = input("Yes or No? ").strip().lower()
        
        if input_1 == "yes":
            print("You wake up the crocodile and feed him. He is happy.")
        else:
            print("Instead of waking up the crocodile, you decide to sneak near him and pet him. He wakes up and is angry.")
        
        print("The crocodile invites you to a round of Croco Doc. Will you accept the invitation?")
        input_2 = input("Yes or No? ").strip().lower()
        
        if input_2 == "yes":
            game = self.croco_doc()  
            if game == True:  
                print("You win the game and the crocodile is happy.")
                crocodile_fang = Item("Crocodile Fang", "Your trophy for winning against the Crocodile", movable=True)
                user_items.append(crocodile_fang)
                print("You picked up the Item 'Crocodile Fang'.")
            else:
                print("Now the crocodile is very angry. You should leave the room.")
                return True
        else:
            print("You refuse the invitation and the crocodile is sad. He wants you to leave him alone.")
            return True
        
    def croco_doc(self):
        print("Welcome to the Croc Doc game!")
        print("Press the crocodile's teeth, but be careful not to make it snap!")

        #The Game
        teeth = list(range(1, 11)) #all teeth
        bad_tooth = random.choice(teeth) #the bad tooth
        won = False  #Variable to track if the player has won

        while True:
            try:
                #Player chooses a tooth
                choice = int(input("Choose a tooth (1-10): "))

                #Check if its the "bad" tooth
                if choice == bad_tooth:
                    print("Oh no! The crocodile snaps! You lost.")     #loose
                    won = False
                    break
                else:
                    print(f"You pressed tooth {choice}. You're safe!") #win 
                    
                    #Remove the chosen tooth from the list
                    teeth.remove(choice)

                    #If no teeth are left
                    if len(teeth) == 1:
                        print("Congratulations! You safely pressed all the teeth.")
                        won = True  # Player has won
                        break
                    else:
                        continue   #contunue the game
            
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 10.")
                

        #If the player won, they receive a crocodile fang
        return won

## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
crocodile_cage = CrocodileCage("crocodile_cage", "Only wake up the sleeping crocodile, if you are ready to play.")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "crocodile_cage": crocodile_cage
}
