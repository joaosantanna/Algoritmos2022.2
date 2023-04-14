from math import factorial
def fatorial(x):
    fat = 1
    for i in range(1,x + 1):
        fat = fat * i
    return fat

print(fatorial(50))
print(factorial(50))