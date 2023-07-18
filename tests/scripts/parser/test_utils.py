import pytest

from scripts.parser.utils import (
    _validate_player_exists,
    add_players,
    update_players_kills,
    increment_total_kills,
)


@pytest.mark.parametrize(
    'player_name, result', [('player_1', True), ('player_2', None)]
)
def test_parser_utils_validade_player_exists(
    player_name, result, fake_initial_game
):
    fake_initial_game.players = ['player_1']
    fake_initial_game.kills = {'player_1': 0}

    is_exists = _validate_player_exists(
        player=player_name, game=fake_initial_game
    )

    assert is_exists == result


@pytest.mark.parametrize(
    'game_players, expected_players, expected_kills',
    [
        (
            ['player_1', 'player_2'],
            ['player_1', 'player_2'],
            {'player_1': 0, 'player_2': 0},
        ),
        (['<world>', 'player_2'], ['player_2'], {'player_2': 0}),
    ],
)
def test_parser_utils_add_players(
    game_players, expected_kills, expected_players, fake_initial_game, game_1
):
    game_1.players = expected_players
    game_1.kills = expected_kills

    add_players(players=game_players, game=fake_initial_game)

    assert vars(fake_initial_game) == vars(game_1)


def test_parser_utils_update_players_kills(players, game_1):
    update_players_kills(players=players, game=game_1)

    assert vars(game_1) == {
        'game': 'game_1',
        'kills': {'player_1': 1, 'player_2': 0},
        'players': ['player_1', 'player_2'],
        'total_kills': 0,
    }


def test_parser_utils_increment_total_kills(game_1):
    increment_total_kills(game=game_1)

    assert game_1.total_kills == 1
