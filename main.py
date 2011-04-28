import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import datetime

class WelcomePage(webapp.RequestHandler): 
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
    self.response.out.write(template.render(path, {})) 

app = webapp.WSGIApplication([('/', WelcomePage)])
    
def main():
  run_wsgi_app(app)

if __name__ == "__main__":
  main()
