from fastapi import FastAPI

app = FastAPI()


@app.get("/hi/{who}")  # path decorator
def greet(
    who: str, word: str
):  # path function, こっちだけに定義するとクエリパラメータになる
    return f"{word} {who}"
