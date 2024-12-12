def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        print(res)
        counter = 0
        for i in range(2, res):
            if res % i == 0:
                counter += 1

        if counter <= 0:
            return 'Простое'
        else:
            return 'Составное'
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(0, 0, 8)
print(result)
