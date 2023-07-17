from fastapi import APIRouter, HTTPException, status

from quake_arena_api.games.responses import (
    InternalServerErrorResponse,
    NotFoundErrorResponse,
)
from quake_arena_api.games.schemas import GameCollectionResponse, GameOut
from quake_arena_api.games.usecases import GameUseCaseDependency


router = APIRouter(tags=['games'], prefix='/v0/games')


@router.get(
    '/{name}',
    description='Game search by name',
    status_code=status.HTTP_200_OK,
    responses={
        404: {'model': NotFoundErrorResponse},
        500: {'model': InternalServerErrorResponse},
    },
)
async def get(name: str, use_case: GameUseCaseDependency) -> GameOut:
    try:
        return await use_case.get(name=name)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Object not found on Games for name: {name}',
        )
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get(
    '',
    description='List all games',
    status_code=status.HTTP_200_OK,
    responses={500: {'model': InternalServerErrorResponse}},
)
async def query(use_case: GameUseCaseDependency) -> GameCollectionResponse:
    try:
        return await use_case.query()
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
