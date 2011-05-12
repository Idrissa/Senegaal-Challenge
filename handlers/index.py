from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from handlers.application import ApplicationHandler

class IndexHandler(ApplicationHandler):
  def get(self):
    values = {}
    self.response.out.write(template.render("templates/index.html", values))
