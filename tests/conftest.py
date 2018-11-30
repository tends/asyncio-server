import asyncio
import pytest


@pytest.yield_fixture
def loop():
    # Настройка
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop

    # Очистка
    loop.close()
