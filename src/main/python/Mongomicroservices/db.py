from conn  import Mongo

class Database:
 
 def db(self):
  m=Mongo()
  client=m.connection()
  db = client["payment_1"]
  return db
