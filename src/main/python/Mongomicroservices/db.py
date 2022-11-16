from conn  import Mongo

class Database:
 
 def db(self):
  m=Mongo()
  client=m.connection()
  db = client["mydatabase"]
  return db
