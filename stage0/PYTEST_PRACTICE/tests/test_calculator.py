from calculator import add, multiply, divide
import pytest


def test_add():
    result = add(10, 20)
    assert result == 30

@pytest.mark.parametrize(
        "a, b, expected",
        [
            (5,5,25),
            (3,4,12),
            (5,0,0),
            (-4,7, -28),
            (-4,-4,16)

        ])
def test_multiply(a,b,expected):
    result = multiply(a, b)
    assert result == expected



def test_divide():
    result=divide(10,2)
    assert result == 5

    with pytest.raises(ValueError):
        divide(10,0)

