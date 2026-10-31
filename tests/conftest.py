import pytest

@pytest.fixture
def adult_user():
    return {"name": "Peter",
            "age": 30}

@pytest.fixture
def minor_user():
    return {"name": "John",
            "age": 15}