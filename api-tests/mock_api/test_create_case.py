from mock_api.claimer_api import create_case

def test_create_case_success():
    data = {
        "trusteeInn": "1234567890",
        "complainerType": "1",
        "text": "Тестовая жалоба"
    }
    response = create_case(data)
    assert response.status_code == 200
