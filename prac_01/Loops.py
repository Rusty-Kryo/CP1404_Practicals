"""
Loops practical, for week 1
"""
print("""Loop 1""")
#first loop
for i in range(1, 21, 2):
    print(i, end=' ')

print("""
Loop 2""")

#second loop
for i in range(0, 110, 10):
    print(i, end=' ')
print("""
Loop 3""")
#third loop
for i in range(20, 0, -1):
    print(i, end=' ')
print("""
Loop 4""")
#fourth loop
n = int(input("# of Stars:"))
for i in range(0, n, 1):
    print('*', end=' ')
print("""
Loop 5""")
#fifth loop
n = int(input("# of Stars:"))
for i in range(0, n, 1):
    print('*' * (i+1))

