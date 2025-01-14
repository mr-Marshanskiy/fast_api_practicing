from service import user as code


def test_verify_password():
    resp = code.verify_password(
        '123456', '123123123'
    )
    assert resp is True


def test_get_hash():
    resp = code.get_hash(
        '123456',
    )
    assert type(resp) is str
