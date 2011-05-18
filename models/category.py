
import google.appengine.ext.db

class Categorie(db.Model):
   
   nom = db.StringProperty()
   created_at = db.DateTimeProperty(auto_now_add=True)


