import asyncio
import sys

import aiohttp
import os


async def download(session, url, filepath):
    async with session.get(url) as response:
        if response.status == 200:
            with open(filepath, 'wb') as f:
                f.write(await response.read())
            print(f'downloaded {filepath}')
        else:
            print(f'failed to download {url} with status {response.status}')


async def download_images(amount, folder):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(amount):
            url = f'https://picsum.photos/200/300?random={i + 1}'
            filepath = os.path.join(folder, f'image_{i + 1}.jpg')
            tasks.append(download(session, url, filepath))
        await asyncio.gather(*tasks)


def main():
    amount = int(sys.argv[1])
    folder = sys.argv[2]

    if not os.path.exists(folder):
        os.makedirs(folder)

    asyncio.run(download_images(amount, folder))


if __name__ == '__main__':
    main()
