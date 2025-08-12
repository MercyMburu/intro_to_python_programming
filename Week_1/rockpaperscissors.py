# Rock Paper Scissors Game
# Build a Human-versus-Computer Rock-Paper-Scissors Game

# In this project, you will create a script to allow the user to play rock-paper-scissors against the computer. For starters, if you are not familiar with the game, you need to understand that: rock beats scissors, scissors beats paper, and paper beats rock. Here are the steps to follow in build your game:

#     Utilise the Random Python Library to allow the computer to randomly choose rock, paper, or scissors in each round
#     Allow the user to now input their choice and compare it directly with the computer’s choice. You can then declare the winner of the round based on the rules of the game
#     Now, instead of declaring the winner, just assign a point to the winner of a round. This should allow you to utilise loops to increase the rounds within a game to 3 or 5. Your program will assign points to the winner of each round and declare the winner after all rounds i.e the one with the most points.
#     To make the game more efficient, stop the game and declare the winner immediately a user guess 2 points out of 3 in a 3-round game or 3 out of 5 points in a 5-round game. This should stop the game from continuing when there’s already a clear winner even if all rounds have not been completed.
#     You can now freely play rock-paper-scissors with your computer and see how well you perform against the computer’s randomised choices.


choices=["rock","paper","scissors"]

my_score=0
comp_score=0
round_num=1

while round_num<3:
    print("This is round number: ",round_num)
    my_choice=input("Choose between rock,paper and scissors: ")
    
    if my_choice != "rock" and my_choice != "paper" and my_choice != "scissors":
        print("Invalid.")
        continue
    print("Enter Computers choice (rock, paper, or scissors):")
    computer_choice = input("Computer's choice: ").lower()
    
    if computer_choice != "rock" and computer_choice != "paper" and computer_choice != "scissors":
        print("Invalid computer choice.")
        continue
    print("You chose:", my_choice)
    print("Computer chose:", computer_choice)

    # Determine the winner of the round
    if my_choice == computer_choice:
        print("You tied! No points.")
    elif (my_choice == "rock" and computer_choice == "scissors") or \
         (my_choice == "scissors" and computer_choice == "paper") or \
         (my_choice == "paper" and computer_choice == "rock"):
        print("You win this round!\n")
        my_score += 1
    else:
        print("Computer wins this round!\n")
        comp_score += 1

    print("My Score:",my_score)
    print("Computer Score:",comp_score)

    
    if my_score == 2 or comp_score == 2:
        break

    round_num += 1

print("\nGame Over!")
if my_score > comp_score:
    print("You won the game! ")
elif my_score== comp_score:
     print("You tied! ")
else:
    print("Computer won the game.")



    




