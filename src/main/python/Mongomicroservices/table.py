from db import Database

class Table:
 def table(self):
  d=Database()
  col=d.db()
  col=col["customers"]
  return col
