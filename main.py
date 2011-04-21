from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import datetime

class WelcomePage(webapp.RequestHandler): 
  def get(self):
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write(
      """<html> <head>
      <title>Senegaal's Challenge</title> </head>
      <body>
      <h1>Senegaal's Challenge</h1>
      <p> The current time is: %s</p>
      </body> </html>
      """ % (datetime.datetime.now())) 

app = webapp.WSGIApplication([('/', WelcomePage)])
    
def main():
  run_wsgi_app(app)

if __name__ == "__main__":
  main()