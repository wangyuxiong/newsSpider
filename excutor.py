# coding=utf8
#!/usr/bin/env python

import urllib2
from GetUrlThread import GetUrlThread
from MyHtmlParser import MyHtmlParser
import datetime
import MySQLdb


def getContextFromUrl(url):
    response = urllib2.urlopen(url)
    return response.read()


def parserMetaInfo(context):
    # 解析首页出来的新内容，得到title，url，
    my = MyHtmlParser()
    my.feed(context)
    for k in my.kvs:
        print k + " , " + my.kvs[k]
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        value = [k, my.kvs[k]]
        #sql = "insert into blog_news(title,url,source) values('%s', '%s', 'jobbole.com')"
        sql = "insert into blog_news(title,url,source,create_time,update_time)  \
        values('" + k + "', '" + my.kvs[k] + "','jobbole.com','" + now + "', '" + now + "')"
        print sql
        commitDate(sql)


def commitDate(sql):
    conn = MySQLdb.connect(host='localhost', user='root', passwd='wangyx', db='mysite', charset='utf8')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    finally:
        print cursor.close


#拿到监测的站点
def parserConf(confPath):
    f = open(confPath)
    urls = []
    for url in f.readlines():
        urls.append(url.strip("\n"))
    return  urls


def  main():
    confPath = "urls.cfg"
    urls = parserConf(confPath)
    for url in urls:
        context = getContextFromUrl(url)
        parserMetaInfo(context)


def main_threads():
    confPath = "urls.cfg"
    urls = parserConf(confPath)
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()