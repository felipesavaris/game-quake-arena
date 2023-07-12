class Game:
    def __init__(self, number: int = 0) -> None:
        self.game: str = f'game_{number}'
        self.total_kills: int = 0
        self.players: list[str] = []
        self.kills: dict = {}
