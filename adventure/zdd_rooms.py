"""This is to keep all special rooms of the ZDD."""
from main_classes import Room
from main_classes import Item 

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

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
class Cafeteria(Room):
    def check_items(self, items, text, user_items):
        # Überprüft, ob eines der Items in der Liste items in user_items vorhanden ist
        for item in items:
            if item in [x.name for x in user_items]:
                print(text)
                user_items = [x for x in user_items if x.name != item]  # Entfernt nur das erste gefundene Zertifikat
                return user_items  # Rückgabe nach dem ersten Treffer
        return user_items

    def pay_with_item(self, user_items):
        # Filtert nach Items, die nicht "Workout Certificate" oder "Cardio Certificate" sind
        non_certificate_items = [x for x in user_items if x.name not in ["Workout Certificate", "Cardio Certificate"]]
        
        if non_certificate_items:
            # Entferne das erste nicht-Zertifikat-Item als Zahlung
            item_to_pay = non_certificate_items[0]
            print(f"You used {item_to_pay.name} to pay.")
            user_items.remove(item_to_pay)
            return True  # Zahlung erfolgreich
        else:
            print("It seems like you don't have anything to pay with.")
            return False  # Keine Zahlungsmittel
        
    def pay_with_item_coin(self, user_items):
        # Filtert nach Items, die nicht "Workout Certificate" oder "Cardio Certificate" sind
        non_certificate_items = [x for x in user_items if x.name in ["old coin"]]
        
        if non_certificate_items:
            # Entferne das erste nicht-Zertifikat-Item als Zahlung
            item_to_pay = non_certificate_items[0]
            print(f"You used {item_to_pay.name} to pay.")
            user_items.remove(item_to_pay)
            return True  # Zahlung erfolgreich
        else:
            print("It seems like you don't have anything to pay with.")
            return False  # Keine Zahlungsmittel


    def run_story(self, user_items):
        
        # Überprüfen, ob "Workout Certificate" oder "Cardio Certificate" in user_items vorhanden ist
        user_items = self.check_items(
            ["Workout Certificate", "Cardio Certificate"],
            "You have a certificate! You can pick something for free.",
            user_items
        )
        
        while True:
            print("It seems like someone is hungry, buying will cost you! or how could I help you?")
            action = input("Would you like to buy a 'drink', 'eat', try the 'old snack vending machine' or 'inspect' to look around? ").strip().lower()
            
            if action == "drink":
                
                print("What would you like to drink?")
                action = input("We have 'coffee', 'juice', 'water', and 'smoothie': ").strip().lower()
                if action == "coffee":
                    drink_description = "coffee"
                elif action == "juice":
                    drink_description = "juice"
                elif action == "water":
                    drink_description = "water"
                elif action == "smoothie":
                    drink_description = "smoothie"
                else:
                    print("I'm not sure what that is; I assume we don't sell it here.")
                    continue
                
                # Bezahlung prüfen
                if self.pay_with_item(user_items):
                    drink = Item(name= drink_description, description= "drink bought from the cafeteria")
                    user_items.append(drink)
                    print(f"You have selected a {drink_description}.")
                else:
                    print("You couldn't pay for the drink.")

            elif action == "eat":
                food_description = ""
                print("What would you like to eat?")
                action = input("It's not like we're a restaurant, but we have various options: 'sandwiches', 'chips', 'sweets', and 'salads': ").strip().lower()
                if action == "sandwiches":
                    food_description = "sandwiches"
                elif action == "chips":
                    food_description = "chips"
                elif action == "sweets":
                    food_description = "sweets"
                elif action == "salads":
                    food_description = "salads"
                else:
                    print("I'm not sure what that is; I assume we don't sell it here.")
                    continue
                
                # Bezahlung prüfen
                if self.pay_with_item(user_items):
                    food = Item(name= food_description, description= "food bought from the cafeteria")
                    user_items.append(food)
                    print(f"You have selected {food_description}.")
                else:
                    print("You couldn't pay for the food.")

            elif action == "machine":
                machine_description = ""
                print("What snacks do you wanna buy?")
                action = input("'a' for haribo, 'b' for snickers, 'c' chips or 'd' for kinderschokolade: ").strip().lower()
                if action == "a":
                    machine_description = "Haribo"
                elif action == "b":
                    machine_description = "Snickers"
                elif action == "c":
                    machine_description = "Chips"
                elif action == "d":
                    machine_description = "Kinderschokolade"
                else:
                    print("This is not a Supermarket... just an old machine.")
                    continue

                if self.pay_with_item_coin(user_items):
                    snack = Item(name= machine_description, description= "snack bought from the old vending machine")
                    old_coin = Item("old coin", "coin used for the vending machine", movable = True)
                    user_items.append(snack)
                    print(f"You have selected {machine_description}.")
                else:
                    print("You couldn't pay for the food.")

            elif action == "inspect":
                print("Oh, seems like you found an 'old coin'! Lucky you! How will this be usefull...?")
                old_coin = Item("old coin", "coin used for the vending machine", movable = True)
                user_items.append(old_coin)
                continue

            elif action == 'leave':
                break
                
            else:
                print("Seems like I can't help you. Or can I?")
                continue

            

cafeteria_room = Cafeteria("cafeteria", "a place you visit when you are hungry")



ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "cafeteria_room" : cafeteria_room
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
