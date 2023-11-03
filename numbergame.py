import random
woohoo = "yes"
victory_screen = """
.--.      .--..-./`) ,---.   .--.,---.   .--.    .-''-.  .-------.    .---.           _ _    .-'''-.    
|  |_     |  |\ .-.')|    \  |  ||    \  |  |  .'_ _   \ |  _ _   \   \   /          ( ` )  /   _   \   
| _( )_   |  |/ `-' \|  ,  \ |  ||  ,  \ |  | / ( ` )   '| ( ' )  |   |   |         (_{;}_)|__/` '.  |  
|(_ o _)  |  | `-'`"`|  |\_ \|  ||  |\_ \|  |. (_ o _)  ||(_ o _) /    \ /           (_,_)    .--'  /   
| (_,_) \ |  | .---. |  _( )_\  ||  _( )_\  ||  (_,_)___|| (_,_).' __   v                  ___'--._ _\  
|  |/    \|  | |   | | (_ o _)  || (_ o _)  |'  \   .---.|  |\ \  |  | _ _             _  |   |  ( ` )  
|  '  /\  `  | |   | |  (_,_)\  ||  (_,_)\  | \  `-'    /|  | \ `'   /(_I_)          _( )_|   `-(_{;}_) 
|    /  \    | |   | |  |    |  ||  |    |  |  \       / |  |  \    /(_(=)_)        (_ o _)\     (_,_)  
`---'    `---` '---' '--'    '--''--'    '--'   `'-..-'  ''-'   `'-'  (_I_)          (_,_)  `-..__.-'   
                                                                                                        
"""
my_logo = """
,---.   .--.  ___    _ ,---.    ,---. _______       .-''-.  .-------.              .-_'''-.      ____    ,---.    ,---.    .-''-.           _____     __   .-'''-.    
|    \  |  |.'   |  | ||    \  /    |\  ____  \   .'_ _   \ |  _ _   \            '_( )_   \   .'  __ `. |    \  /    |  .'_ _   \          \   _\   /  / /   _   \   
|  ,  \ |  ||   .'  | ||  ,  \/  ,  || |    \ |  / ( ` )   '| ( ' )  |           |(_ o _)|  ' /   '  \  \|  ,  \/  ,  | / ( ` )   '         .-./ ). /  ' |__/` '.  |  
|  |\_ \|  |.'  '_  | ||  |\_   /|  || |____/ / . (_ o _)  ||(_ o _) /           . (_,_)/___| |___|  /  ||  |\_   /|  |. (_ o _)  |         \ '_ .') .'     .--'  /   
|  _( )_\  |'   ( \.-.||  _( )_/ |  ||   _ _ '. |  (_,_)___|| (_,_).' __         |  |  .-----.   _.-`   ||  _( )_/ |  ||  (_,_)___|        (_ (_) _) '   ___'--._ _\  
| (_ o _)  |' (`. _` /|| (_ o _) |  ||  ( ' )  \'  \   .---.|  |\ \  |  |        '  \  '-   .'.'   _    || (_ o _) |  |'  \   .---.          /    \   \ |   |  ( ` )  
|  (_,_)\  || (_ (_) _)|  (_,_)  |  || (_{;}_) | \  `-'    /|  | \ `'   /         \  `-'`   | |  _( )_  ||  (_,_)  |  | \  `-'    /          `-'`-'    \|   `-(_{;}_) 
|  |    |  | \ /  . \ /|  |      |  ||  (_,_)  /  \       / |  |  \    /           \        / \ (_ o _) /|  |      |  |  \       /          /  /   \    \\     (_,_)  
'--'    '--'  ``-'`-'' '--'      '--'/_______.'    `'-..-'  ''-'   `'-'             `'-...-'   '.(_,_).' '--'      '--'   `'-..-'          '--'     '----'`-..__.-'   

"""
#Number Guessing Game Objectives:

while woohoo == "yes":
  print(f"{my_logo}")
  the_number = random.randint(0, 101)
  lives = 5

  difficulty = input("Choose difficulty!\nEasy\nMedium\nHard\n\n").lower()

  if difficulty == "easy":
    lives += 5
    print(f"You have {lives} attempts the number!\n")
  elif difficulty == "medium":
    lives += 2
    print(f"You have {lives} attempts the number!\n")
  elif difficulty == "hard":
    lives += 0
    print(f"You have {lives} attempts the number!\n")

  if lives != 0:
    while lives != 0:
      guess = int(input("Guess a number!\nYour Guess: "))
      lives -= 1
      if lives == 0:
        woohoo = input("Do you want to play again?\nYes or No?\n")
      print(f"You have {lives} attempts left!")
      if guess == the_number:
        print(victory_screen)
        lives -= lives
        woohoo = input("Do you want to play again?\nYes or No?\n")
      elif guess < the_number:
        print("The number is higher than that!\n")
      elif guess > the_number:
        print("The number is lower than that!\n")


if lives == 0:
  print(f"Game over!, the number was {the_number}\n")

 
  



































# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

