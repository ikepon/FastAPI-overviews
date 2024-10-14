# Overview Fast API

## 1. fastapi を立ち上げる

- 仮想環境立ち上げ

```
source .venv/bin/activate
```

- ライブラリインストール

```
uv add fastapi
uv add uvicorn
```

- アプリケーション起動

```
# main.py を直接実行する場合
python src/main.py

# uvicorn を使って起動する場合
uvicorn hello:app --reload
```

## 2. ブラウザで確認する

http://127.0.0.1:8000/hi
