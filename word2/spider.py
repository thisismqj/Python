import json
import requests
from bs4 import BeautifulSoup as bs
import re

timer = 1

file = "class"
word_list = open("source//"+file+".txt").readlines()[:-2]
result = open("library//"+file+"//main.json", "a+", encoding="utf-8")

def get(word):
    try:
        url = "https://dict.cn/" + word
        response = requests.get(url)
        html = bs(response.text, "lxml")
        d1 = {"word": word, "mean": {}, "speech": {}}
        mean = html.find(name="ul", attrs={
                         "class": "dict-basic-ul"}).find_all(name="li", attrs={})[:-1]
        for j in mean:
            try:
                #        print(j.span.text)
                #        print(re.split(r"；", j.strong.text))
                d1["mean"][j.span.text] = re.split(r"；", j.strong.text)
            except:
                print("There was sth. wrong...")
        try:
            adapt = html.find(
                name="div",
                attrs={"class": "layout phrase"}).find_all(
                name="dl")
        except:
            pass
        else:
            for i in adapt:
                try:
                    d1["speech"][re.match(r"[a-z 〔〕/']*", i.dt.b.text).group()] = re.search(
                        r"(?<=\n\t\t\t\t\t\t\t\t\t).*?(?=[a-z])", i.dd.ol.text, re.DOTALL).group()
                except:
                    print("There was sth. wrong...")
        return d1
    except:
        return "?"
try:
    for each_word in word_list:
        print(timer, end=" ")
        result.write(json.dumps(get(each_word), indent=4,
                                ensure_ascii=False) + "\n")
        timer += 1
except:
    result.close()
# 草