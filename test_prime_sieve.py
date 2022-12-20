import prime_sieve as p

def test_is_prime():
    assert p.is_prime(2) == True
    assert p.is_prime(5) == True
    assert p.is_prime(10) == False

