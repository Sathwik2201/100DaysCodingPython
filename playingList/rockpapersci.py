rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
ur_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if ur_choose >= 3 or ur_choose < 0:
  print("Invalid number!,you lose")
else:  
  rps = [rock,paper,scissors]
  ur_move = rps[ur_choose]
  print(ur_move)
  computer_choose = random.randint(0,2)
  computer_move = rps[computer_choose]
  print("Computer chose:\n",computer_move)
  if ur_move == rock and computer_move == scissors or ur_move == scissors and   computer_move == paper or ur_move == paper and computer_move == rock :
    print("You Win!")
  elif ur_move == computer_move:
    print("It's a draw")
  else:
   print("You lose")

