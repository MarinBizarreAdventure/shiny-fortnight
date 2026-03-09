import asyncio
import random
async def fetch_data(url: str) -> str:
    print(f"starting {url}")
    await asyncio.sleep(random.randint(0,2))
    print(f"Done {url}")
    return f"data from {url}"

async def main():
    r1 = await fetch_data("url1")
    r2 = await fetch_data("url2")
    r3 = await fetch_data("url3")


    result = await asyncio.gather(
        fetch_data("url1"),
        fetch_data("url2"),
        fetch_data("url3"),
    )

asyncio.run(main())
