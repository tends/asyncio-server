import solvers
import pytest
import os


async def check_solver(tested_func, args, exp):
    res = await tested_func(args)
    assert res.startswith(exp) is True


@pytest.mark.asyncio
async def test_ping():
    """TODO:"""
    await check_solver(solvers.ping, '8.8.8.8', 'E ping exception: Operation not permitted - Note that ICMP messages')


@pytest.mark.asyncio
async def test_cat():
    test_file = 'testfile.txt'
    with open(test_file, 'w') as f:
        print("a", file=f)

    await check_solver(solvers.cat_file, test_file, 'S a')
    await check_solver(solvers.cat_file, '', 'E ')

    os.remove(test_file)


@pytest.mark.asyncio
async def test_sum_items():
    test_set = {
        ('1', '2', '3'): 'S 6',
        ('1', ): 'S 1',
        ('1', 'a'): 'E '
    }

    for args, expected in test_set.items():
        res = await solvers.sum_items(list(args))
        assert res.startswith(expected) is True


@pytest.mark.asyncio
async def test_sleep_secs():
    test_set = {
        ('1',): 'S done',
        ('0', ): 'S done',
        ('1', 'a'): 'E '
    }

    for args, expected in test_set.items():
        res = await solvers.sleep_secs(list(args))
        assert res.startswith(expected) is True



