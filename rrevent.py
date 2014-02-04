from pox.core import core
from pox.lib.revent import *

class Chef(EventMixin):

 _eventMixin_events = set([
	SpamStarted,
	SpamFinished,
 ])

class Hungry(object):

 def __init__(self):
  chef.addListeners(self)

 def _handle_SpamStarted(self,event):
  print"I cant blah blah"
 
 def _handle_SpamFinished(self,event):
  print "Spam is ready"

def launch():
 chef=Chef("spam")
 core.registerNew(Chef)
