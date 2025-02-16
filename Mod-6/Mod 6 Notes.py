# print("Hello World");

# rock, paper scissors
import math;
import random;

choices = ["rock", "paper", "scissors"]
print("Welcome to the game")
playerInputs = input("Enter \t Rock, \t Paper or Scissors \n").lower()

while playerInputs not in choices:
    playerInputs = input("Invalid choice. Choose \t Rock, \t Paper or Scissors \n").lower()

print("Player's choice is: " + playerInputs)

computer = random.choice(choices)
print("Computer's choice is: " + computer)

while playerInputs == computer:
    playerInputs = input("tie. Choose \t Rock, \t Paper or Scissors \n").lower()
    computer = random.choice(choices)
    print("Computer's choice is: " + computer)
    if (playerInputs == "rock" and computer == "scissors") or (playerInputs == "paper" and computer == "rock") or (playerInputs == "scissors" and computer == "paper"): 
        print("You win") 
        exit()
    else:
        print("You lose") 
        exit()

if (
    playerInputs == "rock" and computer == "scissors"
) or (
    playerInputs == "paper" and computer == "rock"
) or (
    playerInputs == "scissors" and computer == "paper"
): 
    print("You win")
else:
    print("You lose")


# LIST
my_list = [10,20,5,4]
my_list.append(12)
my_list.remove(10)
my_list.sort()
print(my_list)

my_tuple = (1,2,3,4)

my_set = {1,2,3,4}
print(my_set.union({10,13}))

my_dict = {"name":"wilson", "age":20}
print(my_dict["name"])
my_dict["city"]="New York"

print(my_dict.keys())
print(my_dict.values())


