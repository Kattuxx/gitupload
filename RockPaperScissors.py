import random

def main():

    # we need a choice of rock, paper, or scissors from the user
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose one of the following:")
    userChoice = input("Rock, Paper, or Scissors? ")


    choices = ["Rock", "Paper", "Scissors"]
    computerChoice = random.choice(choices)

    print("You chose: " + userChoice)
    print("The computer chose: " + computerChoice)

    if userChoice == computerChoice:
      print("It's a tie!") 
    elif userChoice == "Rock" and computerChoice == "Paper" or \
    userChoice == "Paper" and computerChoice == "Scissors" or \
    userChoice == "Scissors" and computerChoice == "Rock":
      print("You lost! Sucks to be you!")
    elif (userChoice == "Rock" and computerChoice == "Scissors") or \
    (userChoice == "Paper" and computerChoice == "Rock") or \
    (userChoice == "Scissors" and computerChoice == "Paper"):
      print("You won! Congrats!")

while True:
    main()
    if input("Play again? (Y/N)").strip().upper() != 'Y':
        break

# computer needs to choose rock, paper, or scissors
# we need to compare the two choices
# we need to print out who won 
# we need to print out who lost
# offer another game