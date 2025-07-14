import pytest

@pytest.fixture(scope="session")
def sample_data():
    return {
        "trusteeInn": "1234567890",
        "complainerType": "1",
        "text": "Пример обращения"
    }
