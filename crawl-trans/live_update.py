import shutil

import requests
from bs4 import BeautifulSoup
import aspose.words as aw
import os
import re
import telegram
import schedule
import time

def find_date(s):
    pattern = "([1-9]|[12][0-9]|3[01])[ ](January|February|March|April|May|June|July|August|September|October|November|December)[ ]((19|20)[0-9][0-9])"
    r = re.compile(pattern)

    if re.search(r, s):
        return re.search(r, s).group(0)

    return None


def send_message(msg):
    try:
        telegram_notify = telegram.Bot("5409351248:AAFknbKbdqe4e-PuzzEk5e7NCdEeK6V7weo")

        telegram_notify.send_message(chat_id="-1001668312234", text=msg, parse_mode='Markdown')

    except Exception as ex:
        print(ex)

def send_message1(msg):
    try:
        telegram_notify = telegram.Bot("5409351248:AAFknbKbdqe4e-PuzzEk5e7NCdEeK6V7weo")

        telegram_notify.send_message(chat_id="-631815701", text=msg, parse_mode='Markdown')

    except Exception as ex:
        print(ex)


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

out_path = "tmp"
dst_path = "result"

file = open("output.csv", "r", encoding="utf-8")
num = 1
for line in file:
    if line != "\n":
        num += 1
file.close()


def update():
    global num
    new_posts = []
    url = "https://iohk.io/en/blog/posts/page-1"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    all_html = soup.findAll(class_="Post__Container-sc-1lacib6-0 Ueqgo")

    for html in all_html:
        bs = BeautifulSoup(str(html), 'html.parser')
        elms = bs.select("a")
        new_posts.append("https://iohk.io" + elms[0].attrs["href"])

    with open("all_post.txt", "r", encoding="utf-8") as f:
        all_posts = f.readlines()
        all_posts = [post.rstrip() for post in all_posts]

    for post in reversed(new_posts):
        if post not in all_posts:
            with open("all_post.txt", "r+", encoding="utf-8") as f:
                content = f.read()
                f.seek(0, 0)
                f.write(post + "\n" + content)

            os.mkdir(out_path)

            req = requests.get(post)
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
                link = post

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

            for fi in os.listdir(out_path):
                if os.path.isfile(os.path.join(out_path, fi)):
                    if "html" not in fi and "md" not in fi:
                        lines = [line.replace(fi, ("img/" + fi.replace("output", year + "-{:02d}-{:02d}-".format(
                            month_to_number[month], int(day)) + post.split("/")[-2]))) for line in lines]
                        os.rename(os.path.join(out_path, fi),
                                  os.path.join(out_path, "img", fi.replace("output", year + "-{:02d}-{:02d}-".format(
                                      month_to_number[month], int(day)) + post.split("/")[-2])))

            with open(os.path.join(out_path, "output.md"), "w", encoding="utf-8") as f:
                for li in lines[3:-1]:
                    f.write(li)

            os.remove(os.path.join(out_path, "img", "output.001.png".replace("output", year + "-{:02d}-{:02d}-".format(
                month_to_number[month], int(day)) + post.split("/")[-2])))
            os.remove(os.path.join(out_path, "output.html"))

            file_name = year + "-{:02d}-{:02d}-".format(month_to_number[month], int(day)) + post.split("/")[-2] + ".md"
            os.rename(os.path.join(out_path, "output.md"), os.path.join(out_path, file_name))

            for fifo in os.listdir(out_path):
                if os.path.isfile(os.path.join(out_path, fifo)):
                    shutil.copy2(os.path.join(out_path, fifo),
                                 os.path.join(
                                     os.path.join(dst_path, year, "{:02d}".format(month_to_number[month]), fifo)))
                else:
                    for fi in os.listdir(os.path.join(out_path, fifo)):
                        if not os.path.exists(
                                os.path.join(dst_path, year, "{:02d}".format(month_to_number[month]), fifo)):
                            os.mkdir(os.path.join(dst_path, year, "{:02d}".format(month_to_number[month]), fifo))

                        shutil.copy2(os.path.join(out_path, fifo, fi),
                                     os.path.join(dst_path, year, "{:02d}".format(month_to_number[month]), fifo, fi))

            shutil.rmtree(out_path)

            message = "Update " + post + " successful"
            send_message(message)
            send_message1(message)
#send_message("Hello")
#update()
#schedule.every().hour.do(update)
while True:
#    schedule.run_pending()
    #update()
    #time.sleep(1 * 60 * 60)
    try:
        update()
    except:
        print("Connection error!")
    time.sleep(4* 60 * 60)
