import pytest

from src.daily_task.sep_22 import get_unique_numbers


@pytest.mark.parametrize("name, expected", [
    (
        "123 sd d34 5 65 6436 3452 dsad46 5 62 wer6 45 5 66",
        [5, 45, 62, 65, 66, 123, 3452, 6436]
    ),
    (
        "10 20 30 20 10",
        [10, 20, 30]
    ),
    (
        "5 abc 5 xyz 10",
        [5, 10]
    ),
    (
        "100 50 25",
        [25, 50, 100]
    ),
    (
        "abc xyz hello",
        []
    )
])
def test_get_unique_numbers(name, expected):
    assert get_unique_numbers(name) == expected