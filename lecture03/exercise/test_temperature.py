from temperature import fahrenheit_to_celsius
from pytest import approx


def test_fahrenheit_to_celsius():

    # assert (fahrenheit_to_celsius(32) == 0)
    # assert (fahrenheit_to_celsius(0) == -17.78)
    # assert (fahrenheit_to_celsius(-143.5) == -97.5)
    # assert (fahrenheit_to_celsius(50) == 0)
    approx(fahrenheit_to_celsius(33) == -17.78)
