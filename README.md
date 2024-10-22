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


# その他メモ

- ディレクトリを切った時は `__init__.py` を作る
  - ディレクトリをインポートするときに、`__init__.py` がないとエラーになる

- web -> service -> data の順でデータを取得する
  - data は DB や外部データに接続する
  - service は data を加工して web に返す
  - web は service からデータを受けてブラウザに返す

- model
  - table のカラムの型と対応
  - validation もここに書くと思う
  - Rails の AR に近い感じだと思う

- Authentication
  - ユーザーが誰か
