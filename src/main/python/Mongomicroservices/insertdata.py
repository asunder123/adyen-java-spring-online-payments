from table  import Table

class Data:
 
 def insert(self):
  t=Table()
  mylist = [
            { "name": "Amy", "address": "Apple st 652"},
              { "name": "Hannah", "address": "Mountain 21"},
                { "name": "Michael", "address": "Valley 345"},
                  { "name": "Sandy", "address": "Ocean blvd 2"},
                    { "name": "Betty", "address": "Green Grass 1"},
                      { "name": "Richard", "address": "Sky st 331"},
                        { "name": "Susan", "address": "One way 98"},
                          { "name": "Vicky", "address": "Yellow Garden 2"},
                            { "name": "Ben", "address": "Park Lane 38"},
                              { "name": "William", "address": "Central st 954"},
                                { "name": "Chuck", "address": "Main Road 989"},
                                  { "name": "Viola", "address": "Sideway 1633"}
                                  ]
  col=t.table()
  x=col.insert_many(mylist)
  ids=x.inserted_ids
  return ids
