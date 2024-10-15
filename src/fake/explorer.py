from model.explorer import Explorer


_explorers = [
    Explorer(name="Claude Hande", country="FR", description="Scarce during full moons"),
    Explorer(name="Noah Weiser", country="DE", description="Myopic machete man"),
]


def get_all() -> list[Explorer]:
    """全ての Explorer を取得する"""
    return _explorers


def get_one(name: str) -> Explorer | None:
    """指定された名前の Explorer を取得する"""
    for explorer in _explorers:
        if explorer.name == name:
            return explorer
    return None


# TODO: ここから下はテスト用のコード、DB導入の際に正しく動作するものに置き換える
def create(explorer: Explorer) -> Explorer:
    """Add an explorer"""
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """Partially modify an explorer"""
    return explorer


def replace(explorer: Explorer) -> Explorer:
    """Completely replace an explorer"""
    return explorer


def delete(name: str) -> bool:
    """Delete an explorer; return None if it existed"""
    return None
