python
import asyncio

async def main():
    await asyncio.sleep(1)
    print("Hello, World!")

# Kjør den asynkrone funksjonen
asyncio.run(main())