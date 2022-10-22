import requests
from bs4 import BeautifulSoup
import aspose.words as aw
import os

url = "https://iohk.io/en/blog/posts/2022/05/27/everything-you-always-wanted-to-know-about-impermanent-loss-and-were-afraid-to-ask/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

html = str(soup.find(class_="Post__Container-sc-1lacib6-0 Ueqgo"))
with open("test/test.html", "w") as f:
    f.write(html)

doc = aw.Document("test/test.html")
doc.save("test/test.md")

with open("test/test.md", "r") as f:
    lines = f.readlines()
    lines = [line for line in lines]

with open("test/test.md", "w") as f:
    for line in lines[3:-1]:
        f.write(line)

os.remove("test/test.001.png")
os.remove("test/test.html")

#
#
# # import requests
# # from bs4 import BeautifulSoup
# # import markdownify
# #
# # url = "https://iohk.io/en/blog/posts/2022/05/27/everything-you-always-wanted-to-know-about-impermanent-loss-and-were-afraid-to-ask/"
# # req = requests.get(url)
# # soup = BeautifulSoup(req.content, 'html.parser')
# #
# # html = str(soup.find(class_="Post__Container-sc-1lacib6-0 Ueqgo"))
# # with open("test.html", "w") as f:
# #     f.write(html)
# #
# # md = markdownify.markdownify(html, heading_style="ATX")
# # with open("test.md", "w") as f:
# #     f.write(md)

# import re
#
# pattern = "(0[1-9]|[12][0-9]|3[01])[ ](January|February|March|April|May|June|July|August|September|October|November|December)[ ]((19|20)[0-9][0-9])"
# r = re.compile(pattern)
#
# s = '29 February 2020'
#
# if re.search(r, s):
#     print(re.search(r, s).group(0))