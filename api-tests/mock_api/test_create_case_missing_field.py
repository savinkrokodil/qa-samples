from mock_api.claimer_api import create_case

def test_create_case_missing_field():
    data = {
        # "trusteeInn" — пропущено
        "complainerType": "1",
        "text": "Обращение без INN"
    }
    response = create_case(data)
    assert response.status_code == 400
