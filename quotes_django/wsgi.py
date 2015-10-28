"""
WSGI config for quotes_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_django.settings")

import sys
sys.path.append("/users/ejt64/.local/lib/python2.7/site-packages")
print >>sys.stderr, "sys.path is: " + str(sys.path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Uncomment this to force WSGI to restart when it's hung
#def application(environ, start_response):
#	if environ['mod_wsgi.process_group'] != '':
#		import signal
#		os.kill(os.getpid(), signal.SIGINT)
#	return ["killed"]
