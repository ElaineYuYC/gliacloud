# -*- coding: UTF-8 -*-

import sys

if __name__ == '__main__':
    listUrls = []
    urls = ["http://www.google.com/a.txt", "http://www.google.com.tw/a.txt", "http://www.google.com/download/c.jpg", "http://www.google.co.jp/a.txt", "http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt", "http://yahoo.com/123/000/c.jpg", "http://gliacloud.com/haha.png",]
    for strItem in urls:
        intC = strItem.rfind('/')
        listUrls.append(strItem[(intC+1):])
    dicCount = {strE:listUrls.count(strE) for strE in listUrls}
    lSort = sorted(dicCount,key=dicCount.__getitem__)
    for i in range(-1,-4,-1):
        print(lSort[i] + ' ' + str(dicCount[lSort[i]]))
