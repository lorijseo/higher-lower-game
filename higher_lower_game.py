from game_data import data
from art import logo
from art import vs
import random


def compare(a, b):
    """compares the number of instagram followers between person_a and person_b"""
    if a > b:
        return "A"
    elif a < b:
        return "B"


def display():
    """displays person_a and person_b before user input"""
    print(f"Compare A: {person_a['name']}, a {person_a['description']} from {person_a['country']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']} from {person_b['country']}.")


def take_guess():
    """allows user to input their guess"""
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    return guess


score = 0
game = True

people_list = random.sample(data, 2)
print(logo)

while game:
    person_a = people_list[0]
    person_b = people_list[1]
    followers_a = person_a["follower_count"]
    followers_b = person_b["follower_count"]
    display()
    answer = take_guess()
    if answer == compare(followers_a, followers_b):
        score += 1
        print(f"You're right! Current score: {score}\n")
        people_list[0] = person_b
        people_list[1] = random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False
