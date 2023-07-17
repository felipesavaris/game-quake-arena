from pydantic import BaseModel, Field


class GameOut(BaseModel):
    total_kills: int = Field(
        description='Total kills during the game', example=10
    )
    players: list[str] = Field(
        description='Participating players', example=['player1', 'player2']
    )
    kills: dict[str, int] = Field(
        description='Players and their actions',
        example={'player1': 1, 'player2': 0},
    )


class GameCollectionResponse(BaseModel):
    results: list[dict[str, GameOut]] = Field(
        description='List with information of all games',
        example=[
            {
                'game_1': {
                    'total_kills': 10,
                    'players': ['player1', 'player2'],
                    'kills': {'player1': 1, 'player2': 0},
                },
                'game_2': {
                    'game_2': 10,
                    'players': ['player1', 'player2'],
                    'kills': {'player1': 1, 'player2': 0},
                },
            }
        ],
    )
