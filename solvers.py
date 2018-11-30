import asyncio
import aioping
import aiofiles
from aiocache import SimpleMemoryCache

cache = SimpleMemoryCache()


async def ping(host):
    """
    TODO: Operation not permitted Необходимо реализовать следующие команды:
    Проверка доступности сервера:
    ping -> S pong
    """
    try:
        delay = await aioping.ping(host) * 1000
        print("Ping response in %s ms" % delay)
    except Exception as e:
        return "E ping exception: {}".format(e)
    else:
        return "S pong"


async def cat(file_name):
    """
    Вывод файла с диска:
    cat <FILENAME> -> S <DATA> или E <comment> если файла нет (или ошибка чтения)
    """
    try:
        async with aiofiles.open(file_name, mode='r') as f:
            contents = await f.read()
    except Exception as e:
        return "cat file error %s" % e
    else:
        return "S \n" + contents


async def sum(args):
    """
    Суммирование всех параметров:
    sum 1 2 3 ... 4 5 (неограниченное число параметров) -> S <СУММА>
    Пауза:
    """

    result = 0
    try:
        for each in  (map(int, args)):
            result += int(each)
    except Exception as e:
        return "E %s" % e
    else:
        return "S " + str(result)


async def sleep(msg):
    """sleep <SECONDS> -> S done (через <SECONDS> секунд)
    """
    try:
        secs = int(msg)
    except Exception as e:
        return "E Error parse msg to seconds: {}".format(e)
    else:
        await asyncio.sleep(secs)
        return "S done"


async def set(args):
    """
    Запись в глобальное хранилище (в памяти):
    set <KEY> <VALUE> -> S <comment>, либо E <comment> если сохранить не удалось
    """
    try:
        key = args[0]
        value = args[1:]
        res = await cache.set(key, value)
    except Exception as e:
        return "E %s" % e
    else:
        return "S %s" % res


async def get(args):
    """
    Получение значения из хранилища:
    get <KEY> -> S <VALUE> или E <comment> (если ключа нет)
    """
    try:
        res = await cache.get(args[0])
    except Exception as e:
        return "E %s" % e
    else:
        return "S %s" % res if res is not None else "E %s" % res

