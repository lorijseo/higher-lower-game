from game_data import data
from art import logo
from art import vs
import random


def compare(a, b):
    if a > b:
        return "A"
    elif a < b:
        return "B"
    else:
        return "A"


def display():
    print(logo)
    print(f"Compare A: {person_a['name']}, a {person_a['description']} from {person_a['country']}.")
    print(vs)
    second_person = random.choice(data)
    if person_a == second_person:
        second_person = random.choice(data)
    print(second_person["follower_count"])
    print(f"Against B: {second_person['name']}, a {second_person['description']} from {second_person['country']}.")
    return second_person


def take_guess():
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    return guess


score = 0
game = True
person_a = random.choice(data)
followers_a = person_a["follower_count"]


while game:
    person_b = display()
    answer = take_guess()
    if answer == compare(followers_a, person_b["follower_count"]):
        score += 1
        person_a = person_b
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False
