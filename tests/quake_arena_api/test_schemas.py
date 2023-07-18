from quake_arena_api.games.schemas import GameCollectionResponse, GameOut


def test_api_schemas_parse_obj_game_out(game_data):
    game = GameOut.model_validate(game_data)

    assert game.total_kills == game_data['total_kills']
    assert game.players == game_data['players']
    assert game.kills == game_data['kills']


def test_api_schemas_parse_obj_game_collection_response(game_data):
    all_games = {
        'results': [
            {
                'game_1': game_data,
                'game_2': game_data,
            }
        ]
    }

    game_collection = GameCollectionResponse.model_validate(all_games)
    results = game_collection.results[0]

    assert vars(results['game_1']) == all_games['results'][0]['game_1']
    assert vars(results['game_2']) == all_games['results'][0]['game_2']
