from hangman import progress_checker, length_checker, games, letter_checker


def test_progress_checker():
    assert progress_checker("P", "APPLE") == "P"
    assert progress_checker("L", "APPLE") == "L"


def test_length_checker():
    assert length_checker("banana")
    assert not length_checker("f")


def test_letter_checker():
    assert letter_checker("D", "DOG", "___") == "D__"
    assert letter_checker("G", "DOG", "___") == "__G"
