number = random.randrange(1, 11)  # 1-15
print("I'm thinking of a number from 1 to 10. ")
guess = int(input("Your guess: "))

if guess != number: 
    print(f"Sorry, but I was really thinking of {number}. ")
elif guess == number: 
    print(f"That's right!  My secret number was {number}! ")
