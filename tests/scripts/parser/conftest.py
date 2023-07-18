import pytest

from scripts.parser.models import Game
from scripts.parser.utils import add_players


@pytest.fixture
def fake_initial_game():
    return Game(number=1)


@pytest.fixture
def players():
    return ['player_1', 'player_2']


@pytest.fixture
def game_1(players):
    game = Game(number=1)
    add_players(players=players, game=game)
    return game
