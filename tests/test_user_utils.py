from user_utils import is_adult
import pytest


def test_adult_user(adult_user):
    assert is_adult(adult_user)

def test_minor_user(minor_user):
    assert not is_adult(minor_user)

def test_adult_user_exactly_18():
    user = {"name": "Alice", "age": 18}
    assert is_adult(user)

@pytest.mark.parametrize("age, expected", [
    (30, True),
    (15, False),
    (18, True),
    (17, False),
    (50, True),
    (0, False),
    (100, True)
])
def test_is_adult(age, expected):
    user = {"name": "Test User", "age": age}
    assert is_adult(user) == expected

def test_user_with_cleanup(user_with_cleanup):
    assert user_with_cleanup["age"] == 30
    