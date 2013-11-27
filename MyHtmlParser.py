# coding=gb2312
#!/usr/bin/env python

from sgmllib import SGMLParser


class MyHtmlParser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_a = 0
        self.valid = 0
        self.url = ''
        self.kvs = {}

    def start_a(self, attrs):
        self.is_a = 1
        for k, v in attrs:
            if k == 'class' and v == "meta-title":
                self.valid = 1

        for k, v in attrs:
            if k == 'href':
                if v.startswith('http'):
                    self.url = v

    def end_a(self):
        self.is_a = 0
        self.valid = 0
        self.url = ''

    def handle_data(self, text):
        if self.is_a == 1 and self.valid == 1:
            self.kvs[text] = self.url

