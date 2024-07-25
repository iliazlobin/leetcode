import aiohttp
import asyncio


async def check_service(session, address):
    try:
        async with session.get(f"https://{address}", timeout=0.5) as response:
            result = response.status == 200
            print(f"Checked {address}: {result}")
            return address, result
    except (aiohttp.ClientError, asyncio.TimeoutError) as e:
        print(f"Failed to check {address}: {e}")
        return address, False


async def health_check(services_addresses):
    async with aiohttp.ClientSession() as session:
        tasks = [check_service(session, address) for address in services_addresses]
        results = await asyncio.gather(*tasks)
        return dict(results)


if __name__ == "__main__":
    services_addresses = [
        "google.com",
        "yahoo.com",
    ]

    result = asyncio.run(health_check(services_addresses))
    print(result)
