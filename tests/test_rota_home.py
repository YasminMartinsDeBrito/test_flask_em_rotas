from app import app

# Retornando o test client do nosso app
def app_client():
    return app.test_client()

def test_status_code_rota_home():
    # Pegando o retorno da nossa função app_client()
    client = app_client()

    response = client.get("/")
    # Testando se o status HTTP do retorno é igual ao esperado
    assert response.status_code == 200, "Status incorreto"

def test_json_response_rota_home():
    client = app_client()
    response = client.get("/")

    # resposta esperada
    expected_dict = {"message": "meu primeiro teste com flask!"}

    # Testando se o retorno é um dicionario
    assert type(response.get_json()) is dict, "Não retornou dicionario"

    # testando se o dicionario retornado é igual ao esperado
    assert response.get_json() == expected_dict, "Retorno incorreto"


    # links
    # test client =https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_client
    #  gettin started = https://docs.pytest.org/en/6.2.x/getting-started.html