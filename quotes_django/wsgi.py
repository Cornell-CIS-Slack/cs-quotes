"""
WSGI config for quotes_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
#my_user_packages = "/users/ejt64/.local/lib/python2.7/site-packages"
#if my_user_packages not in sys.path:
#	sys.path.append(my_user_packages)
#print >>sys.stderr, "sys.path is: " + str(sys.path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_django.settings")


application = get_wsgi_application()

# Uncomment this to force WSGI to restart when it's hung
#def application(environ, start_response):
#	if environ['mod_wsgi.process_group'] != '':
#		import signal
#		os.kill(os.getpid(), signal.SIGINT)
#	return ["killed"]
