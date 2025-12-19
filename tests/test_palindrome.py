import pytest
from palindrome import is_palidrome


@pytest.mark.parametrize(
    "word, expected",
    [
        ("radar", True),
        ("level", True),
        ("racecar", True),
        ("hello", False),
        ("world", False),
        ("Radar", True),
        ("Level", True),
        ("RaDaR", True),
        ("шалаш", True),
        ("довод", True),
        ("Анна", True),
        ("", True),
        ("a", True),
        (" ", True),
        ("12321", True),
        ("12345", False),
    ],
)
def test_is_palindrome_basic(word, expected):
    assert is_palidrome(word) == expected


def test_invalid_input():
    with pytest.raises(AttributeError):
        is_palidrome(123)
