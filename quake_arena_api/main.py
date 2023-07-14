from fastapi import FastAPI


app = FastAPI(
    title='Quake Arena API', description='Game query API', version='0.0.1'
)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)
