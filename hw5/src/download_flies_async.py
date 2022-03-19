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


async def download_site_n_times(url, n, path_dir):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task
            (
                download_site(url, session, path_dir + str(i + 1) + ".jpg")
            ) for i in range(n)]
        await asyncio.gather(*tasks)


def main():
    start_time = time.time()
    n = int(sys.argv[1])
    path_dir = sys.argv[2]
    url = "https://thissnackdoesnotexist.com/"
    asyncio.run(download_site_n_times(url, n, path_dir))
    with open(path_dir + "time.txt", "w") as f:
        f.write(f"Total: {time.time() - start_time}")


if __name__ == "__main__":
    main()
