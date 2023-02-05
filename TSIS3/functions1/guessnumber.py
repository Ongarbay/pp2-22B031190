import random
number = random.randint(1, 20)
tries = 1
print("Hello! What is your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
g = "Take a guess."
print(g)
n = int(input())
while (n != number):
    if (n < number):
        print("Your guess is too low.")
    elif (n > number):
        print("Your guess is too high.")
    print(g)
    tries += 1
    n = int(input())

print(f"Good job, {name}! You guessed my number in {tries} guesses!")
