from types import coroutine
import asyncio
import time

def sync_function(test_param:str) -> str:
    print("This is a synchronous function...")
    time.sleep(0.1)
    return f"Sync Result: {test_param}"


async def asyc_function(test_param: str) -> str:
    print("This is an asynchronous coroutine function....")
    await asyncio.sleep(0.1)
    return f"Async Result : {test_param}"




async def main():
    sync_result = sync_function("Test")
    print(sync_result)


if __name__=='__main__':
    # runs the event-loop
    asyncio.run(main())

    # loop = asyncio.get_running_loop()
    # future = loop.create_future()
    # print(f"Empty Future: {future}")

    # future.set_result("Futuew Result : Test")
    # future_result = await future
    # print(future_result)


    # coroutine_obj = asyc_function("Test")
    # print(coroutine_obj)


