# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?


def is_prime(n):

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n**0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


prime_factors = []
n = 600851475143

for i in range(int(n**0.5 + 1)):
    if is_prime(i) and n % i == 0:
        prime_factors.append(i)

print(prime_factors[-1])
