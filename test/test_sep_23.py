import pytest

from src.daily_task.sep_23 import calculate_sum


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([20, 30, 40], 90),
        ([10, 20], 30),
        ([5, 5, 5], 15),
        ([100, 200], 300),
    ],
)
def test_calculate_sum(numbers, expected):
    assert calculate_sum(numbers) == expected