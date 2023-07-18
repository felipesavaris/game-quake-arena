import pytest
from pytest_mock import MockerFixture

from quake_arena_api.games.schemas import GameOut
from quake_arena_api.games.controller import router
from quake_arena_api.games.usecases import GameUseCase, GameCollectionResponse
from quake_arena_api.main import app as _app


@pytest.fixture
def game_data():
    return {
        'total_kills': 0,
        'players': ['player_1', 'player_2'],
        'kills': {'player_1': 0, 'player_2': 0},
    }


@pytest.fixture
def games_mock():
    return [
        {'game_1': {'total_kills': 0, 'players': [], 'kills': {}}},
        {
            'game_2': {
                'total_kills': 11,
                'players': ['Isgalamido', 'Mocinha'],
                'kills': {'Isgalamido': -7, 'Mocinha': 0},
            }
        },
    ]


@pytest.fixture
def app():
    _app.include_router(router)

    return _app


@pytest.fixture
async def mock_usecase_get(mocker: MockerFixture):
    return mocker.patch.object(
        GameUseCase,
        'get',
        return_value=GameOut(**{'kills': {}, 'players': [], 'total_kills': 0}),
    )


@pytest.fixture
async def mock_usecase_query(mocker: MockerFixture):
    games = [
        {'game_1': GameOut(**{'total_kills': 0, 'players': [], 'kills': {}})}
    ]

    collection = GameCollectionResponse(results=games)

    return mocker.patch.object(
        GameUseCase,
        'query',
        return_value=collection,
    )
