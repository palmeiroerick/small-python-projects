"""
Bagels, A Deductive Logic Game

Guess a secret number based on clues.

Rules:
    The secret number has three unique digits.
    You have 10 guesses to find it.
    After each guess, you'll receive one or more hints based on the digits of your guess.

Hints:
    Pico   -> One digit is correct but in the wrong position.
    Fermi  -> One digit is correct and in the right position.
    Bagels -> No digit is correct.
"""
from random import sample

digits: list = sample(range(0, 10), 3)
got_it = False

for count in range(1, 11):
    guess_digits: str = ""

    while len(guess_digits) != 3 or not guess_digits.isdigit():
        guess_digits: str = input(f"\nGuess #{count}:\n> ")

    guess: list = [int(digit) for digit in guess_digits]

    if guess == digits:
        got_it = True
        break

    clues: list = [] 

    for i, digit in enumerate(guess):
        if guess[i] == digits[i]:
            clues.append("Fermi")
            continue

        if digit in digits:
            clues.append("Pico")
            continue

    if not clues:
        clues.append("Bagels")

    for clue in clues:
        print(clue, end=" ")

    print()

if got_it:
    print("You got it!")
else:
    print("\nAnswer: ", end="")

    for digit in digits:
        print(digit, end="")

    print()
