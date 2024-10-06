from fastapi import FastAPI, Body, Header

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
