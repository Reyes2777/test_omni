from pytest import mark


@mark.asyncio
async def test_create(create_db):
    a = 1
    assert a == 1
