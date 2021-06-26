'''
Create a python program in which the user selects a particular 
range of number (example 20 to 80 or 330 to 430). The system 
should automatically select some random number and the user 
must identify that number selected by the system in minimum number of guesses. 
 
If the user identifies it in the required number of guesses then it 
should print "Yeah! You identified the number" 
 
else if the number guessed by the user is higher than the randomly 
selected number then it should print 
"Please try again! The number you guessed is too high" 
 
else if he number guessed by the user is smaller than the randomly 
selected number then it should print 
"Please try again! The number you guessed is too small". 
 
Else if the user does not guess the integer in minimum number of guesses, then it should 
give "Oops! All you chances are finished. Better luck next time!"
'''
import random
def game(x,y) :
    c=0
    if(y-x) < 100 :
        c=5
        print("Let's start the Game! You will be having 5 chances to guess a random number between the values entered!")
    else :
        c=10
        print("Let's start the Game! You will be having 10 chances to guess a random number between the values entered!")
    while True :
        r = random.randint(x,y)
        for i in range(c) :
            guess = int(input("Enter your guess number" + str(i+1) + ": "))
            if guess == r:
                print('Yeah! You identified the number')
                break
            elif guess < r :
                print('Please try again! The number you guessed is too small')
            else :
                print('Please try again! The number you guessed is too high')
        if i ==c:
            print('OOPS! All you chances are finished. Better luck next time!')
        ch = input('Do you want to continue playing?(y/n) ')
        if ch != 'y':
            break
    print("Thank You!")


def choose() :
    x=y=0
    while x>=y :
        x = int(input("Enter the starting number: "))
        y = int(input("Enter the ending number: "))
        if x>=y:
            print("OPPS! The starting value must be smaller than the ending value!\n")
    game(x,y)

choose()

#output
'''
Enter the ending number: 120
Enter your guess number1: 50
Enter your guess number2: 20
Please try again! The number you guessed is too small
Enter your guess number3: 35
Please try again! The number you guessed is too high
Enter your guess number4: 30
Please try again! The number you guessed is too high
Enter your guess number5: 25
Please try again! The number you guessed is too small
Enter your guess number6: 28
Please try again! The number you guessed is too high
Enter your guess number7: 26
Yeah! You identified the number
Do you want to continue playing?(y/n) y
Enter your guess number1: 70
Please try again! The number you guessed is too small
Enter your guess number2: 100
Please try again! The number you guessed is too small
Enter your guess number3: 115
Please try again! The number you guessed is too small
Enter your guess number4: 117
Please try again! The number you guessed is too small
Enter your guess number5: 119
Please try again! The number you guessed is too small
Enter your guess number6: 120
Yeah! You identified the number
Do you want to continue playing?(y/n) n
Thank You!
'''