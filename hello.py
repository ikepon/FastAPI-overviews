from fastapi import FastAPI

app = FastAPI()


@app.get("/hi/{who}")  # path decorator
def greet(who: str):  # path function
    return f"hello {who}"
