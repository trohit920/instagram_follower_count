import random 
from art import logo, vs 
from game_data import data
import os

print(logo)
print("Comparing Instagram followers..!!\n")
score = 0
B = random.choice(data)

def compare(a_follower,b_follower):
  if a_follower > b_follower:
    return 0  
  else:
    return 1

def game():
  global B 
  A = B
  B = random.choice(data)
  if A == B:
    B = random.choice(data)
  a_follower = A['follower_count']
  b_follower = B['follower_count']

  print(f"Compare A: {A['name']}, {A['description']} from {A['country']}")
  print(vs)
  print(f"Against B: {B['name']}, {B['description']} from {B['country']}")
  return a_follower,b_follower 

def play():
  is_correct = True
  a_follower,b_follower = game()
  # print(a_follower, b_follower)

  while is_correct: 

    res = compare(a_follower,b_follower)
    # print(res) 
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_guess == "a" and res == 0:
      global score 
      score = score + 1 
      os.system('clear')
      print(logo)
      print(f"You're right! Current score: {score}.")
    elif user_guess == "b" and res == 1:
      score = score + 1
      os.system('clear')
      print(logo)
      print(f"You're right! Current score: {score}.")
    else:
      os.system('clear')
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      # is_correct = False
      return 
    a_follower,b_follower = game()

play()
