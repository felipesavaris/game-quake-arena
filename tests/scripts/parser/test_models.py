from scripts.parser.models import Game


def test_parse_models_retuns_new_game(fake_initial_game):
    game = Game(number=1)

    assert vars(game) == vars(fake_initial_game)
