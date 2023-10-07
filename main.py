from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def readRoot():
    return {
        'hello': 'world'
    }
