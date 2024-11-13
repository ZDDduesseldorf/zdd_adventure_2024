"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
import threading
import time
import os




class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            return [x for x in user_items if x.name != "old book"]       # Remove book from inventory
        return user_items
    
                


class Gym(Room):
    def check_pygame(self):
        try:
            import pygame
        except ImportError:
            print("<<<pygame is not installed, you sadly will enter the gym with no music>>> \n<<<unless you manually install it with 'pip install pygame' and try again !>>>\n")
            self.pygame_available = False
            time.sleep(2)
            return False
        else:
            print("pygame is there! \nhave fun listening to music\n")
            pygame.mixer.init()
            pygame.mixer.music.load(self.get_file_location())
            pygame.mixer.music.set_volume(0.05)
            self.pygame_available = True
            return True
        

    def get_file_location(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))     # Use the directory where the script is located as the base path
        file = os.path.join(base_dir, "gym_song.mp3")             #and ignore the current working directory in the terminal
        return file


   
    def play_music(self):
        if self.pygame_available:                    #handling errors if pygame is not installed
            try:
                import pygame
                pygame.mixer.music.play(-1)          # Loop indefinitely
                while pygame.mixer.music.get_busy():
                    time.sleep(1)                    # Check each second if the music is still playing

            except Exception as e:                   # Catch any errors that occur during music playback and print an error message
                print(f"Error playing music: {e}")   # This prevents the program from crashing if something goes wrong with pygame
        else:
            print("Music playback skipped because pygame is not installed.")

   
   
    def stop_music(self):
        if self.pygame_available:                                                     #handling errors if pygame is not installed
            import pygame
            pygame.mixer.music.stop()


    def run_story(self, user_items):
        if self.check_pygame():
            self.music_thread = threading.Thread(target=self.play_music,  daemon=True) #threading is used to be able to do multiple tasks at once (music and storyline)
            self.music_thread.start()
        
        while True:                                                                    # a while loop, to always keep asking the user the first question

            print("Welcome to the Gym! You see various gym equipment around.\n")
            action = input("Would you like to 'train', do 'cardio', or 'end' your session?\n ").strip().lower()
            training_ascii="""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢴⡄⠀⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⣰⣧⣼⣿⣽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣇⠀⣿⠿⢿⠻⠿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣾⠿⠢⠄⠁⠀⣬⣿⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⠀⠀⢀⠠⠧⠄⠈⣧⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⢄⣀⠀⠀⣀⣀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡏⠉⠠⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡖⠉⠑⠀⠲⣤⠤⠘⠉⡁⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⡀⠀⡄⠀⠰⠀⠀⠀⢹⡀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⢲⢧⣠⣀⣀⠴⢄⣀⣤⣆⠘⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠎⡾⣄⣀⣀⣴⠒⢄⣀⣿⠀⢺⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⢰⣷⣖⠁⠁⢈⡀⠣⣾⢻⣄⡜⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠁⢳⢉⡏⠃⠠⡀⠀⡏⠉⣼⠸⠙⡀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⢰⠟⣄⢰⠈⢹⠉⢰⣿⣆⡆⠱⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⡤⡔⠊⠉⡱⢆⠀⠀⠀⠀⠀⠀⠀⢸⠀⢀⡞⠀⠈⠳⡶⢼⠤⡿⠁⠘⣷⠀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⣀⠀⠀⠀⠀⠀⠀
⢀⡔⢺⠁⠀⡇⠀⠀⢷⠈⢣⠀⠀⠀⠀⠀⢀⣼⢦⣼⣁⣀⠤⠤⠷⠤⠼⠥⠤⢤⣻⣟⣻⡀⠀⠀⠀⠀⠀⡴⠋⠀⢸⠈⠹⠒⢄⡀⠀⠀
⢻⠀⢸⠀⠀⢧⠀⠀⠸⣷⡞⢧⢀⡠⠤⠒⠛⣿⡓⣛⣧⣤⠒⡶⢶⣲⡶⠒⠶⣶⠏⠨⣹⣗⠒⠢⠤⣀⡎⠀⠀⠀⡘⠀⢠⠀⠈⡏⢳⡄
⢸⠀⠀⡆⠀⠸⡄⠀⠀⢣⣤⠊⢁⡠⠤⠒⠉⠻⢿⡿⠋⠋⠐⡅⠀⣿⠀⠀⠰⠉⠚⣿⠋⠀⠉⠑⠢⡤⣉⣲⠀⢠⠃⠀⡜⠀⢠⠀⠸⢸
⠀⡆⠀⢹⡀⠀⢳⠀⠀⠈⢏⠋⢳⠀⠀⠀⠀⠀⠸⣇⢄⡖⠀⢸⢸⢿⠰⠀⠀⡟⢰⠇⠀⠀⠀⠀⣸⠀⠀⠀⣰⠏⠀⣰⠃⢀⡎⢀⠇⡸
⡀⠹⡄⠀⢷⠀⠀⢧⠀⠀⠈⡆⠀⡇⠀⠀⠀⠀⠀⢹⡟⠑⢤⣾⠋⠀⢳⣀⠘⠙⠇⠀⠀⠀⠀⠀⡟⠀⢀⣼⠋⠀⡰⠃⠀⡜⠀⡜⢀⠃
⢣⡀⢹⣆⡀⢳⣀⠀⠳⣄⡀⠘⢦⡕⠀⠀⠀⠀⠀⢸⡇⠀⠀⢳⠀⠀⣼⠉⠀⢸⡆⠀⠀⠀⠀⠀⠺⣶⡚⠁⣠⠖⠁⣠⠎⢀⡜⣠⠊⠀"""

            if action == "train":
                print("What are you planning on training today?")
                train_type = input("'upper body' or 'lower body'? ").strip().lower()

                if train_type == "upper body":
                    upper_body_exercise = input("Do you want to start with 'chest', 'back', or 'arms'? ").strip().lower()

                    if upper_body_exercise == "chest":
                        print("You start with some chest exercises: bench press, push-ups, and chest flys.")
                        print(training_ascii)
                        time.sleep(4)
                        workout_summary = "Chest workout: bench press, push-ups, chest flys."
                    elif upper_body_exercise == "back":
                        print("You begin your back workout with pull-ups, rows, and deadlifts.")
                        print(training_ascii)
                        time.sleep(4)
                        workout_summary = "Back workout: pull-ups, rows, deadlifts."
                    elif upper_body_exercise == "arms":
                        print("You focus on arms with bicep curls, tricep extensions, and hammer curls.")
                        print(training_ascii)
                        time.sleep(4)
                        workout_summary = "Arms workout: bicep curls, tricep extensions, hammer curls."
                    else:
                        print("That's not a valid option in the gym.")
                        continue

                elif train_type == "lower body":
                    lower_body_exercise = input("Do you want to start with 'hamstrings', 'quads', or 'calves'? ").strip().lower()

                    if lower_body_exercise == "hamstrings":
                        print("You start with exercises for hamstrings: deadlifts, leg curls, and bridges.")
                        print(training_ascii)
                        time.sleep(4)
                        workout_summary = "Hamstrings workout: deadlifts, leg curls, bridges."
                    elif lower_body_exercise == "quads":
                        print("You focus on quads with squats, lunges, and leg presses.")
                        print(training_ascii)
                        time.sleep(4)
                        workout_summary = "Quads workout: squats, lunges, leg presses."
                    elif lower_body_exercise == "calves":
                        print("You hit calves with standing and seated calf raises.")
                        print(training_ascii)
                        time.sleep(4)
                        workout_summary = "Calves workout: standing and seated calf raises."
                    else:
                        print("That's not a valid option in the gym.")
                        continue
                else:
                    print("That's not a valid option in the gym.")
                    continue

            elif action == "cardio":
                running_ascii = """
                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \\   ,/;,
               ,-' /'  \\_   \\ / _/
               `\\ /     _/\\  ` /
                 |     /,  `\\_/
                 |     \\'
    /\\_        /`      /\\
   /' /_``--.__/\\  `,. /  \\
  |_/`  `-._     `\\/  `\\   `.
            `-.__/'     `\\   |
                          `\\  \\
                            `\\ \\
                              \\_\\__
                               \\___)
                """
                cardio_duration = 10
                print("You hop on the treadmill and start your cardio session.")
                print(running_ascii)
                time.sleep(4)
                print(f"You have been running for {cardio_duration} minutes!")

                while True:

                    continue_cardio = input("Do you want to continue? (yes/no) ").strip().lower()      #option to be able to continue doing cardio

                    if continue_cardio == "yes":
                        cardio_duration += 10
                        print(running_ascii)
                        time.sleep(4)
                        print(f"You have been running for {cardio_duration} minutes!")
                    elif continue_cardio == "no":
                        print(f"You have done cardio for {cardio_duration} minutes, respect!")
                        break                                                                          # Cardio finished 
                    else:
                        print("That's not a valid option. Please answer with 'yes' or 'no'.")

            elif action == "end":
                self.stop_music()                                                                     #stops music
                print("You decide to end your session. Good workout!")
                return                                                                                #end session  
            else:
                print("That's not a valid option in the gym.")


## ----------------------------------------------------------------
## List here all rooms

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
gym_room = Gym("Gym", "the place where you could get jacked" )                                         #room instance 

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "gym_room": gym_room   
} 