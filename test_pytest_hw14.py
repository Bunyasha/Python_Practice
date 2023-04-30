import pytest
from def_for_unittest_hw14 import prime_factors_of_number


def test_prime_number():
    assert prime_factors_of_number(1) == "Число является простым"

def test_composite_number():
    assert prime_factors_of_number(10) == [2, 5]

def test_not_number():
    with pytest.raises(TypeError):
        prime_factors_of_number('gfhd')
            


if __name__ == '__main__':
    pytest.main()