import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from web import explorer, creature, auth, user  # 分けた router をインポート

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # NOTE: ここに URL("http://localhost:3000"とか) を指定すると、その URL からのリクエストのみ許可することができる
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(explorer.router)  # 分けた router を追加
app.include_router(creature.router)  # 分けた router を追加
app.include_router(auth.router)  # 分けた router を追加
app.include_router(user.router)  # 分けた router を追加
# TODO: ログの設定を調整する
LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "fmt": os.getenv("LOG_FORMAT_DEFAULT", "%(levelprefix)s %(message)s")
        },
        "access": {
            "fmt": os.getenv(
                "LOG_FORMAT_ACCESS",
                '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
            )
        },
    },
}


@app.get("/")
def top():
    return {"message": "Hello, World!"}


@app.get("/echo/{thing}")
def echo(thing: str):
    return {"message": thing}


if __name__ == "__main__":
    import uvicorn

    # "main:app" は、main.py ファイルの app インスタンスを参照しているという意味
    # reload=True は、src またはそのサブディレクトリのコードが変更されると自動的にリロードする
    uvicorn.run("main:app", reload=True)
