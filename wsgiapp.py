# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)
import os, time

from www.transwarp import db
from www.transwarp.web import WSGIApplication, Jinja2TemplateEngine

from www.config import configs

def datetime_filter(t):
	delta = int(time.time() - t)
	if delta < 60:
		return u'1分钟前'
	if delta < 3600:
		return u'%s分钟前' % (delta // 60)
	if delta < 86400:
		return u'%s小时前' % (delta // 3600)
	if delta < 604800:
		return u'%s天前' % (delta // 86400)
	dt = datatime.fromtimestamp(t)
	return u'%s年%s月%s日' % (dt.yer, dt.month, dt.day)

db.create_engine(**configs.db)

wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))

template_engine = Jinja2TemplateEngine(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'www'), 'templates'))
template_engine.add_filter('datetime', datetime_filter)
wsgi.template_engine = template_engine

from www import urls
wsgi.add_interceptor(urls.user_interceptor)
wsgi.add_interceptor(urls.manage_interceptor)
wsgi.add_module(urls)

if __name__ == '__main__':
	wsgi.run(9000)