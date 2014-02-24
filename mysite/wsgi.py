"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
import site



"""
sys.path.append('D:\\home\\site\\wwwroot')
sys.path.append('D:\\home\\site\\wwwroot\\mysite')
sys.path.append('D:\\home\\site\\wwwroot\\polls')
"""

"""
site.addsitedir('/opt/local/Library/Frameworks/Python.framework/Versions/2.6')
sys.path.append('/Users/ubriela/git/GeoCrowdDemo/geocrowd/')
sys.path.append('/Users/ubriela/git/GeoCrowdDemo/geocrowd/mysite/')
sys.path.append('/Users/ubriela/git/GeoCrowdDemo/geocrowd/polls/')
"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

