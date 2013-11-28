# coding=utf-8
#!/usr/bin/env python

import web

urls = (
    '/', 'index'
)

render = web.template.render('templates/')

class index:
    def GET(self):
        db = web.database(dbn='mysql', user='root', pw='wangyx', db='mysite')
        posts = db.query("select * from blog_news order by id desc limit 32")
        return render.index(posts)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()