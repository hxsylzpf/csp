import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.contrib.auth.handlers.modwsgi import check_password, groups_for_user

def check_password(environ, user, password):
    if user == 'ubriela':
        if password == 'ubiela':
            return True
        return False
    return None

