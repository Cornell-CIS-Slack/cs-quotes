import string
import random

def generate_api_key():
	return "".join([random.SystemRandom().choice(string.ascii_letters+string.digits) for n in xrange(64)])
