import multiprocessing
import os
import asyncio
import aiohttp
import time
import requests # использует блокирующие сокеты

async def async_hello():
    print("Hello")
    await asyncio.sleep(1)
    return "World"


async def my_coro(my_val):
    await asyncio.sleep(1)
    return my_val + 1


async def func_with_exception():
    raise TypeError


async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            return data
        

async def task_to_cancel(name):
    try:
        print(f"Task {name} started")
        await asyncio.sleep(1)
        print(f"Task {name} finished")
    except asyncio.CancelledError:
        print(f"Task {name} was cancelled")


async def write_to_file(lock, file, content):
    async with lock:
        await asyncio.sleep(1) # симуляция записи в файл
        file.write(content + "\n")
        await asyncio.sleep(1)
        file.write(f"end of coro with content {content}" + "\n")


async def main():
    lock = asyncio.Semaphore(2)
    with open("output.txt", "w") as f:
        await asyncio.wait_for(
            write_to_file(lock, f, "first_entry"),
            timeout=2
        )

    # task = asyncio.create_task(task_to_cancel("my_task"))
    # await asyncio.sleep(2)
    # task.cancel()
    # await task

    # start_time = time.time()
    # url = "http://example.com"
    # tasks = [get_data(url) for i in range(10)]
    # middle_time = time.time()
    # result = await asyncio.gather(*tasks)
    # end_time = time.time()
    # print(end_time - middle_time)
    # print(end_time - start_time)
    # print(len(result))

    # try:
    #     async with asyncio.TaskGroup() as tg:
    #         task1 = tg.create_task(my_coro(1))
    #         task2 = tg.create_task(my_coro(2))
    #         task3 = tg.create_task(func_with_exception())
    #         # Автоматическое ожидание завершения задач
    # except Exception:
    #     pass
    
    # print(task1.result(), task2.result())

    # asyncio.gather() - способ дождаться выполнения нескольких корутин
    # results = await asyncio.gather(task1, task2, task3, return_exceptions=True)
    # print(results)

    # Ожидать все корутины вручную
    # await task1   
    # await task2
    # try:
    #     await task3
    # except Exception as e:
    #     pass
    # print(task1.result())
    # print(task2.result())


if __name__ == "__main__":
    asyncio.run(main())
