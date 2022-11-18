from table  import Table

class Data:
 def insert(self):
    t=Table()
    myList=[{"CardType": "VISA","carts": ["Cosmetics", "Groceries"]},{"CardType": "MasterCard","carts": ["Cosmetics", "Appliances"]},{"CardType": "RuPay","carts": ["Cosmetics", "Groceries", "Appliances"]}]
    print(myList)
    col=t.table()
    x=col.insert_many(myList)
    ids=x.inserted_ids
    return ids
