"""
Code for quick pick lottery generator

- asks the user for a number which dictates
how many quick picks are generated

"""
import random
number_range = [num for num in range(1, 46)]
def main():
    qp = []
    num_of_qp = int(input("How many quick picks do you want? : "))
    for i in range(0, num_of_qp):
        generated_qp = qp_generator()
        sorted_qp = sorted(generated_qp)
        qp.append(sorted_qp)
    line_print(qp)
def qp_generator():
    qp = random.sample(number_range, 6)
    return qp

def line_print(qp):
    for line in qp:
        print(f"{line[0]:3} {line[1]:3} {line[2]:3} {line[3]:3} {line[4]:3} {line[5]:3}")

main()