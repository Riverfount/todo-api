def test_main_status_code_200_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_main_return_message(client):
    response = client.get('/')
    assert response.json() == {'message': 'Opa, tá funcionando. Estamos respondendo da raiz da API!!!'}
