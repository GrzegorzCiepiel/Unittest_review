# Python unittests practice #

At the outset of this topic, I must admit that using a Jupyter Notebook would be more readable, but I wrote these tests in PyCharm, and rewriting the code no longer makes sense.

## INTRODUCTION

### Sam's Surf Shop
Welcome to Sam’s Surf Shop! This project will exercise my knowledge of errors and unit testing practices in Python. It will also give  a small taste of testing a full application.

## TEST


The base is surfshop.py file with class ShoppingCart.
There are thre methods - add_surfboards that allows customer to add to cart from one to five boards,
set_checkout_date and apply_locals_discount

In the file test.py I build new class SurfshopTest which inherits from *unittest.TestCase*.

Firstly I test if after adding 1 surfboard to cart the right message will ocure.
Then test similar way for two and three surfboards. In one test I can not add more than 5 boards becose there is a rule that cart cannot have more than 5 surfboards.

Next I test that rule using *assertRaises* method. I also check functionality of *unittest.skip* decorator.

As the last test I check if apply_locals_discount method returns locals_discount as True.
