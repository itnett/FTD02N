python
import asyncio

async def faulty_coroutine():
    await asyncio.sleep(1)
    raise ValueError("An error occurred")

async def main():
    try:
        await faulty_coroutine()
    except ValueError as e:
        print(f"Caught exception: {e}")

asyncio.run(main())