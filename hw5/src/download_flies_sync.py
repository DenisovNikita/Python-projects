import sys
import time
import requests
from bs4 import BeautifulSoup as BS


def download_site(url, full_path):
    with requests.get(url) as response:
        html = response.text
        soup = BS(html, features="html.parser")
        for meta_tag in soup.find_all("meta", property="og:image"):
            image_url = meta_tag["content"]
            if image_url == "":
                continue
            with requests.get(image_url) as image_response:
                image_data = image_response.content
                with open(full_path, "wb") as f:
                    f.write(image_data)


def main():
    start_time = time.time()
    n = int(sys.argv[1])
    path_dir = sys.argv[2]
    url = "https://thissnackdoesnotexist.com/"
    for i in range(n):
        download_site(url, path_dir + str(i + 1) + ".jpg")
    with open(path_dir + "time.txt", "w") as f:
        f.write(f"Time: {time.time() - start_time}")


if __name__ == "__main__":
    main()
