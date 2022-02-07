#Building a container object
#Subject: inheritance

import csv

class PurchasedItem(object):
    counter = 0

    #define constructor
    def __init__(self, id, account, purchased_quantity, item_name, item_quantity, item_unit, item_price, category):
        PurchasedItem.counter += 1
        self.id = id
        self.account = account
        self.purchased_quantity = purchased_quantity
        self.name = item_name
        self.quantity = item_quantity
        self.unit = item_unit
        self.price = item_price
        self.category = category

    def __getattribute__(self, name):
        print("Getting:", name)
        return super().__gettattribute__(name)
    
    def __getattr__(self, name):
        print("Getting an attribute which doesn't exist!")
    
    def __setattr__(self, name, value):
        
        names = ('Id', 'account', 'purchased_quantity', 'quantity', 'name', 'unit', 'price', 'category')
        
        if name not in names:
            raise AttributeError("No attribute {}".format(name))
        
        print("Setting {} for {}".format(name))
        super().__setattr__(name, value)

    #private attribute
    @price.setter
    def price(self):
        return self._price
   
    def change_price(self, price):
        self.price = price

    @property
    def subtotal(self):
        return self.purchased_quantity * self.price

    @property
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError('Price must be a float')
        
        if value < 0:
            raise ValueError('Price must be >= 0')
        self._price = value
    
    def __repr__(self):
        return "PurchasedItem('{}', '{}', {}, '{}', {}, '{}', {}, '{}')".format(
            self.id, self.account, self.purchased_quantity, self.name,
            self.quantity, self.unit, self.price, self.category
        )

    def Reading_Shopping_Data():
        """
        Build a list of rows from a csv file
        """

        data = []
        with open(filename) as f:
            rows = csv.reader(f)
            header = next(f)
            for row in rows:
                row[2] = int(row[2])
                row[6] = float(row[6])

                item = PurchasedItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

                data.append(item)
        return data

class ShoppingCart(object):
    def __init__(self):
        self.items = []
    
    @classmethod
    def from_csv(cls, filename):
        self = cls()
        with open(filename) as f:
            rows = csv.reader(f)
            header = next(rows)
            for row in rows:
                row[2] = int(row[2])
                row[6] = float(row[6])
    
                obj = PurchasedItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                self.items.append(obj)
        
        return self
    
    def total(self):
        return "[{}]".format(", ".join([str(e) for e in self.items]))

    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        if isinstance(index, str):
            filtered_items = [item for item in self.items if index in item.name.lower()]
            new_cart = self.__class__()
            new_cart.items = filtered_items
            return new_cart
        
        else:
            return self.items[index]
        
    def __iter__(self):
        return self.items.__iter__()