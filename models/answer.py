from google.appengine.ext import db
from user import User
from question import Question 

class Answer(db.Model):
  
  user=  db.Reference(User)
  question= db.Reference(Question)
  score=db.StringProperty()
