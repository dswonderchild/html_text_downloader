import urllib.request
import html2text
import sys

def my_print(text):
    sys.stdout.write(str(text)+"\n")
    sys.stdout.flush()

##https://mydocx.ru/6-30956.html
##https://mydocx.ru/6-31252.html

number = 30956

while number < 31253:
    url = f"https://mydocx.ru/6-{number}.html"
    try:
        fp = urllib.request.urlopen(url)
    except:
        pass
    mybytes = fp.read()
    mystr = mybytes.decode("windows-1251")
    fp.close()

    text = html2text.html2text(mystr)

    my_print(number)

    with open("text.txt", "a", encoding="utf-8") as f:
        f.write(text)

    number += 1
