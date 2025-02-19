import random

jackpotnum=random.randint(1,100)

guessnum=int(input("Enter Your guess number"))

count=1

while guessnum!=jackpotnum:
    if guessnum<jackpotnum:
        print("guess the higher lower ")
    else:
        print('Guess the number lower')
    count+=1
    guessnum=int(input("Guess the number again"))
print('Right answer')
print("Total number of guess counnt is",count)