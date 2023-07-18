import json

from fastapi import Depends
from typing import Annotated

from quake_arena_api.games.schemas import GameCollectionResponse, GameOut


async def _read_games_data():
    games = None
    with open('games_results.json', 'r') as database:
        data = database.read()

        if data:
            games = json.loads(data)

    return games


class GameUseCase:
    async def get(self, name: str) -> GameOut:
        games = await _read_games_data()

        for game in games:
            if game.get(name):
                return GameOut(**game[name])
        raise KeyError

    async def query(self) -> GameCollectionResponse:
        results = []
        games = await _read_games_data()

        for game in games:
            key = (*game,)[0]

            results.append({key: GameOut(**game[key])})

        return GameCollectionResponse(results=results)


GameUseCaseDependency = Annotated[GameUseCase, Depends()]
