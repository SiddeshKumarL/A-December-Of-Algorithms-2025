n = int(input('Enter N:').strip())
if n <= 2:
    print(f"The count of prime numbers less than {n} is: 0")
else:
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p < n:
        if is_prime[p]:
            for m in range(p * p, n, p):
                is_prime[m] = False
        p += 1
    count = sum(is_prime)
    print(f"The count of prime numbers less than {n} is: {count}")
