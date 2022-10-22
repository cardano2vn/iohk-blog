import requests
from bs4 import BeautifulSoup

all_post = []

for i in range(1, 65):
    url = "https://iohk.io/en/blog/posts/page-" + str(i) + "/#blog-posts"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    #all_html = soup.findAll(class_="Post__HeadContent-sc-1lacib6-3 ffZKuJ")

    all_html = soup.findAll(class_="Post__HeadContent-sc-1lacib6-3 eTFHst")

    for html in all_html:
        bs = BeautifulSoup(str(html), 'html.parser')
        elms = bs.select("a")
        all_post.append("https://iohk.io" + elms[0].attrs["href"])

with open("all_post.txt", "w", encoding="utf-8") as f:
    for i in all_post:
        f.write(i + "\n")
