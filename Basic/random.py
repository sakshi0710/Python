import  random

comp = random.randint(1,100)

print("Guess any number!!! see if you can guess the computer generated number!!")
guess= int(input("enter the number you want to guess:"))
b= True
while b:
    if (comp == guess):
        print("congrats you guessed the right number", comp)
        break
    else:
        if comp>guess:
            print("Your guess is too LOW")
            print("Would you like to guess again")
            s= input("enter the Y/N:")
            if s=="Y":
                guess=int(input("enter the number you want to guess:"))
            elif s=="N":
                print("computer generated number is:", comp)
                break
            else:
                print("invalid input")

        else:
            print("Your guess is too HIGH")
            print("Would you like to guess again")
            s = input("enter the Y/N:")
            if s == "Y":
                guess = int(input("enter the number you want to guess:"))
            elif s == "N":
                print("computer generated number is:", comp)
                break
            else:
                print("invalid input")


print("thanks for playing with us!!! enjoy")
