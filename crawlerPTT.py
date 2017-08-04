# -*- coding: UTF-8 -*-

from urllib.request import urlopen
from urllib import parse
import sys
import os

def saveHTML(htmlContent):
    with open('pttText.html', 'w', encoding="utf-8") as fHTML:
        fHTML.write(htmlContent)

if __name__ == '__main__':
    global strURL
    strURL = "https://www.ptt.cc/bbs/Soft_Job/index.html"

    with urlopen(strURL) as responseURL:
        bytesHtml = responseURL.read()
        strHtml = bytesHtml.decode("utf-8")
        saveHTML(strHtml)
        print("done")
    
