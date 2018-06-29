# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name    #Initializing the store with a name
        self.product = []  #Creating an empty list of products


    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.product.append(product) 



    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        print (self.name)



class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here! - This part is ok!

        self.name = name
        self.description=description
        self.price = price


    def __str__(self):
        # your code goes here! #!!!! TO MAKE LOOK NICER !! THIS IS BASIC
        #return (" "Product Name:",%d,"Product Description:", %d,"Price: ", %d" % (self.name, self.description, self.price)  )
        return "%d,%d,%d" % (self.name, self.description, self.price)


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.lops = []  #lops=listOfProducts

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.lops.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total_price=0
        n=0
        #for n in lops[]
          #  total_price = total_price + self.price
        return total_price 

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!



        print (self.get_total_price())  #Need to check 

    def checkout(self):
        """
        Does the checkout.
        """


        # your code goes here!


""" Supporet Material :
Classes : 
https://docs.python.org/2/tutorial/classes.html
print :
https://www.codecademy.com/en/forum_questions/551c137f51b887bbc4001b73


"""

