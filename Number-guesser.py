import random 

top_of_rang = input("Type a number : ")

if top_of_rang.isdigit() :
    top_of_rang = int(top_of_rang)

    if top_of_rang == 0:
        print("Enter a number larger than 0 next time !")
        quit()
else:
    print("Enter a number next time !")
    quit()  

random_no = random.randint(0,top_of_rang)

guesses =0
while True :
    guesses += 1
    user_guess = input("Guess a number : ")
    if user_guess.isdigit() :
        user_guess = int(user_guess)
    else :
        print("Please enter a digit !")    
        continue

    if user_guess == random_no :
        print("You Got It !!!")
        break
    elif user_guess > random_no :
            print("You were above the number !")
    else :
            print("You were below the number !")    
            

print("You got it on " , guesses , " guesses")