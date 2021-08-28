# first lets import the rendom library
import random
from game_data import data
from art import logo , vs
from replit import clear
print(clear())

# creating the random genarator for the compare value
index = random.randint(0,len(data))
# createing another random genarator for the vs value
vIndex = random.randint(0,len(data))
# print(f"Length of dagta {len(data)}")
# for keep track fo weather the game is over or not we will create another bool variable with False
is_game_over = False
# to keep track of te user we will create a object ..
user_point = 0
'''the option i choose must be greatter then the computer choosing option
and it will printn the current score by saying your correct'''
def compare(choose,folower_of_B):
  is_correct = False
  global user_point
  point = user_point
  if choose > folower_of_B:
    # to keep track of te user we will create a object ..
    user_point = point + 1
    is_correct = True
  elif choose< folower_of_B:
    user_point = point
    is_correct = False
  if is_correct:
    print("You're correct")
    print(f"Current score is : {user_point}")
    is_game_over =False
  elif not is_correct:
    print("you're rong")
    print(f"Current score is {user_point}")
    is_game_over = True
  return is_game_over
print(logo)
choose = ""
while not is_game_over:
  # now i am going to store the against string to a variable object.
  compareA = f"Compare A: {data[index]['name']} ,{data[index]['description']} from {data[index]['country']}"
  compareB = f"Against B: {data[vIndex]['name']}, {data[vIndex]['description']}, from {data[vIndex]['country']}"
  # geting the value of the folower 
  '''we need to work with this two things in our project'''
  folower_of_A = data[index]['follower_count']
  folower_of_B = data[vIndex]['follower_count']
  print(compareA)
  print(vs)
  print(compareB)
  user_choise = input("Who has more followers? Type 'A' ro 'B'")
  if user_choise == "A":
    choose = folower_of_A
    is_game_over = compare(choose,folower_of_B)
    if not is_game_over:
      index = vIndex
  elif user_choise=="B":
    choose = folower_of_B
    is_game_over =  compare(choose,folower_of_A)
    # tempIndex = random.randint(0,len(data))
    if not is_game_over:
      index = vIndex
  vIndex = random.randint(0,len(data))
      

