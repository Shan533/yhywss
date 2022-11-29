from expense import calculate_mileage, get_actual_mileage_rate, \
                    get_actual_trip_cost, get_reimbursement_amount
from pytest import approx


def test_calculate_mileage():
    assert (calculate_mileage(106, 110) == 4)


def test_get_actual_mileage_rate():
    assert (get_actual_mileage_rate(30, 4.68) == 0.1560)


def test_get_actual_trip_cost():
    assert (get_actual_trip_cost(106, 110, 30, 4.68) == 0.62)


def test_get_reimbursement_amount():
    assert (get_reimbursement_amount(20) == 11.50)
