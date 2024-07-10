#Guess a number game
#Want the user to guess a number
#If they guess right, you win will be diplays
#If they guess wrong they will get 2 more chances


guess_count= 0
correct_num = 9

while guess_count < 3:
    guess_number=input("Guess: ")
    guess_count+=1
    if int(guess_number) == correct_num:
        print("You win")
        break
else:
    print("You are a loser")

        