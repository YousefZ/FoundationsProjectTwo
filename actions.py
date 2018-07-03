# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "EShopper"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!\n" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    print("Welcome, This is a list of the stores you can shop from : ")
    for items in stores:
        print("* ",items.name)



def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!

    ''' FROM is previous Excerciseif order in menu or order in original_flavors or order in signature_flavors:
        #print("Correct")
        return True
    else : print("Sorry Item not in menu")
______________________
----------------------
Having an issue here by identifying Zara as part of stores, the check is not working, so testing with Zara value directly
----------------------


    '''
    if store_name == "Zara":
        print("correct Store Name: ",store_name)
        return store_name
    else:
        #print("Sorry invalid Store Name get_store func Entered Value ", store_name )
        return False




def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    

    # print('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.')
    # cust_entry=1
    # while cust_entry != "checkout":
    #     cust_entry=input()
    #     if cust_entry.lower()=="checkout":
    #         #Call checout method
    #         break
    #     if get_store(cust_entry) == False:
    #         print("No store with that name. Please try again.")
    #     else: 
    #         break
    # return 


    print('Pick a store by typing its name. ')
    cust_entry=" "
    while cust_entry != "checkout":
        cust_entry=input()
        for store in stores:
            if cust_entry == store.name:
                #print("Store Found 222")
                return store
        print("No store with that name. Please try again.")
    # if cust_entry == "Checkout":
    #     print("GoodBye")





'''
def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    order_item = 1
    print("What's your order? Type Exit to end your order: ")
    while order_item  != "exit":
        order_item= input()
        if order_item.lower()=="exit":

            break
        if is_valid_order(order_item.lower()) == True:
            #print("CheckedShouldAdd")
            order_list.append(order_item.lower())
   
    # your code goes here!

    #print(*order_list)
    return order_list

'''



# def pick_products(cart, picked_store):
#     """
#     prints list of products and prompts user to add products to card.
#     """
#     # your code goes here!
#     #print(products)
#     picked_store.print_products()

#     input_cart_item=""
#     print("please pick a product or type \"back\" to return to main menu")
#     input_cart_item = input()
#     while input_cart_item != "back":
#         for product in picked_store.products:
#             if input_cart_item.lower() == product.name.lower():
#                 print("item exists in store and added to cart")
#                 cart.add_to_cart(product)
#             else : 
#                 print("No Item with that name, please choose another product2")
#             input_cart_item = input()



def pick_products(cart, picked_store):
    picked_store.print_products()
    
    input_cart_item=input("please pick a product or type \"back\" to return to main menu: \n")
    while input_cart_item != "back":
        flag = False
        for product in picked_store.products:
            if input_cart_item.lower() == product.name.lower():
                cart.add_to_cart(product)
                print("++++++ added to cart +++++++ add more items? ")
                flag = True
                break
            
        
        if flag == False:
            print("There's No Item with that name, please choose another product or type \"back\" to return to main menu")
        input_cart_item=input()



def shop():
    cart = Cart()
    """
    The main shopping functionality
    """
    print_stores()
    store1 = pick_store()
    pick_products(cart,store1)
    receipt = cart.get_total_price()
    #cart.print_receipt()
    cart.checkout()



    #print("shop is called ", pick_store() )
    #pick_products(cart, pick_store())

    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)




'''Sources and Reference: 
# https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Importing_Modules    Importing Modules and Other items






'''
