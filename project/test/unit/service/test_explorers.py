from model.explorer import Explorer
from service import exlorer as code


sample = Explorer(
    name='Claude Hande',
    country='FR',
    description='Scarce during full moons'
)


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one('Claude Hande')
    assert resp == sample


def test_get_missing():
    resp = code.get_one('wrong_name')
    assert resp is None

