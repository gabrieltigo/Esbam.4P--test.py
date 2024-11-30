import pytest
import requests

BASE_URL = "https://dog.ceo/api"

# API 1 - Retorna informações sobre cães de raça de grande porte
def get_large_breeds():
    """
    Retorna uma lista de raças grandes para os testes.
    """
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    breeds = response.json()["message"]
    large_breeds = ["mastiff", "newfoundland"]  # Adicione outras raças aqui.
    return [breed for breed in large_breeds if breed in breeds]

@pytest.mark.parametrize("breed", get_large_breeds())
def test_successful_breed_images(breed):
    """
    Teste de sucesso: Verifica se a API retorna status code 200 ao buscar imagens de uma raça específica.
    """
    response = requests.get(f"{BASE_URL}/breed/{breed}/images")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert "message" in response.json(), "Expected 'message' key in response"
    assert isinstance(response.json()["message"], list), "Expected 'message' to be a list of URLs"

# 2 API TESTE - oferece informações sobre países com leis de condenação rigorosa
BASE_URL_COUNTRIES = "https://restcountries.com/v3.1"

def test_country_strict_laws():
    """
    Teste de sucesso: Verifica se a API retorna informações de países, simulando busca por leis rígidas.
    """
    countries_to_test = ["Saudi Arabia", "Singapore", "Iran"]
    for country in countries_to_test:
        response = requests.get(f"{BASE_URL_COUNTRIES}/name/{country}")
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
        data = response.json()
        assert isinstance(data, list) and len(data) > 0, "Expected at least one country in the response"
        assert data[0]["name"]["common"] == country, f"Expected {country} but got {data[0]['name']['common']}"

def test_country_not_found():
    """
    Teste de erro: Verifica se a API retorna erro ao buscar um país inexistente.
    """
    response = requests.get(f"{BASE_URL_COUNTRIES}/name/NonExistentCountry")
    assert response.status_code == 404, f"Expected 404 but got {response.status_code}"
    assert "message" in response.json(), "Expected 'message' key in response"
    assert response.json()["message"] == "Not Found", "Expected 'Not Found' message"

# 3 API - Retorna informações sobre Pokémon, como características e habilidades do Arcanine
BASE_URL_POKEAPI = "https://pokeapi.co/api/v2"

def test_pokemon_arcanine_success():
    """
    Teste de sucesso: Verifica se a API retorna status code 200 ao buscar informações do Pokémon Arcanine.
    """
    response = requests.get(f"{BASE_URL_POKEAPI}/pokemon/arcanine")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    data = response.json()
    assert "name" in data and data["name"] == "arcanine", "Expected Pokémon name to be 'arcanine'"
    assert "abilities" in data, "Expected 'abilities' key in response"
    assert isinstance(data["abilities"], list), "Expected 'abilities' to be a list"

def test_pokemon_not_found():
    """
    Teste de erro: Verifica se a API retorna erro ao buscar um Pokémon inexistente.
    """
    response = requests.get(f"{BASE_URL_POKEAPI}/pokemon/nonexistentpokemon")
    assert response.status_code == 404, f"Expected 404 but got {response.status_code}"

    if response.headers.get("Content-Type") == "application/json":
        data = response.json()
        assert "detail" in data, "Expected 'detail' key in response"
        assert data["detail"] == "Not found.", "Expected 'Not found.' message in response"
    else:
        assert response.text == "Not Found", "Expected plain text 'Not Found'"

def test_pokemon_arcanine_ability_check():
    """
    Verificação de dados: Valida se Arcanine possui habilidades específicas.
    """
    response = requests.get(f"{BASE_URL_POKEAPI}/pokemon/arcanine")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    data = response.json()
    abilities = [ability["ability"]["name"] for ability in data["abilities"]]
    expected_abilities = ["intimidate", "flash-fire", "justified"]
    for ability in expected_abilities:
        assert ability in abilities, f"Expected ability '{ability}' not found in {abilities}"

# 4 API - Fornece dados sobre preços de criptomoedas e informações de mercado
BASE_URL_CRYPTOAPI = "https://api.coingecko.com/api/v3"

def test_crypto_price_success():
    """
    Teste de sucesso: Verifica se a API retorna informações de preços para uma criptomoeda válida.
    """
    crypto = "bitcoin"
    response = requests.get(f"{BASE_URL_CRYPTOAPI}/simple/price?ids={crypto}&vs_currencies=usd")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    
    data = response.json()
    assert crypto in data, f"Expected '{crypto}' in response but got {data}"
    assert "usd" in data[crypto], "Expected 'usd' price in response data"

def test_crypto_price_invalid():
    """
    Teste de erro: Verifica se a API retorna erro ao buscar uma criptomoeda inexistente.
    """
    crypto = "nonexistentcrypto"
    response = requests.get(f"{BASE_URL_CRYPTOAPI}/simple/price?ids={crypto}&vs_currencies=usd")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    
    data = response.json()
    assert crypto not in data, f"Expected no data for '{crypto}', but got {data}"

def test_crypto_market_data_success():
    """
    Teste de sucesso: Verifica se a API retorna dados de mercado para uma criptomoeda válida.
    """
    crypto = "ethereum"
    response = requests.get(f"{BASE_URL_CRYPTOAPI}/coins/{crypto}")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    
    data = response.json()
    assert "id" in data and data["id"] == crypto, "Expected correct crypto ID in response"
    assert "market_data" in data, "Expected 'market_data' in response"

def test_crypto_market_data_invalid():
    """
    Teste de erro: Verifica se a API retorna erro ao buscar dados de mercado para uma criptomoeda inexistente.
    """
    crypto = "fakecrypto"
    response = requests.get(f"{BASE_URL_CRYPTOAPI}/coins/{crypto}")
    assert response.status_code == 404, f"Expected 404 but got {response.status_code}"
    
    data = response.json()
    assert "error" in data, f"Expected 'error' in response, but got {data}"

# 5 API - Fornece informações sobre séries, incluindo enredo e classificação.
BASE_URL_SERIESAPI = "http://www.omdbapi.com"
API_KEY = "376680ac"  # chave de API

def test_series_brasileiras_info_success():
    """
    Teste de sucesso: Verifica se a API retorna informações sobre séries brasileiras.
    """
    imdb_ids = {
        "O Mecanismo": ("tt6873658", ["The Mechanism"]),
        "Coisa Mais Linda": ("tt8001788", ["Coisa Mais Linda", "Girls from Ipanema"]),
        "A Grande Família": ("tt0281447", ["A Grande Família", "Big Family"]),
    }
    for series_title, (imdb_id, acceptable_titles) in imdb_ids.items():
        response = requests.get(f"{BASE_URL_SERIESAPI}/?i={imdb_id}&apikey={API_KEY}")
        print(f"Response for {series_title}: {response.json()}")  # Log para depuração
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

        data = response.json()
        assert data["Response"] == "True", f"Expected 'True' in response but got {data}"

        # Verificar se o título está na lista de títulos aceitáveis
        if data["Title"] not in acceptable_titles:
            print(f"Inconsistência para {series_title}: {data}")  # Log adicional
        assert data["Title"] in acceptable_titles, (
            f"Expected one of {acceptable_titles} but got '{data['Title']}'"
        )

def test_series_brasileiras_info_error():
    """
    Teste de erro: Verifica se a API retorna erro ao buscar informações para um título inexistente.
    """
    response = requests.get(f"{BASE_URL_SERIESAPI}/?i=nonexistentseries&apikey={API_KEY}")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    data = response.json()
    assert data["Response"] == "False", f"Expected 'False' in response but got {data['Response']}"
    assert "Error" in data, "Expected 'Error' key in response"
