import pytest
from unittest.mock import patch

from quake_arena_api.games.usecases import GameUseCase
from quake_arena_api.games.schemas import GameCollectionResponse, GameOut


async def test_api_usecases_get_should_return_a_game(games_mock):
    with patch(
        'quake_arena_api.games.usecases._read_games_data'
    ) as mock_data_json:
        mock_data_json.return_value = games_mock

        game = await GameUseCase().get('game_1')

    assert isinstance(game, GameOut)
    assert vars(game) == {'total_kills': 0, 'players': [], 'kills': {}}


async def test_api_usecases_get_should_an_exception():
    with patch(
        'quake_arena_api.games.usecases._read_games_data'
    ) as mock_data_json:
        mock_data_json.return_value = None
        with pytest.raises(Exception) as exc:
            await GameUseCase().get(name='game_1')

    assert exc.value.args == ("'NoneType' object is not iterable",)


async def test_api_usecases_query_should_rerturn_games(games_mock):
    with patch(
        'quake_arena_api.games.usecases._read_games_data'
    ) as mock_data_json:
        mock_data_json.return_value = games_mock

        games = await GameUseCase().query()

    results = games.results

    assert isinstance(games, GameCollectionResponse)
    assert vars(results[0]['game_1']) == {
        'kills': {},
        'players': [],
        'total_kills': 0,
    }
    assert vars(results[1]['game_2']) == {
        'kills': {'Isgalamido': -7, 'Mocinha': 0},
        'players': ['Isgalamido', 'Mocinha'],
        'total_kills': 11,
    }
