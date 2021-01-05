import pytest
from romanos import numberToRoman, romanToNumber
from fizzbuzz import fizzBuzz, fizzBuzz2
from diamond import diamond

# ----- Números Romanos -----
@pytest.mark.parametrize(
    "num, output",
    [(1, "I"), (194, "CXCIV"), (1934, "MCMXXXIV")]
)
def test_numberToRoman(num, output):
    assert numberToRoman(num) == output

@pytest.mark.parametrize(
    "numeral, output",
    [("I", 1), ("CXCIV", 194), ("MCMXXXIV", 1934)]
)
def test_romanToNumber(numeral, output):
    assert romanToNumber(numeral) == output

# ----- Fizzbuzz -----
@pytest.mark.parametrize(
    "n, output",
    [
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]) ]
)
def test_fizzBuzz(n, output):
    assert fizzBuzz(n) == output

@pytest.mark.parametrize(
    "n, output",
    [
        (13, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "Fizz"]),
        (23, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', 'Fizz', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', 'Fizz']) ]
)
def test_fizzBuzz2(n, output):
    assert fizzBuzz2(n) == output

# ----- Diamond -----
@pytest.mark.parametrize(
    "car, output",
    [
        ('A', ["A"]),
        ('C', ["  A", " B B", "C   C", " B B", "  A"]),
        ('D', ["   A", "  B B", " C   C","D     D", " C   C", "  B B", "   A"])
    ]
)
def test_diamond(car, output):
    assert diamond(car) == output