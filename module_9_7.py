import random


def is_prime(func):
    def wrapper(*args):
        res = func(args)
        if res % random.randint(1, res) == 0:
            return 'Составное'
        else:
            return 'Простое'
    return wrapper

@is_prime
def sum_three(*args):
    summa = 0
    for n in args:
        for i in n:
            summa += i
    print(summa)
    return summa

result = sum_three(2, 3, 6)
print(result)