import random


# This app is a console rock-paper-scissors game played against the computer that tracks the score of the player and the computer.
# The winner of each round is awarded one point and points are accumulated until the human player decides to quit. 
# The score is displayed after each round and when the game ends.


def print_score(score):
    """this function prints the current score"""
    total_games = score["Player"] + score["Computer"]
    player_percentage = (score["Player"] / total_games) * 100
    computer_percentage = (score["Computer"] / total_games) * 100

    print("Scoreboard:")
    print("--------------------")
    print("| Player  | Computer |")
    print("--------------------")
    print(f"|   {score['Player']}    |    {score['Computer']}    |")
    print("--------------------")
    print(f"Total Games: {total_games}")
    print(f"Player Win Percentage: {player_percentage:.2f}%")
    print(f"Computer Win Percentage: {computer_percentage:.2f}%")


def main():
    """this function prompts the user for input and manages the game loop while calling other functions"""
    print("Welcome to Rock-Paper-Scissors!")
    score = {"Player": 0, "Computer": 0}
    while True:
        choice = input("\nEnter your choice (rock, paper, scissors) or 'q' to quit:")
        print()
        if choice == "q":
            break
        if choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        result = determine_winner(choice, computer_choice)
        if result == "Player":
            score["Player"] += 1
            print("You win!")
        elif result == "Computer":
            score["Computer"] += 1
            print("Computer wins!")
        else:
            score["Computer"] += 0.5
            score["Player"] += 0.5
            print("It's a tie!")
        print_score(score)
    if score["Player"] > score["Computer"]:
        print("You won the game!")
    elif score["Player"] < score["Computer"]:
        print("Computer won the game!")
    else:
        print("It's a tie!")
    print("Final score:")
    print_score(score)


def get_computer_choice():
    """this function generates a random choice for the computer"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    """this function determines the winner based on the player's choice and the computer's choice"""
    # implementation of determining the winner
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        return "Player"
    else:
        return "Computer"


if __name__ == '__main__':
    main()
