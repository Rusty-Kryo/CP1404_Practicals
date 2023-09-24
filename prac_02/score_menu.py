"""
display menu
get choice
decision for the choice
error check
display choice, and result

do final thing

"""

menu = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
>>>"""

def main():
    score = 0
    while True:
        print(menu)
        com = input().upper()
        if com == "G":
            score = int(input("Enter Score:"))
        elif com == "P":
            score_decision(score)
        elif com == "S":
            print('*' * score)
        elif com == "Q":
            break
        else:
            print(menu)

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