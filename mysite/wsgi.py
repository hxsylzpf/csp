"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
import site

site.addsitedir('/opt/local/Library/Frameworks/Python.framework/Versions/2.6')
sys.path.append('/Users/ubriela/DropboxUSC/Dropbox/_USC/Code/Python/Django/')
sys.path.append('/Users/ubriela/DropboxUSC/Dropbox/_USC/Code/Python/Django/mysite')
sys.path.append('/Users/ubriela/DropboxUSC/Dropbox/_USC/Code/Python/Django/mysite/mysite')
sys.path.append('/Users/ubriela/DropboxUSC/Dropbox/_USC/Code/Python/Django/mysite/polls')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

