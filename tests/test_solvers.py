import solvers
import pytest
import os


def test_ping():
    """TODO:"""
    assert True


@pytest.mark.asyncio
async def test_cat():
    test_file = 'testfile.txt'
    with open(test_file, 'w') as f:
        print("a", file=f)
    txt = await solvers.cat(test_file)
    assert txt.split()[1] is "a"
    txt = await solvers.cat('')
    assert txt.split()[0] is "E"
    os.remove(test_file)

