import pytest
from src.arthimetic_operation.additional import addition
from src.students.student_name import get_student_name

@pytest.mark.parametrize(
    "name,expected",
    [
        ("John", "John"),
        ("Alice", "Alice"),
        ("Bob123", "not a name"),
        ("", "not a name"),
        ("Mary-Jane", "not a name")
    ]
)


def test_get_student_name(name, expected):
    assert get_student_name(name) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (-5, -5, -10),
        

    ]
)

    
def test_addition_parameterized(a, b, expected):
    assert addition(a, b) == expected

    