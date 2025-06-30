import pytest

URL = "/auth/register"


def test_register(not_auth_test_client):
    data = {
        "email": "example1@example.com",
        "password": "exampleexampleexample",
    }
    data_with_grade = {
        "email": "example1_whis_grade@example.com",
        "password": "exampleexampleexample",
        "grade_id": 1,
    }
    response = not_auth_test_client.post(URL, json=data)
    response_grade = not_auth_test_client.post(URL, json=data_with_grade)
    assert (
        response.status_code == 201
    ), "При регистрации с валидными данными ожидается ответ со статусом 201"
    assert (
        response_grade.status_code == 201
    ), "При регистрации с валидными данными ожидается ответ со статусом 201"


@pytest.mark.parametrize(
    "email, password",
    [
        ("qwe@qwe.ru", ""),
        ("qwe1@qwe.ru", "qwe"),
        ("qwe12@qwe.ru", "qweqwe"),
    ],
)
def test_len_password(test_client, email, password):
    data = {
        "email": email,
        "password": password,
    }
    response = test_client.post(URL, json=data)
    assert (
        response.status_code == 400
    ), "Убедитесь , что пароль не может быть короче 8 символов или пустым"


@pytest.mark.parametrize(
    "email, password",
    [
        ("qwe@qwe.ru", "qwe@qwe.ru"),
    ],
)
def test_login_password(test_client, email, password):
    data = {
        "email": email,
        "password": password,
    }
    response = test_client.post(URL, json=data)
    assert (
        response.status_code == 400
    ), "Убедитесь , что пароль не может содержать логин"
