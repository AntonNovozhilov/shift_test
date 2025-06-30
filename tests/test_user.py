URL = "/users/{id}"


def test_upgrade_user_not_superuser(test_client, user_two):
    user = user_two
    data = {"grade_id": 1}
    response = test_client.patch(URL.format(id=user.id), json=data)
    assert response.status_code == 403, (
        "При запросе на изменение грейда от "
        "обычного пользователя ожидается код 403"
    )


def test_upgrade_user(super_user_client, user_one):
    user = user_one
    data = {"grade_id": 1}
    response = super_user_client.patch(URL.format(id=user.id), json=data)
    assert (
        response.status_code == 200
    ), "При запросе на изменение грейда от супер пользователя ожидается код 200"
