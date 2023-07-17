from fastapi import FastAPI

from quake_arena_api.games.controller import router


app = FastAPI(
    title='Quake Arena API', description='Game query API', version='0.0.1'
)
app.include_router(router=router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('quake_arena_api.main:app', reload=True)
