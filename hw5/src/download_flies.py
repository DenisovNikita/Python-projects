import sys
import time
import aiohttp
import aiofiles
import asyncio
from bs4 import BeautifulSoup as BS


async def download_site(url, session, full_path):
    async with session.get(url) as response:
        html = await response.text()
        soup = BS(html, features="html.parser")
        for meta_tag in soup.find_all("meta", property="og:image"):
            image_url = meta_tag["content"]
            if image_url == "":
                continue
            async with aiohttp.ClientSession() as image_session:
                async with image_session.get(image_url) as image_response:
                    image_data = await image_response.content.read()
                    async with aiofiles.open(full_path, "wb") as f:
                        await f.write(image_data)


async def main():
    n = int(sys.argv[1])
    path_dir = sys.argv[2]
    url = "https://thissnackdoesnotexist.com/"
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1, n + 1):
            tasks.append(
                asyncio.create_task(
                    download_site(url, session, path_dir + str(i) + ".jpg")
                )
            )
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Total: {time.time() - start_time}")
