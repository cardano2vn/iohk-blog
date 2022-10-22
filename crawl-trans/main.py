import shutil
import requests
from bs4 import BeautifulSoup
import aspose.words as aw
import os
import re

month_to_number = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


def find_date(s):
    pattern = "([1-9]|[12][0-9]|3[01])[ ](January|February|March|April|May|June|July|August|September|October|November|December)[ ]((19|20)[0-9][0-9])"
    r = re.compile(pattern)

    if re.search(r, s):
        return re.search(r, s).group(0)

    return None


with open("all_post.txt", "r", encoding="utf-8") as f:
    urls = f.readlines()
    urls = [url.rstrip() for url in urls]

out_path = "tmp"
dst_path = "result"

if not os.path.exists(dst_path):
    os.mkdir(dst_path)

num = 1

for url in urls:
    os.mkdir(out_path)

    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    html = str(soup.find(class_="Post__Container-sc-1lacib6-0 Ueqgo"))
    with open(os.path.join(out_path, "output.html"), "w", encoding="utf-8") as f:
        f.write(html)

    doc = aw.Document(os.path.join(out_path, "output.html"))
    doc.save(os.path.join(out_path, "output.md"))

    with open(os.path.join(out_path, "output.md"), "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line for line in lines]

    date = None

    for line in lines:
        date = find_date(line)

        if date is not None:
            break

    day, month, year = date.rstrip().split(" ")

    with open("output.csv", "a", encoding="utf-8") as csv:

        time = "{:02d}/{:02d}/{:02d}".format(int(day), month_to_number[month], int(year))

        num1 = lines[3].find("**")
        num2 = lines[3].rfind("**")
        title = lines[3][num1 + 2:num2].rstrip()
        link = url

        num3 = lines[5].rfind(")")
        min_reads = lines[5][num3 + 2:].rstrip()

        if "min" not in min_reads or "read" not in min_reads:
            for j in range(3, 10):
                if "min" in lines[j] and "read" in lines[j]:
                    num3 = lines[j].rfind(")")
                    min_reads = lines[j][num3 + 2:].rstrip()
                    break

        csv.write("{}\t{}\t{}\t{}\t{}\n".format(num, time, title, link, min_reads))
        num += 1

        lines[3] = "# " + title + "\n"

    if not os.path.exists(os.path.join(dst_path, year, "{:02d}".format(month_to_number[month]))):
        os.makedirs((os.path.join(dst_path, year, "{:02d}".format(month_to_number[month]))))

    if not os.path.exists(os.path.join(out_path, "img")):
        os.mkdir(os.path.join(out_path, "img"))

    for file in os.listdir(out_path):
        if os.path.isfile(os.path.join(out_path, file)):
            if "html" not in file and "md" not in file:
                lines = [line.replace(file, ("img/" + file.replace("output", year + "-{:02d}-{:02d}-".format(
                    month_to_number[month], int(day)) + url.split("/")[-2]))) for line in lines]
                os.rename(os.path.join(out_path, file),
                          os.path.join(out_path, "img", file.replace("output", year + "-{:02d}-{:02d}-".format(
                              month_to_number[month], int(day)) + url.split("/")[-2])))

    with open(os.path.join(out_path, "output.md"), "w", encoding="utf-8") as f:
        for line in lines[3:-1]:
            f.write(line)

    os.remove(os.path.join(out_path, "img", "output.001.png".replace("output", year + "-{:02d}-{:02d}-".format(
        month_to_number[month], int(day)) + url.split("/")[-2])))
    os.remove(os.path.join(out_path, "output.html"))

    file_name = year + "-{:02d}-{:02d}-".format(month_to_number[month], int(day)) + url.split("/")[-2] + ".md"
    os.rename(os.path.join(out_path, "output.md"), os.path.join(out_path, file_name))

    for fifo in os.listdir(out_path):
        if os.path.isfile(os.path.join(out_path, fifo)):
            shutil.copy2(os.path.join(out_path, fifo),
                         os.path.join(os.path.join(dst_path, year, "{:02d}".format(month_to_number[month]), fifo)))
        else:
            for fi in os.listdir(os.path.join(out_path, fifo)):
                if not os.path.exists(os.path.join(dst_path, year, "{:02d}".format(month_to_number[month]), fifo)):
                    os.mkdir(os.path.join(dst_path, year, "{:02d}".format(month_to_number[month]), fifo))

                shutil.copy2(os.path.join(out_path, fifo, fi),
                             os.path.join(dst_path, year, "{:02d}".format(month_to_number[month]), fifo, fi))

    shutil.rmtree(out_path)
