import random

def user_choice():
    user_input = int(input("Enter your choice: \n0. for Snake\n1. for Water\n2. for Gun\n"))
    
    if (user_input < 0 or user_input > 2):
        print("Invalid choice, please try again")
        user_choice()
    else:
        return user_input
    

user_choice = user_choice()

computer_choice = random.randint(0,2)

# if ( user_choice == 0 ):
#     match computer_choice:
#         case 0:
#             print("Computer chose 0.) Snake. It's a tie!")
#         case 1:
#             print("Computer chose 1.) Water. You win!")
#         case 2:
#             print("Computer chose 2.) Gun. You Lose!")
# elif ( user_choice == 1 ):
#     match computer_choice:
#         case 0:
#             print("Computer chose 0.) Snake. You Lose!")
#         case 1:
#             print("Computer chose 1.) Water. It's a tie!")
#         case 2:
#             print("Computer chose 2.) Gun. You Win!")
# else:
#     match computer_choice:
#         case 0:
#             print("Computer chose 0.) Snake. You Win!")
#         case 1:
#             print("Computer chose 1.) Water. You Lose!")
#         case 2:
#             print("Computer chose 2.) Gun. It's a tie!")


choices = [
    [0, 1, -1],
    [-1, 0, 1],
    [1, -1, 0],
]

match choices[user_choice][computer_choice]:
    case -1:
        print(f"Computer chose {computer_choice} You Lose!")
    case 0:
        print(f"Computer chose {computer_choice} A Tie!")
    case 1:
        print(f"Computer chose {computer_choice} You Win!")
