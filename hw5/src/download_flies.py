import sys
import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup as BS


async def main():
    n = int(sys.argv[1])
    path_dir = sys.argv[2]
    for i in range(1, n + 1):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://thissnackdoesnotexist.com/") as response:
                html = await response.text()
                soup = BS(html, features="html.parser")
                for meta_tag in soup.find_all("meta", property="og:image"):
                    image_url = meta_tag["content"]
                    image_data = requests.get(image_url).content
                    with open(path_dir + str(i) + ".jpg", "wb") as f:
                        f.write(image_data)


if __name__ == "__main__":
    asyncio.run(main())
