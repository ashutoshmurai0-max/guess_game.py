import random

number = random.randint(1, 100)
attempts = 0

print("1 se 100 ke beech ka number guess karo!")

while True:
    guess = int(input("Tumhara guess: "))
    attempts += 1

    if guess < number:
        print("Thoda bada socho 🔼")
    elif guess > number:
        print("Thoda chhota socho 🔽")
    else:
        print(f"Sahi! {attempts} attempts me guess kiya 🎉")
        break
