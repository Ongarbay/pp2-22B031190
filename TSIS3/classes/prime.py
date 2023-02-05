def filter_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append(x)
primes = list(filter(filter_prime, l))
print(primes)
