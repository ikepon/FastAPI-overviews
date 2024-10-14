import os

from fastapi import FastAPI

app = FastAPI()

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
