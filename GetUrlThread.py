# coding=utf-8
#!/usr/bin/env python

from threading import Thread


class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        response = urllib2.urlopen(self.url)
        context = response.read()
        self.parserMetainfo(context)
        #print self.url, resp.getcode()

    def parserMetainfo(self, context):
        # 解析首页出来的新内容，得到title，url，
        """

        :param context:
        """
        print context
        pass