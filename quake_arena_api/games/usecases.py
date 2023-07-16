import json

from fastapi import Depends
from typing import Annotated

from games.schemas import GameOut


with open('games_results.json', 'r') as database:
    games = None
    data = database.read()

    if data:
        games = json.loads(data)


class GameUseCase:
    async def get(self, name: str) -> GameOut:
        for game in games:
            if game.get(name):
                return GameOut(**game[name])
        raise KeyError


GameUseCaseDependency = Annotated[GameUseCase, Depends()]
