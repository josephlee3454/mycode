import random

def game():

  x  = input("rock paper scissors shoot type in your fist shape and lets let the fists do the talking")
  
if x == "rock":
    rock()
if x == "scissor":
    scissors()
if x == "paper":
    paper()
    

def comp_hand():
    handArr = ["rock", "scissors" , "paper"]
    idx = random.randrange(0,2)
    print(handArr[idx])
    return handArr[idx]

def rock():
  if comp_hand() == "rock":
    print("same it was a tie you escape defeat this one time")
    game()
  elif comp_hand == "paper":
    print("i won hahaha humans are not as smart as computers")
    game()
  else:
    print("you beat a computer i am sad all of a sudden i have developed a distaste for humans")
  
def paper():
  if comp_hand() == "paper":
    print("same it was a tie you escape defeat this one time")
    game()
  elif comp_hand == "scissors":
    print("i won hahaha humans are not as smart as computers but its ok ill add ytour numbers for you ans send your stupid selfies")
    game()
  else:
    print("you beat a computer i am sad all of a sudden i have decided maybe its humanitys end !!!!!!")

def scissors(): 
  if comp_hand() == "scissors":
    print("same it was a tie you escape defeat this one time")
    game()
  elif comp_hand == "rock":
    print("i won hahaha humans are not as smart as computers but its ok ill add ytour numbers for you ans send your stupid selfies")
    game()
  else:
    print("you beat a computer i am sad all of a sudden i have decided maybe its humanitys end !!!!!!")

  

game()  























