from models import Game


def _validate_player_exists(player: str, game: Game) -> bool:
    if player in game.players:
        return True
    return


def _add_player_kills_stucture(name: list[str], game: Game) -> None:
    if name in game.players or name == '<world>':
        return

    game.players.append(name)
    game.kills.update({f'{name}': 0})


def _increment_kills(player: str, game: Game) -> None:
    if (player != '<world>'):
        value = game.kills.get(player)
        game.kills.update({player: int(value + 1)})


def _decrement_kills(players: list[str], game: Game) -> None:
    if players[0] == '<world>' or (players[0] == players[1]):
        value = game.kills.get(players[1])
        game.kills.update({players[1]: int(value - 1)})


def add_players(players: list[str], game: Game) -> None:
    for player in players:
        player_exists = _validate_player_exists(player, game)

        if not player_exists:
            _add_player_kills_stucture(player, game)


def update_players_kills(players: list[str], game: Game) -> None:
    _increment_kills(player=players[0], game=game)
    _decrement_kills(players=players, game=game)


def increment_total_kills(game: Game) -> None:
    game.total_kills += 1
