# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup

__Author__ = "Sky Huang"
import os
import json

proDir = os.path.split(os.path.realpath(__file__))[0]
filePath2 = os.path.join(proDir + "\\media\\uploads\\", "测试.html")
filePath = os.path.join(proDir, "测试.html")
file = open(file=filePath, encoding="utf-8").read()
soup = BeautifulSoup(file, "html.parser")
allData = []
count = 1

for k in soup.find_all("a"):
    value = k.text.replace(u'\xa0', u'$')
    allData.append([count, value])
    count += 1

print(allData)

sz = []
allData[0].append(0)
allData[1].append(0)
sz.append(allData[0])
sz.append(allData[1])

# print(sz)

for i in range(len(allData)):
    if i > 1:
        prew_index = len(allData[i - 1][1]) - len(allData[i - 1][1].replace('$', ''))
        now_index = len(allData[i][1]) - len(allData[i][1].replace('$', ''))
        if now_index - prew_index == 1:
            allData[i].append(allData[i - 1][0])
        elif now_index - prew_index == 0:
            try:
                allData[i].append(allData[i - 1][2])
            except Exception as e:
                print(allData[i - 1], e)
        elif now_index - prew_index < 0:
            for l in range(0, len(sz)):
                # 找新数组
                _prew_index = len(sz[(len(sz) - 1) - l][1]) - len(sz[(len(sz) - 1) - l][1].replace('$', ''))
                if now_index - _prew_index == 0:
                    allData[i].append(sz[(len(sz) - 1) - l][2])
                    break
        sz.append(allData[i])

# print(sz)


def getchild(pid):
    result = []
    for obj in sz:
        if obj[2] == pid:
            result.append({
                "id": obj[0],
                "title": obj[1].replace('$', ''),
                "pid": obj[2],
                "children": getchild(obj[0]),
            })

    return result


newResult = getchild(0)
for item in range(1, len(newResult)):
    newResult[0]["children"].append(newResult[item])
for item in range(1, len(newResult)):
    newResult.pop()

print(newResult)

json_str2 = json.dumps(newResult[0], ensure_ascii=False)
# print(json_str2)

print("*"*50)

def fun(list):
    for i in range(0,len(list)):
        id = list[i]["id"]
        title = list[i]["title"]
        pid = list[i]["pid"]
        children_list = list[i]["children"]
        print("id:",id,"title:",title,"pid:",pid)
        if len(children_list) == 0:
            pass
        else:
            fun(children_list)
fun(newResult)

listA = [1, 2, 3, 4, 5]
listB = [0, 0, 0, 5, 3]
retE = [i for i in listB if i in listA]
print(retE)