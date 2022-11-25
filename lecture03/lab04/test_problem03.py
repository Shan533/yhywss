from problem03 import record_day, calculate_days


def test_record_day():
    assert (record_day("tH") == "th")
    assert (calculate_days("th") == 1)
