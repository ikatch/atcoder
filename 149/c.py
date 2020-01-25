def is_prime(x):
    if x <= 1:
        return False

    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True


x = int(input())

p = x

while not is_prime(p):
    p += 1

print(p)
