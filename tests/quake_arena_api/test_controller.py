import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch


async def test_api_games_get_for_name_should_internal_server_error(app):
    client = TestClient(app)

    response = client.get('/v0/games/game_1')

    assert response.status_code == 500
    assert response.json() == {'detail': 'Internal Server Error'}


@pytest.mark.usefixtures('mock_usecase_get')
async def test_api_games_get_for_name_should_return_a_game(app):
    client = TestClient(app)

    response = client.get('/v0/games/game_1')

    assert response.status_code == 200
    assert response.json() == {'kills': {}, 'players': [], 'total_kills': 0}


async def test_api_games_get_for_name_should_return_not_found_error(app):
    with patch(
        'quake_arena_api.games.usecases._read_games_data'
    ) as mock_data_json:
        mock_data_json.return_value = []
        client = TestClient(app)
        response = client.get('/v0/games/game_')

    assert response.status_code == 404
    assert response.json() == {
        'detail': 'Object not found on Games for name: game_'
    }


@pytest.mark.usefixtures('mock_usecase_query')
async def test_api_games_get_for_name_should_return_list_of_games(app):
    client = TestClient(app)

    response = client.get('/v0/games')

    assert response.status_code == 200
    assert response.json()['results'][0] == {
        'game_1': {'kills': {}, 'players': [], 'total_kills': 0}
    }
