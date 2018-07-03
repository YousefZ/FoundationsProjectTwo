# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name    #Initializing the store with a name
        self.products = []  #Creating an empty list of products


    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product) 



    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        #print( "Name \t\t\t\t\t Description \t\t\t\t Price")
        
        print('{:20}'.format('Name'),'{:35}'.format('Description'),'{:40}'.format('Price'))
        print(70*"-")

        for item in self.products:
            print ("%s%s%s" % ('{:21}'.format(item.name),'{:30}'.format(item.description),'{:10}'.format(item.price)))



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
        return "%s %s%s" % (self.name, self.description, self.price )
        # return "{} {} {}".fomrat(self.name, self.description, self.price)


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!

        self.lops = []


    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.lops.append(product)
        #print("%s, Added to your cart" % product)



    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total_price=0
        # n=0
        #for n in lops[]
          #  total_price = total_price + self.price
        for item in self.lops:
            total_price += item.price
        return total_price 

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        
        print("\n-----Reciept-----\n")
        print('{:20}'.format('Name'),'{:35}'.format('Description'),'{:40}'.format('Price'))
        print(70*"-")
        for items in self.lops:
            #print("\n %s %s %0.3f" % (items.name, items.description, items.price) )
            print ("%s%s%s" % ('{:21}'.format(items.name),'{:30}'.format(items.description),'{:10}'.format(items.price)))
            continue

        print(70*"-","\n",70*"-")
        print ("The Total value for this cart is %0.3f is KWD : \n" %  self.get_total_price())  #Need to check 

    def checkout(self):
        """
        Does the checkout.
        """

        self.print_receipt()

        cust_choice = input("Please type \"confirm\" to complete your purchase or \"cancel\" to cancel your order\n")

        if cust_choice.lower() == "confirm":
            print("Your order has been placed")
        elif cust_choice.lower() == "cancel":
            print("Your order has been cancelled")






            #input_cart_item=input("please pick a product or type \"back\" to return to main menu: \n")




        # your code goes here!


""" Supporet Material :
Classes : 
https://docs.python.org/2/tutorial/classes.html
print :
https://www.codecademy.com/en/forum_questions/551c137f51b887bbc4001b73


"""

