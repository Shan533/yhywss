
def fahrenheit_to_celsius(temp_in_f):
    TEMP_MULTIPLIER = 5/9
    TEMP_SLIDE = 32

    return TEMP_MULTIPLIER * (temp_in_f-TEMP_SLIDE)
