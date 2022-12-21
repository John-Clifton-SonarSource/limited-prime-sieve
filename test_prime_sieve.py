import prime_sieve as p

def test_is_prime():
    assert p.is_prime(2) == True
    assert p.is_prime(5) == True
    assert p.is_prime(10) == False

def test_complex_code():
    p.complex_code(1,7,6,5,4,3,2)
    p.complex_code(2,7,6,5,4,3,2)
    p.complex_code(3,7,6,5,4,3,2)
    p.complex_code(4,7,6,5,4,3,2)
    p.complex_code(5,7,6,5,4,3,2)
    p.complex_code(6,7,6,5,4,3,2)
    p.complex_code(7,7,6,5,4,3,2)

    p.complex_code2(1,7,6,5,4,3,2)
    p.complex_code2(2,7,6,5,4,3,2)
    p.complex_code2(3,7,6,5,4,3,2)
    p.complex_code2(4,7,6,5,4,3,2)
    p.complex_code2(5,7,6,5,4,3,2)
    p.complex_code2(6,7,6,5,4,3,2)
    p.complex_code2(7,7,6,5,4,3,2)

