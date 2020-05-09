import random

def fun(score,comp):
    i=0
    flag=0
    while(i<3):
        print("Attempt ", (i+1), ": ")
        g=int(input("Guess a Number.."))
        if(g==comp):
            print('Computer\'s Choice is ', comp)
            score[0]=score[0]+1
            flag=1
            print('\t---------------')
            print('\tHurray! You WIN')
            print('\t---------------')
            break
        else:
            if(g<comp):
                print("Guess a number greater than ", g)
            else:
                print("Guess a number less than ", g)
        i=i+1

    if(flag==0):
        print('Computer\'s Choice is ', comp)
        score[1] = score[1] + 1
        print('\t---------------')
        print('\tSorry, You LOST')
        print('\t---------------')

print("Let's Play...")
print("You will get 3 attempts to guess the number...")
score=[0,0]
while 1:
    print('\n===============================================================================')
    print("Menu Options:")
    print("\t1. Range=(1,50)")
    print("\t2. Range=(51,100)")
    print("\t3. Range=(1,100)")
    print("\t0. Exit.")
    ch=int(input("Enter Your Choice:"))
    if(ch==1):
        comp = random.randint(1,50)
        fun(score,comp)
    elif(ch==2):
        comp = random.randint(51,100)
        fun(score,comp)
    elif(ch==3):
        comp = random.randint(1, 100)
        fun(score, comp)
    elif(ch==0):
        print("Thank You!")
        print('Your Score = ', score[0], ' Computer\'s Score = ', score[1])
        break
    print('Your Score = ', score[0], ' Computer\'s Score = ', score[1])

