import random

def score_cal(x,y):
    global score
    if user==computer:
        print("Computer's Move: ",y)
        print("Draw, Once More")
        print("Score: ",score)
        print(" ")
    elif user=="Rock" and computer=="Scissors" or user=="Paper" and computer=="Rock" or user=="Scissors" and computer=="Paper":
        print("Computer's Move: ",y)
        print("You WIN!!")
        score+=1
        print("Score: ",score)
        print(" ")
    else:
        print("Computer's Move: ",y)
        print("Computer WINS!!")
        print("Score: ",score)
        print(" ")


#main
print('''Enter Your Move
1. Rock
2. Paper
3. Scissors
      ''')
score=0
next=0
moves=["Rock","Paper","Scissors"]
while next==0:
    computer= moves[random.randint(0,2)]
    user=input("Enter your Move: ").title()
    if user in moves:
        pass
    else:
        print("Invalid Move! Try Again")
        exit()

    score_cal(user,computer)

