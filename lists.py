character_list = ["Donut","Alien", "Blueball" ]
for item in range(len(character_list)):
    print(item + 1, character_list[item])
select_character = input( "Select a character: ")
select_character = int(select_character) - 1
description_list = ["Will shoot sprinkles to eliminate enemies", 
                    "Will use lazers to slice through enemies", 
                    "Bounce on enemies and crush them"]
print(character_list[select_character]," - ", description_list[select_character])