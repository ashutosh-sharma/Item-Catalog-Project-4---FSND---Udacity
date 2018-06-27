""" Adding dummy data to database, this will add categories to the database """
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

### You can add items by just uncommenting the items below.

#Category : Indian Breads
cat1 = Category(id = 1, name = "Indian Breads")
session.add(cat1)
session.commit()
"""
item1 = Item(name = "Butter Naan", description = "butter naan desc", price = "Rs. 15.99", category = cat1)
session.add(item1)
session.commit()

item2 = Item(name = "Roti", description = "with salad", price = "Rs. 10.99", category = cat1)
session.add(item2)
session.commit()
"""

#Category : Fast Foods
cat2 = Category(id = 2, name = "Fast Food")
session.add(cat2)
session.commit()

"""
item = Item(name = "Dosa", description = "with sambhar and coconut", price = "Rs. 49.99", category = cat2)
session.add(item)
session.commit()

item = Item(name = "Chole Bhature", description = "with raita", price = "Rs. 49.99", category = cat2)
session.add(item)
session.commit()
"""

#Category : Beverages
cat3 = Category(id = 3, name = "Beverages")
session.add(cat3)
session.commit()

"""
item = Item(name = "Tea", description = "with nothing(coz its good without anything)", price = "Rs. 10.99", category = cat3)
session.add(item)
session.commit()

item = Item(name = "Coffee", description = "with great aroma", price = "Rs. 20.99", category = cat3)
session.add(item)
session.commit()
"""

#Category : Main Course
cat4 = Category(id = 4, name = "Main Course")
session.add(cat4)
session.commit()

"""
item = Item(name = "Paneer Tikka", description = "with great taste", price = "Rs. 69.99", category = cat4)
session.add(item)
session.commit()

item = Item(name = "Paneer Kofta", description = "with raita", price = "Rs. 69.99", category = cat4)
session.add(item)
session.commit()
"""

print("Categories added!")


