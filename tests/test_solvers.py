import solvers
import pytest
import os


@pytest.mark.asyncio
async def test_ping():
    """TODO:"""
    res = await solvers.ping('8.8.8.8')
    assert res.startswith('E ping exception: Operation not permitted - Note that ICMP messages can only be sent from '
                          'processes running as root.') is True


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

