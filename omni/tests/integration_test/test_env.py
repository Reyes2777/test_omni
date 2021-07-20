from pytest import mark


@mark.asyncio
async def test_create(db_transaction):
    a = 1
    assert a == 1
