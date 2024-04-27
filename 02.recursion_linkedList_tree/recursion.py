# recursion demo in python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 131231


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n//10)


# 10 20
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)


print(power(2, 3))  # 8
print(power(30, 40))  # 81
