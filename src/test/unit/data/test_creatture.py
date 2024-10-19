import os
import pytest
from model.creature import Creature
from errors import Missing, Duplicate

# set this before data imports below for data.init
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import creature


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="Yeti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman",
    )


def text_create(sample: Creature):
    resp = creature.create(sample)
    assert resp == sample


def test_create_duplicate(sample: Creature):
    with pytest.raises(Duplicate):
        _ = creature.create(sample)


def test_get_one(sample: Creature):
    resp = creature.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = creature.get_one("Missing")


def test_modify(sample: Creature):
    creature.area = "Sesame Street"
    resp = creature.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    thing: Creature = Creature(
        name="Missing",
        country="US",
        area="Missing",
        description="Missing",
        aka="Missing",
    )
    with pytest.raises(Missing):
        _ = creature.modify(thing.name, thing)


def test_delete(sample: Creature):
    resp = creature.delete(sample.name)
    assert resp is None


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = creature.delete(sample.name)
