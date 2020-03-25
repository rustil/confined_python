def primes(max_num):
    # Only primes smaller than max_num are calculated
    is_prime = max_num * [True]
    is_prime[0] = False
    is_prime[1] = False

    primes = []

    # Sieve of Erathosthenes:
    for i in range(2, max_num):
        if is_prime[i]:
            for j in range(2 * i, max_num, i):
                # Multiples are not primes
                is_prime[j] = False
            primes.append(i)
    
    return primes

print(primes(100))