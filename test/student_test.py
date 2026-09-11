import pytest
from src.students.student_name import get_student_name


@pytest.mark.parametrize("name, expected", [
    ("John", "John"),
    ("Alice", "Alice"),
    ("Bob123", "not a name"),
    ("", "not a name"),
    ("Mary-Jane", "not a name")
])


def test_get_student_name(name, expected):
    assert get_student_name(name) == expected

