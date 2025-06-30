URL = "/grade"


def test_post_grade_not_superuser(test_client):
    data_one = {"title": "менеджер", "selary": 10000}
    response = test_client.post(URL, json=data_one)
    assert response.status_code == 403, (
        "При запросе на изменение грейда от обычного "
        "пользователя ожидается код 401"
    )


def test_post_grade_superuser(super_user_client):
    data_one = {"title": "менеджер", "selary": 10000}
    response = super_user_client.post(URL, json=data_one)
    assert response.status_code == 200, (
        "При запросе на изменение грейда от обычного пользователя "
        "ожидается код 401"
    )
