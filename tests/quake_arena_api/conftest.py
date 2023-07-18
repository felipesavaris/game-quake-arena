import pytest


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
