file=open("Scoreboard.txt","a")
import random
import operator
count=0
print("Welcome to Pratice Your Abacus")
username=input("Enter your Player's name")
y="yes"
while y=="yes":
    mode=input("Enter which mode you want to play \n random with stop \n random infinity\n steady with stop\n steady infinity\n once:")
    digit=int(input("Enter no of digits you want to practice with"))
    if digit>0:
        if mode=="once":
            o=(input("Enter the operation you want to do"))# we can randomize operators and no of digits by asking user do they want to do that
            a=random.randint(0,10**digit-1)
            b=random.randint(0,10**digit-1)
            z=int(input(str(a)+o+str(b)+"="))
            ops = { "+": operator.add, "-": operator.sub ,"*": operator.mul,"/": operator.truediv,"**": operator.pow}
            if z==ops[o](a,b):
                print("Your answer is correct")
            else:
                print("Correct answer was",ops[o](a,b))
            y=input("Do you want to play again,yes or no")
    ################################################
        if mode=="steady with stop":
            count1=0
            o=(input("Enter the operation you want to do"))
            for i in range(1000):
                 a=random.randint(0,10**digit-1)
                 b=random.randint(0,10**digit-1)
                 z=int(input(str(a)+o+str(b)+"="))
                 ops = { "+": operator.add, "-": operator.sub ,"*": operator.mul,"/": operator.truediv,"**": operator.pow}
                 if z==ops[o](a,b):
                    count1+=1
                 else:
                    print("Answer was wrong,your no of correct answers are",count1)
                    y=input("Do you want to play again,yes or no")
                    count=count1
                    break
    #################################################
        if mode=="steady infinity":
            count1=0
            count2=0
            o=(input("Enter the operation you want to do"))
            ops = { "+": operator.add, "-": operator.sub ,"*": operator.mul,"/": operator.truediv,"**": operator.pow}
            for i in range(1000):
                a=random.randint(0,10**digit-1)
                b=random.randint(0,10**digit-1)
                z=input(str(a)+o+str(b)+"=")
                ops = { "+": operator.add, "-": operator.sub ,"*": operator.mul,"/": operator.truediv,"**": operator.pow}
                if z=="stop":
                    print("No of Correct Answers are:",count1,"No of wrong answers are:",count2)
                    y=input("Do you want to play again,yes or no")
                    count=count1-count2
                    break
                if int(z)==ops[o](a,b):
                    count1+=1
                if int(z)!=ops[o](a,b):
                    count2+=1
        ###############################################
        if mode=="random with stop":
            count1=0
            for i in range(1000):
                  a=random.randint(0,10**digit-1)
                  b=random.randint(1,10**digit-1)
                  opz=("+","-","*")
                  ops = { "+": operator.add, "-": operator.sub ,"*": operator.mul,"/": operator.truediv,"**": operator.pow}
                  o=random.choice(opz)
                  if a%b==0:
                      o="/"
                  z=int(input(str(a)+o+str(b)+"=")) #use int() or line 71 will not work z will be considered string
                  if z==ops[o](a,b):
                      count1+=1
                  else:
                       print("Answer was wrong,your no of correct answers are",count1)
                       y=input("Do you want to play again,yes or no")
                       count=count1
                       break
            ###########################################
        if mode=="random infinity":
            count1=0
            count2=0
            for i in range(1000):
                a=random.randint(0,10**digit-1)
                b=random.randint(1,10**digit-1)
                opz=("+","-","*")
                ops = { "+": operator.add, "-": operator.sub ,"*": operator.mul,"/": operator.truediv,"**": operator.pow}
                o=random.choice(opz)
                if a%b==0:
                    o="/"
                z=input(str(a)+o+str(b)+"=")
                if z=="stop":
                    print("No of Correct Answers are:",count1,"No of wrong answers are:",count2)
                    y=input("Do you want to play again,yes or no")
                    count=count1-count2
                    break
                if int(z)==ops[o](a,b):
                    count1+=1
                if int(z)!=ops[o](a,b):
                    count2+=1


         # we can also count how many times reapeadlty user can do and make a text dispaly score of every user and high score
if y=="no":
    file.write(username+str(count)+"\n")
    print("Thanks For Playing,See you Next Time  (•◡•) /")# we can also set a timer and display how time they took and record it also.We can also the timer real time to user
    file.close()                                                        # we can also record the score of each player with thier username into a text file.
