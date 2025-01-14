import os
import pytest

from exceptions import Duplicate, Missing
from model.user import User
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import user


@pytest.fixture
def sample() -> User:
    return User(
        name='Ivan',
        hash='12345',
    )


def test_creature(sample):
    resp = user.create(sample)
    assert resp == sample


def test_crete_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = user.create(sample)


def test_get_one(sample):
    resp = user.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = user.get_one('Peter')


def test_modify(sample):
    sample.hash = 'new_hash'
    resp = user.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    thing: User = User(
        name='Fedor', hash='abc',
    )
    with pytest.raises(Missing):
        _ = user.modify(thing.name, thing)


def test_delete(sample):
    resp = user.delete(sample.name)
    assert resp is True
    x_user = user.get_one(name=sample.name, table=user.x_table_name)
    assert x_user.name == sample.name


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = user.delete(sample.name)

