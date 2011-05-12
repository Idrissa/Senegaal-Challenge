from google.appengine.ext import webapp
from google.appengine.dist import use_library

class ApplicationHandler(webapp.RequestHandler):
    """Base class for all handlers.
    
    Add there methods/helpers that can be used by all handlers, 
    such as greetings, logout messages, etc."""
    pass