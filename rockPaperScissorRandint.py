from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Enter Your Choice : ").lower()
print("Computer Choice : ",end=" ")
computer = randint(0,2)
if(computer == 0):
    player2 = "rock"
elif(computer == 1):
    player2 = "paper"
elif(computer == 2):
    player2 = "scissors"
print(player2)

if (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
	print("\nPlayer wins!\n")
elif (player1 == "rock" and player2 == "paper") or (player1 == "paper" and player2 == "scissors") or (player1 == "scissors" and player2 == "rock"):
	print("\nComputer wins!\n")
elif player1 == player2:
	print("\nIt's a tie!\n")
else:
	print("\nsomething went wrong\n")