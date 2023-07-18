import pytest


@pytest.fixture
def game_data():
    return {
        'total_kills': 0,
        'players': ['player_1', 'player_2'],
        'kills': {'player_1': 0, 'player_2': 0},
    }
