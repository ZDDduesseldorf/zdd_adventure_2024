inspection_number = 0
inspection_number =+ 6

print(inspection_number)
riddle_keys = {
        "thick_bushes": [True, inspection_number],
        "skylight": [False, 0],
        "intricate_plant_pot": [True, 2],
        "vines": [True, 1],
        "snake_statue": [True, 3]
    }
riddles = {
            "thick_bushes": "What is can be symbol of independence, carried by those who carve their own path?",    # thick bushes
            "skylight": "What glints in the moonlight, a silent guardian by night?",                                # skylight
            "intricate_plant_pot": "What can be an artist's brush on a canvas of a garden?",                        # intricate plant pot
            "vines": "It cuts through vines without a sound, yet speaks volumes when needed. What is it?",          # vines
            "snake_statue": "Sharp as a serpent's tooth, yet not venomous. What am I?"                              # snake statue
        }
input1 = "thick_bushes"
input2 = "something different"
filter_for_bool = {key: value for key, value in riddle_keys.items() if value[0]} # filters for bools in riddle dict

# if not filter_for_bool:
#     print("dict is empty")
# else:
#     most_recent_riddle = max(filter_for_bool.items(), key=lambda item: item[1][1]) # find item with highest value (second element in the list)
#     print(riddles[most_recent_riddle[0]])


# for entry in riddles:
#     print(f"type '{entry}' for {entry}")
# playterinput = input()

# if playterinput in riddles:
#     print(f"heading to {playterinput}")
# else:
#     print("not recognized!")

opening_prompts = ["Well hello there! It's been a while since anyone came to visit me. I am Dr. Sylas Thorncroft, and perhaps who might you be?\n",
                           "Look who's back already! Came to take another look at things? Remind me of your name please\n",
                           "You don't seem to get bored! Amazing that you're still here.\n"]

print(len(opening_prompts)-1)