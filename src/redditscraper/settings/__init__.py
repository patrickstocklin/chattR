from .base import *

try:
	print "Try Production"
	from .production import *
except:
	print "Failed Production"
	pass

try:
	print "Try Local"
	from .local import *
except:
	print "Failed Local"
	pass