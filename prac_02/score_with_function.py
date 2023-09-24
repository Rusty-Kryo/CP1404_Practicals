"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


#generates a menu
def main():
    score = float(input("Enter score: "))
    print("Score Status")
    #decision process
    score_decision(score)

    rand_score = random.randint(0, 101)
    score_decision(rand_score)

def score_decision(score):
    print(score)
    if score < 0:
        result = "Invalid score"
    elif score > 100:
        result = "Invalid score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    print(result)



main()