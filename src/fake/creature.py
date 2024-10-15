from model.creature import Creature


_creatures = [
    Creature(
        name="Yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
    ),
    Creature(
        name="Bigfoot",
        description="Yeti's Cousin Eddie",
        country="US",
        area="*",
        aka="Sasquatch",
    ),
]


def get_all() -> list[Creature]:
    """全ての Creature を取得する"""
    return _creatures


def get_one(name: str) -> Creature | None:
    """指定された名前の Creature を取得する"""
    for creature in _creatures:
        if creature.name == name:
            return creature
    return None


# TODO: ここから下はテスト用のコード、DB導入の際に正しく動作するものに置き換える
def create(creature: Creature) -> Creature:
    """Add a creature"""
    return creature


def modify(creature: Creature) -> Creature:
    """Partially modify a creature"""
    return creature


def replace(creature: Creature) -> Creature:
    """Completely replace a creature"""
    return creature


def delete(name: str) -> bool:
    """Delete a creature; return None if it existed"""
    return None
