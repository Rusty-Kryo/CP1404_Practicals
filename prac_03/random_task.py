"""
1.  What did you see on line 1?
        - number ranging from 5 and 20
    What was the smallest number
    you could have seen, what was the largest?
        - the lowest value was 5 and the highest value was 20

2.  What did you see on line 2?
        - numbers 3, 5, 7 and 9
    What was the smallest number you could have seen,
    what was the largest?
        - 9
    Could line 2 have produced a 4?
        - No, because since the lower limit is 3 and
        the step is 2.

3.  What did you see on line 3?
        - numbers within 2.5 and 5.5
    What was the smallest number you could have seen,
    what was the largest?
        - smallest is 2.5 and largest is 5.5

4.  Write code, not a comment, to produce a random
    number between 1 and 100 inclusive.
"""

import random
q = True
while q == True:
    a = random.randint(5,20)  # line 1
    b = random.randrange(3, 10, 2)  # line 2
    c = random.uniform(2.5,5.5)  # line 3
    d = random.randint(1, 100)  # line 4 for question 4

    print(a)
    print(b)
    print(c)
    print(d)

    if b == 4:
        q = False