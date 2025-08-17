import random

def SWG():
    print("Welcome to you Snake, Water, Gun game")
    valid_choice = ["Snake", "Water", "Gun"]
    
    player_input = input("Enter your choice(Snake, Water,Gun):").capitalize()
    
    if player_input not in valid_choice:
        print("Invalid choice! Please choose from Snake, Water, or Gun.")
        
    computer_choice = random.choice(valid_choice)
    
    print(f"Your choice: {player_input} and computer choice: {computer_choice}")
    
   
    
    if player_input == computer_choice:
        print("The game is draw")
    elif (player_input == "Snake" and computer_choice == "Water") or \
         (player_input == "Water" and computer_choice == "Gun") or \
         (player_input == "Gun" and computer_choice == "Snake"):
        print("You win!")
        
    else:
        print("computer wins!")   
SWG()       