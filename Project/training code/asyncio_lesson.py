import asyncio

async def my_task():
    print("Начало задачи")
    await asyncio.sleep(1)
    print("Задача завершена")

async def main():
    await my_task()

asyncio.run(main())