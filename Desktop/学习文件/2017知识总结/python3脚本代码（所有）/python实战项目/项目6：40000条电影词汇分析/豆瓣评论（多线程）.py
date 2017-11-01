#coding=utf-8
import re
import urllib.request
import re
import jieba
from lxml import etree
from bs4 import BeautifulSoup
import time
import threading
import requests

def gethtml(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
             "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
             "Connection":"keep - alive",
             "Content - Encoding":"gzip",
             "Host": "movie.douban.com",
             'Cookie': 'bid=f_cT-3VfchQ; ll="118256"; __yadk_uid=zqqqOSVlrwWugPAXNsQKpM0VS0W4b8Aj; viewed="25779298"; gr_user_id=d4e8d84f-1387-4169-aadc-0deaf0e6f271; _vwo_uuid_v2=395BD4CEB8065D73CFC22FF207D3BE5D|56027b00887700d2d1ec7fa396cf151a; ps=y; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1509452085%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dm422JNGW44MeaZ0N2qIo8_YotI9wQjPGwONV_OgDWuTFEADixxlv0fo-8doOrHuB%26wd%3D%26eqid%3Dc5a449f7000036470000000559f8173c%22%5D; _pk_id.100001.4cf6=90f5e53cae5fdbd8.1507626744.4.1509452196.1509434978.; __utma=223695111.832803071.1507626744.1509431102.1509452085.4; __utmc=223695111; __utmz=223695111.1509431102.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap=1; dbcl2="168974350:Fu010jQoJ+I"; ck=_tw1; push_noty_num=0; push_doumail_num=0; __utma=30149280.826665397.1507626744.1509431101.1509452085.5; __utmc=30149280; __utmz=30149280.1509431101.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.16897'
            }
    req = urllib.request.Request(url=url, headers=headers)
    page=urllib.request.urlopen(req)
    page2=page.read().decode('utf-8')
    soup=BeautifulSoup(page2,'html.parser')
    #print(soup)
    return soup
def getcontent(soup):

    for one in range(1,21):
        onediv="div"+str([int(one)])
        s=etree.HTML(str(soup))
        content = s.xpath('//*[@id="comments"]/%s/div[2]/p/text()' % onediv)
        #print(content[0])
        seg_list = list(jieba.cut(content[0], cut_all=False))
        #dic="/ ".join(seg_list)  # 精确模式
        #print(seg_list)
        for j in range(0,len(seg_list)):
            if len(seg_list[j]) >= 2:
                with open(r'C:\Users\Administrator\Desktop\肖申克1.csv','a') as f:
                    f.write(seg_list[j]+"\n")
                #print(seg_list[j])
            else:
                #print(seg_list[j])
                pass

    #for i in range(0,len(text)):
        #print(text[i])

def load1():
    for num in range(221,251):
        url="https://movie.douban.com/subject/1292052/comments?start=%s&limit=20&sort=new_score&status=P&percent_type=" % num
        soup=gethtml(url)
        getcontent(soup)
        print(str(num+1)+"is over!")
        time.sleep(0.5)
def load2():
    for num1 in range(251,281):
        url="https://movie.douban.com/subject/1292052/comments?start=%s&limit=20&sort=new_score&status=P&percent_type=" % num1
        soup=gethtml(url)
        getcontent(soup)
        print(str(num1+1)+"is over!")
        time.sleep(0.5)
def load3():
    for num1 in range(281,311):
        url="https://movie.douban.com/subject/1292052/comments?start=%s&limit=20&sort=new_score&status=P&percent_type=" % num1
        soup=gethtml(url)
        getcontent(soup)
        print(str(num1+1)+"is over!")
        time.sleep(0.5)
def load4():
    for num1 in range(311,341):
        url="https://movie.douban.com/subject/1292052/comments?start=%s&limit=20&sort=new_score&status=P&percent_type=" % num1
        soup=gethtml(url)
        getcontent(soup)
        print(str(num1+1)+"is over!")
        time.sleep(0.5)
threads=[]
t1=threading.Thread(target=load1)
t2=threading.Thread(target=load2)
t3=threading.Thread(target=load3)
t4=threading.Thread(target=load4)

threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)
for t in threads:
    t.setDaemon(False)
    t.start()
