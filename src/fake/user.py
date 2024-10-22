from model.user import User
from errors import Missing, Duplicate

fakes = [
    User(name="alice", hash="abc"),
    User(name="bob", hash="def"),
]


def find(name: str) -> User:
    for user in fakes:
        if user.name == name:
            return user
    return None


def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"Missing user {name}")


def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"Duplicate user {name}")


def get_all() -> list[User]:
    """Return all users"""
    return fakes


def get_one(name: str) -> User:
    """Return one user"""
    check_missing(name)
    return find(name)


def create(user: User) -> User:
    """Add a user"""
    check_duplicate(user.name)
    return user


def modify(name: str, user: User) -> User:
    """Partially modify a user"""
    check_missing(name)
    return user


def delete(name: str) -> None:
    """Delete a user"""
    check_missing(name)
    return None
