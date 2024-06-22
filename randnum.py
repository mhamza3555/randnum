import random

start = int(input("Enter the first number of the range: "))
end = int(input("Enter the ending number: "))

random_num = random.randint(start, end)

while True:
    guess = int(input("Enter the guessed number"))
    if guess == random_num:
        print("Correct answer")
        print(f"The random number generated was:",  {random_num})

    else:
        print("try again.")
