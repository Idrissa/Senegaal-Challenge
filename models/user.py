# -*- coding: utf-8 -*-

from google.appengine.ext import db


class User(db.Model):
  
  first_name=db.StringProperty(required=True)
  last_name=db.StringProperty()
  avatar=db.BlobProperty()
  email=db.StringProperty(required=True)
