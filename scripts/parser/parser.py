import json
from typing import Any

from scripts.parser.models import Game
from scripts.parser.utils import (
    add_players,
    update_players_kills,
    increment_total_kills,
)


data_objects = []


def _stores_running_data(game: Game) -> list[dict]:
    data = vars(game)

    if data.get('game'):
        key = data['game']
        del data['game']

        game_data = {
            key: data,
        }

        data_objects.append(game_data)

    return data_objects


def _save_games(games: list[dict]) -> None:
    with open('games_results.json', 'w') as database:
        json.dump(games, database)


def _parser_game_event_actions(log_file) -> list[dict[str, Any]]:
    game_number = 0
    game, all_games = None, None

    for log in log_file:
        if 'InitGame' in log:
            game_number += 1
            game = Game(number=game_number)

        if 'Kill:' in log:
            round_players = []

            split_log = log.split(': ')
            action = split_log[-1]

            killer = action.split(' killed ')[0]
            round_players.append(killer)

            action_split = action.split(' killed ')
            deceased = action_split[1].split(' by ')[0]
            round_players.append(deceased)

            add_players(players=round_players, game=game)

            update_players_kills(players=round_players, game=game)

            increment_total_kills(game=game)

        if game:
            all_games = _stores_running_data(game)
            _save_games(games=all_games)

    return all_games


if __name__ == '__main__':
    print('Starting script!')

    log_file = open('games.log', 'r')

    _parser_game_event_actions(log_file)

    print('Parser successfully executed! See the games_results.json file.')
