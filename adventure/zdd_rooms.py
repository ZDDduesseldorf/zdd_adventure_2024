"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
import time
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
    
class GSITRoom(Room):

    def __init__(self, name, description, items=None):
        super().__init__(name, description, items)
        self.completed_arcade = False
        self.tried_escape = False
        self.arcade_points = 0
        self.ethical_words = ["Data Protection", "Categorical imperative", "Moral Agent", "Transparancy", 
                              "Fairness", "Inclusivity", "Privacy by Design", "Autonomy", "Honesty", 
                              "User Empowerment", "Respect", "Empathy", "Ethical Alignment", "Data Sovereignty",
                              "Social Responsibility"
                             ]
        self.unethical_words = ["Discrimination by Bias", "Data Exploitation", "Invasion of Privacy", "Exclusion",
                                "Monetization of Personal Data", "Deception", "Predatory Practices", "Loss of Autonomy",
                                "Data Misuse", "Deepfakes", "Cyberbullying", "Privacy Erosion", "Unauthorized Use",
                                "Data Theft", "Forced Consent", "Data Monopoly", "Privacy Trade-Offs",
                                "Unauthorized Tracking", "Privacy Evasion",
                               ]

    def run_story(self, user_items):
        self.introduction()
        self.main_menu()

    def introduction(self):
        """Starts story arc of the GSIT-Room"""

        print("You find yourself marching through the long corridor, hearing nothing but your footsteps...")
        for i in range(3):
            time.sleep(1)
            print("...Tap tap...")
        time.sleep(2)
        print("...hmmhmmmm...")
        time.sleep(1)
        print("\nWhat was that??\n")
        time.sleep(3)
        for i in range(3):
            time.sleep(0.5)
            print("...Tap tap...")
        time.sleep(2)
        print("Finally you find yourself in front of a door and enter the gsit room...\n")
        time.sleep(3)
        print("The room is lit by a dim light, the walls are covered with book shelfs and the floor is covered with a thick carpet.")
        time.sleep(3)
        print("You spot an arcade game and a person reading 'Being and Nothingness' \nby Jean-Paul Sartre in a chair by the fireplace.\n")
        time.sleep(3)
    
    def main_menu(self):
        """The 'lobby' of the GSIT-Room"""

        request = "Would you like to...\n>> talk to the person [t]\n>> approach the arcade [a]\n>> escape the room [e]\n\n>>"
        choice = self.handle_input(request=request, allowed_inputs=['t', 'a', 'e'])
        if choice == 't':
            return self.conversation()
        elif choice == 'a':
            return self.arcade_introduction()
        return self.try_escape()
    
    def arcade_introduction(self):
        print("Welcome to...")
        self.show_arcade_logo()
        time.sleep(2)
        print("Ethical Catch!")
        time.sleep(2)
        print("The game is simple: over the course of the game, words will appear on the screen.")
        print("Your task is to catch 5 ethical words by pressing enter.")
        print("If you see an unethical word, press 'no' to avoid catching it.")
        print("You have 3 seconds to catch each ethical word.")
        print("But be careful! Catching unethical words will cost you points!")
        request="Are you ready to play? [y/n]\n>>"
        choice = self.handle_input(request=request, allowed_inputs=['y','n'])
        if choice == 'n':
            print("'I knew you wouldn't dare to play! You'll be stuck here forever!' the person says...\n")
            return self.main_menu()
        print("\n\n\n\n")
        return self.arcade()
    
    def arcade(self):
        """The arcade game of the GSIT-Room
        
        The player has to catch ethical words to win the game.
        """
        num_ethical_words = random.randint(5,7)
        num_unethical_words = 15 - num_ethical_words
        ethical_words_used = random.sample(self.ethical_words, num_ethical_words)
        unethical_words_used = random.sample(self.unethical_words, num_unethical_words)
        words_to_display = ethical_words_used + unethical_words_used
        random.shuffle(words_to_display)
        print("The game starts in ...")
        for nmbr in range(3,0,-1):
            print(f"{nmbr}...")
            time.sleep(1)
        for word in words_to_display:
            if self.arcade_points >= 5:
                print("Congratulations! You have shown yourself to be a real philosopher!")
                self.completed_arcade = True
                break
            time.sleep(random.randint(5,8))
            print(f"\nWord: {word}\n")
            explain = "Press enter to catch the word!\n"
            start_time = time.time()
            choice = self.handle_input(request=explain, allowed_inputs=['', 'no'])
            end_time = time.time()
            needed_time = end_time - start_time
            if word in self.ethical_words and needed_time <= 3 and choice == '':
                print("You caught an ethical word!")
                self.arcade_points += 1
                print(f"You currently have {self.arcade_points} points")
            elif word in self.unethical_words and choice == '':
                print("You caught an unethical word!")
                if self.arcade_points == 0:
                    print("You can't lose any points yet!")
                else:
                    self.arcade_points -= 1
                    print(f"You lost a point! You currently have {self.arcade_points} points")
            elif word in self.unethical_words and choice == 'no':
                print("Correct! Not an ethical word!")
            else: 
                print(f"Too slow! You missed the word by {needed_time - 3:.2f} seconds!") 
            print("Prepare for the next word...")

        if self.completed_arcade:
            # Here, the player wins an Apple Watch -> add to inventory
            self.conversation()
        else:
            print("You lost! You return to the main menu.")
        return self.main_menu()

    def try_escape(self) -> str:
        if self.tried_escape:
            print("You already tried to escape once. Maybe you should try something else.")
            return self.main_menu()
        print("You run towards the door")
        time.sleep(1)
        print("In your head you hear the hmmhmmm getting louder and louder")
        time.sleep(2)
        print("Before you can reach the door, you already passed out, your mind drifting infinitely fast through neverending spheres...")
        time.sleep(2)
        print("'There is no escaping this thought experiment! The Arcade is your way out!' you hear a voice in the distance.")
        time.sleep(2)
        print("You wake up in the middle of the room, confused and a little dizzy.\n")
        self.tried_escape = True
        return self.main_menu()

    def conversation(self):
        if not self.tried_escape and not self.completed_arcade:
            player_name = input("\n'Hello, my dear adventurer! Welcome to the GSIT room! May I know your name, brave soul?'\n>>")
            print(f"\n'Hmmmhmm...I once knew someone named {player_name}. Unfortunately, that poor soul never made it out of here.")
            time.sleep(3)
            print("In order to continue your quest, you have to prove to me both your wisdom and your technical knowledge...")
            time.sleep(3)
            print("I challenge you to win the arcade game and prove yourself worthy!'")
            return self.propose_challenge()
        if not self.completed_arcade:
            request="'Welcome back! Are you ready for a test of your ethics skills?' [y/n]\n>>"
            choice = self.handle_input(request=request, allowed_inputs=['y','n'])
            if choice == 'n':
                print("\n'You will soon realize that there is no escape. The game is the only way back to reality!'\n")
                return self.propose_challenge()
            return self.arcade_introduction()
        self.print_end_sequence()
        
    def print_end_sequence(self):
        print("\n'Well done! You have proven yourself to be a true philosopher!' the reading persons says.\n")
        print("'However, this is not the end. In order to leave this place, you have to demonstrate your technical skills as well.")
        print("Unless you can prove to me that fall detection is possible using technical devices, you will be stuck here forever!'")
        print("The person continues reading, not paying any further attention to you...")
        print("Being a wise person as you have shown yourself to be, you remember the Apple Watch around you wrist.")
        print("'I have faith in technolgy' you think!")
        print("You look around the room and see a sign on the wall:")
        print("\tFace me and I shall set you free!\n\tBut beware, if you fail, you will never wake up!\n")
        print("You feel frightened, knowing you will never leave this room if your Smartwatch fails you.")
        print("You decide to put your faith in technology and step in front of the sign, wondering what will happen next...")
        time.sleep(3)
        print("KNOCK")
        time.sleep(2)
        print("Before you could even hear the sound, you feel a strong force pushing you over.")
        print("You *immediately* get knocked out...")
        print("Your mind drifts through spheres again, faster and faster, leaving your unconscious body behind...")
        print("In the distance you hear a sirene, a door getting kicked in and a paramedic shouting 'Doctor, we've found the person!'")
        print("She and the other paramedics put you on a stretcher and carry your body out of the room and into the hallway...")
        print("They give you a shot which brings you back to consciousness...")
        print("You realize that you were in fact not hurt at all, but that your mind was cut off from your body.")
        print("Hadn't it been for the fall detection, you would have never woken up again.")
        print("Your faith in technology has proven to be well placed.")
        print("You are now back in the hallway of the third floor, ready to continue your quest.")

    def propose_challenge(self):
        request = "'Do you have the courage to accept the challenge and prove your worth? [y/n]\n>>"
        choice = self.handle_input(request=request, allowed_inputs=['y','n'])
        if choice == 'y':
            print("\n'Let the games begin!'")
            return self.arcade_introduction()
        print("\n'Too bad! Maybe you need some time to think about it again...'\n")
        return self.main_menu()

    def handle_input(self, request: str, allowed_inputs: list) -> str:
        """
        Handles user input and ensures it is within the allowed inputs.

        Parameters
        ----------
        request (str): What the user will react to
        allowed_inputs (list): A list of valid input options.

        Returns:
        str: A valid input from the allowed inputs.
        """
        
        choice = input(request)
        while choice not in allowed_inputs:
            print(f"Invalid input '{str(choice)}'. Please try again!\n" )
            choice = input(request)
        return choice
    
    def show_arcade_logo(self):
        print("""/
        @@@@@@@@@@@@@@@@@       
        \               /        
         @@@@@@@@@@@@@@@        
         @             @       
         @   ethical   @        
         @    catch    @        
         @             @         
         @             @         
          -------------        
         /             \        
        /               \       
        *****************       
        \               /       
         @@@@@@@@@@@@@@@               
         @      a      @       
         @     GSIT    @         
         @    games    @         
         @  production @                
         @@@@@@@@@@@@@@@ 
        """)

## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
apple_watch=Item("Apple Watch", "A useful device to detect falls", movable=True)
gsit_room = GSITRoom("GSIT Room", "The Morals of Hell")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "gsit": gsit_room
}
