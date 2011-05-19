from google.appengine.ext import webapp
from google.appengine.dist import use_library
from google.appengine.api import users


class ApplicationHandler(webapp.RequestHandler):
    """Base class for all handlers.
    
    Add there methods/helpers that can be used by all handlers, 
    such as greetings, logout messages, etc."""
    def CommonValues(self):
        values = {}
        values["tabs"] = [
            dict(text="Acceuil", url="/"),
            dict(text="Classements", url="/ranking"),
            dict(text="Questions", url="/question"),
        ]
        user = users.get_current_user()
        if not user:
            values["tabs"].append(dict(text="Login",
                                       url=users.create_login_url("/")))
        else:
            values["tabs"].append(dict(text="Mon profil",
                                       url=users.create_logout_url("/")))
            values["tabs"].append(dict(text="Deconnecter",
                                       url=users.create_logout_url("/")))
        return values