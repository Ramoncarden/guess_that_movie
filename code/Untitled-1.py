import random

num = random.randint(1, 10)
guess = int(input("Guess a number between 1-10: "))

while num != guess:
print("sorry")
guess = int(input("Guess a number between 1-10: "))
if num == guess:
print("thats it!")

def happy(car):
print("ya")

