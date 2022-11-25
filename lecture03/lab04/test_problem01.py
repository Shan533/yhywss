from problem01 import calculate_total_bill, calculate_bill_per_person
from pytest import approx


def test_calculate_total_bill():
    approx(calculate_total_bill(100, 0.15) == 115)
    assert (calculate_bill_per_person(90, 6) == 15)
