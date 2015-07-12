# -*- coding: utf-8 -*-

__author__ = 'fang'

from models import User, Blog, Comment

from transwarp import db

db.create_engine(user='root', password='password',database='awesome')

u = User(name='Administrato', email='admi@example.com', password='1234567890', image='about:blank')

u.insert()
print 'new user:', u
u.delete()

b1 = Blog(user_id='0014347129972910bbdee0a188f412394d92e5e5a299939000', user_name='Administrator',
	name = 'FirstBlog', summary='Test', content = 'Test.')

b1.insert()
print 'new blog:', b1
b1.delete()



'''
u1 = User.find_first('where email=?', 'test@example.com')
print 'find user\'s name:', u1.name

u2 = User.find_first('where email=?', 'test@example.com')
print 'find user:', u2
'''