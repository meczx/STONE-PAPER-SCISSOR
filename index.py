import random

print("Welcome to the Game")
print("Enter your choice 1:Rock ,2:Paper, 3:Scissor")

choice = int(input("choice(1/2/3):"))
com_choice = random.randint(1, 3)

if choice == com_choice:
    print("Match Draw")
elif choice == 1:
    if com_choice == 2:
        print("computer wins!")
    else:
        print("you wins!")
elif choice == 2:
    if com_choice == 3:
        print("computer wins!")
    else:
        print("you wins!")
elif choice == 3:
    if com_choice == 1:
        print("you wins!")
    else:

        print("computer wins!")
