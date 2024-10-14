from model import Creature


_creatures: list[Creature] = [
    Creature(
        name="hoge", country="japan", area="tokyo", description="hogehoge", aka="hoge"
    )
]


def get_creatures() -> list[Creature]:
    return _creatures
