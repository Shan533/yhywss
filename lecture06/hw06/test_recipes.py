from recipes import input_validation, ingredient_validation

def test_ingredient_validation():
    test_empty_list = " "
    test_good_list = "item1, item2"
    assert test_good_list ==  