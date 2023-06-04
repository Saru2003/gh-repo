#! /usr/bin/env python3
import argparse
from bs4 import BeautifulSoup
import requests
import re
parser=argparse.ArgumentParser(description='git')
parser.add_argument('-u',type=str,help='username')
parser.add_argument('-y',type=str,help='year')
args=parser.parse_args()
def c(uname,yr):
    url=f'https://github.com/{uname}?tab=repositories'
    result=requests.get(url)
    doc=BeautifulSoup(result.text,'html.parser')
    d={}
    l=[]
    for article in doc.find_all("li",itemprop="owns"):
        f=article.div.div.h3.a
        f1=f.text.split()
        ff=f"https://github.com/{uname}/"+f1[0]
        status=article.div.div.h3("span",class_="Label Label--secondary v-align-middle ml-1 mb-1")
        s=str(status).split('<span class="Label Label--secondary v-align-middle ml-1 mb-1">')
        ss=s[1].split('</span')
        p=article.div("span")
        pr=str(p).split("</span>")
        pro=pr[-2].split('>')
        t=article.find("relative-time").text#["datetime"]
        l.append([f.text,ff,ss[0],pro[-1],t])
    i=0
    for i in range(len(l)):
        s=l[i][-1].split(', ')
        if s[1]==str(yr):
            d=l[i][0].split()
            print(f"{l[i][4][:5]}: {d[0]} Link: {l[i][1]} "+f"( {l[i][2]}, {l[i][3]} )")
            i=1
    if i==0:
        print("Invalid command.")

if __name__=='__main__':
    c(args.u,args.y)
