import pytest

@pytest.fixture
def adult_user():
    return {"name": "Peter",
            "age": 30}

@pytest.fixture
def minor_user():
    return {"name": "John",
            "age": 15}

@pytest.fixture
def user_with_cleanup():
    print("Creating user")
    user_data = {"name": "Peter", "age": 30}
    yield user_data
    print("Deleting user")