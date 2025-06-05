import asyncio
import aiohttp
import os
import time


# url = "http://"

# # This is the function that makes a single HTTP GET request
# async def fetch(session, i):
#     async with session.get(url) as response:
#         print(f"Request {i}: Status {response.status}")
#         return await response.text()

# # This function kicks off multiple fetches concurrently
# async def main():
#     async with aiohttp.ClientSession() as session:
#         # Create a list of tasks (5–6 fetch requests)
#         tasks = [fetch(session, i) for i in range(1, 7)]

#         # Run all the tasks at the same time (concurrently)
#         await asyncio.gather(*tasks)

# # This line tells Python to start the async event loop
# asyncio.run(main())


# ==== CONFIG ====
url = "http://"
file_path = "file_path.jpg"
bearer_token = "bearer_token"
csrf_token = "csrf_token"
# ===============


async def upload_file(session, i):
    with open(file_path, "rb") as f:
        data = aiohttp.FormData()
        data.add_field("type", "nic")
        data.add_field("name", "card")
        data.add_field(
            "file", f, filename=os.path.basename(file_path), content_type="image/jpeg"
        )

        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "X-CSRFToken": csrf_token,
        }

        async with session.post(url, data=data, headers=headers) as response:
            print(f"[Request {i}] Status: {response.status}")
            # print(await response.text())


async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 6):
            tasks.append(upload_file(session, i))
            # await asyncio.sleep(1)

        await asyncio.gather(*tasks)
    end = time.time()
    total_time = end - start
    print(f"\nTotal time taken: {total_time:.2f} seconds\n")


asyncio.run(main())
