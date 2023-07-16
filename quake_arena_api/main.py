from fastapi import FastAPI

from games.controller import router


app = FastAPI(
    title='Quake Arena API', description='Game query API', version='0.0.1'
)
app.include_router(router=router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)
