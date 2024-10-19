from fastapi import FastAPI, Body, Depends, Header, Query
import asyncio
import uvicorn
from _data import get_creatures

app = FastAPI()


@app.get("/hi/{who}")  # path decorator
def greet(
    who: str, word: str
):  # path function, こっちだけに定義するとクエリパラメータになる
    return f"{word} {who}"


@app.post("/hi")
def greet_post(who: str = Body(embed=True)):
    return f"hello {who}: body"


@app.post("/hi/header")
def greet_query(who: str = Header()):
    return f"hello {who}: header"


@app.get("/creatures")
def get_creature():
    return get_creatures()


@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(1)
    return {"message": "Hello, World!"}


def user_dep(name: str = Query(), password: str = Query()):
    return {"name": name, "valid": True}


@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user
