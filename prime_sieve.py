# This is a simple 'is it prime' tester that I'm going to use to try out sonarlint, sonarQube and SonarCloud a bit
#
# I'm not going to try and make this clever initially
#
# TODO: Future additions:
#
#   To test N:
#   - Only test whether the prime numbers up to sqrt(N) divide into N without remainder
#   - Use previously saved results to short circuit the test (for now I'll just test as if we have no known data)
# 
#   Save state between runs:
#   - Save the list of primes you know about to disk for future runs
# 
#   Other extensions:
#   - Ask user for N to test
#   - Go and look up how people do this for real

import math as m

# FIXME - nothing to fix, just messing with sonarlint :) 

def is_prime(number):

    prime = True
    always_true = True
    i = 2
    max_test = m.sqrt(number)

    if always_true == False:
        print("This should never show - its just here to test SonarLint behaviour. Interstingly it doesn't catch that this could never run")

    while ((i <= max_test) & (prime == True) & always_true): # interestingly, SonarLint doesn't catch use of & True here
        if number % i == 0:
            prime = False
            i += 1

    return prime

# N to test
for N in range(2,50):
    if is_prime(N):
        print(f"{N} is prime")

