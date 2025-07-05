"""
Birthday Paradox

What is the probability that at least two people in a group of n random people
have the same birthday?

Intuitively, we believe that this chance is low when the group is small, such
as 23 people, but the real probability is approximately 50.7%.

This code estimates the probability that at least two people share the same
birthday in a group of n given people.
"""
from random import randint

MAX_PEOPLE = 100
SIMULATIONS = 100000


def main():
    while True:
        try:
            sample_size: int = int(input(f"How many birthdays will I generate? (Max {MAX_PEOPLE})\n> "))
            if 0 < sample_size <= MAX_PEOPLE:
                break
        except ValueError:
            pass

    print(f"{sample_size} people have {simulate(sample_size)}% change of having a\nmatching birthday in their group.")


def generate_birthdays(sample_size: int) -> list:
    return [randint(1, 365) for _ in range(sample_size)]


def has_duplicate(birthdays: list) -> bool:
    seen: set = set()

    for birthday in birthdays:
        if birthday in seen:
            return True

        seen.add(birthday)

    return False


def simulate(sample_size: int) -> float:
    count: int = 0

    for simulation in range(1, SIMULATIONS + 1):
        birthdays = generate_birthdays(sample_size)
        if has_duplicate(birthdays):
            count += 100
        print(f"\r{simulation}", end="")

    print(" simulations made.")

    return count / SIMULATIONS


if __name__ == "__main__":
    main()
