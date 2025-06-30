from datetime import datetime

from shift.core.base import User

URL = "/selary"

URL2 = "/next_advance"


def test_get_auth_selary(not_auth_test_client):
    response = not_auth_test_client.get(URL)
    assert (
        response.status_code == 401
    ), "Неавторизованный пользователь не может получить информацию к зарплате"


def test_get_selary(test_client, user_with_grade):
    response = test_client.get(URL)
    assert (
        response.status_code == 200
    ), "Авторизованный пользователь может получить информацию к зарплате"
    assert (
        "selary" in response.json()
    ), 'Удостоверьтесь , что поле зарплаты называется "selary"'


def test_advancement_date(test_client):
    response = test_client.get(URL2)
    assert response.status_code == 400, (
        "Авторизованный пользователь может получить информацию к"
        " дате следующего повышения."
    )
    assert "advancement_date" in response.json()
