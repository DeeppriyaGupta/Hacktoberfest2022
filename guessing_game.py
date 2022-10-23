import random

a=random.randint(1,100)
c=input("Easy or Difficult: ")
if c=="easy" or c=="EASY" or c=="Easy":
    for i in range(10):
            b=int(input("Enter your guess: "))
            if a==b:
                print("you guessed right number")
                ans=f"You guessed the right number in {i+1} times"
                break
            elif i==9 and b!=a:
                ans='you lost'
                break
            elif b>a:
                print("you guessed large number, try again. You have", 9-i, "attempt left.")
            else:
                
                print("you guessed small number, try again. You have", 9-i, "attempt left.")
                
            
    print(ans)

else:
    for i in range(5):
            b=int(input("Enter your guess: "))
            if a==b:
                print("you guessed right number")
                ans=f"You guessed the right number in {i+1} times"
                break
            elif i==4 and b!=a:
                ans='you lost'
                break
            elif b>a:
                print("you guessed large number, try again. You have", 4-i, "attempt left.")
            else:
                
                print("you guessed small number, try again. You have", 4-i, "attempt left.")
                
            
    print(ans)