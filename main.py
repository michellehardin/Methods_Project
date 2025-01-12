import pandas as pd
import numpy as np
from Inventory import Inventory
from Customer import Customer
from Order import Order

## username and password input for verify
verify = False
welcome_message = "WELCOME TO G8-BOOKSHOP"
account_info = "Account Information"
ordernumber = 1
while not verify:
    print("\n------------------------{welcome_msg}-------------------------\n".format(welcome_msg = welcome_message))
    username = input("UserName: ")
    #############################Create Customer Object
    customer = Customer(username)
    if customer.IsMember(): # check to see if user does not exists
        yesno = input("Not a registered user! Do you want to register (Y/n) ? ")
        if yesno.lower() =='y':
            password = input("Password: ")
            conf_password = input("Confirm Password:")
            if password != conf_password:
                print("Password did not match")  # print a message if different inputs
                continue  # restarts
            else:
                customer.addMember(username, password)
                verify = True
                print("\n------------------------{account_information}-------------------------\n".format(account_information = account_info))
                print("Creating Account")
                firstname = input("Please enter your First Name: ")
                lastname = input("Please enter your Last Name: ")
                customer.SetName(firstname, lastname)
                print("Welcome ", firstname, lastname)
                print("Please enter your shipping address:")
                add_number = input("Address number: ")
                Street = input("Street Name: ")
                city = input("City: ")
                state = input("State: ")
                zip = input ("Zip: ")
                customer.SetAddress(Street, add_number, city, state, zip)


        else:
            print ("Invalid input.")
            break
    else:
        password = input("Password: ")
        if customer.IsRightPassword(password):
            print("\n-----------------User has been identified, Welcome! {user} \n".format(user = username.upper()))
            verify = True
        else:
            print("Wrong Password, Try Again!")
        # print(customer.GetAddress())
##===================Verified
if verify:
    ######################Create Inventory Object
    inventory = Inventory()
    ######################Create Order Object
    order = Order(username)
    # View all items in a category
    inventory.print()

    while(1):
        # the user can see cart information, Delete account, Log out.
        print("\nPlease select from options below:\n")
        cdl = input("(A) Manage Account \n(I) View Inventory \n(C) Cart Options and Information \n(L) Log Out\n(E) Exit\n>>")

        if cdl.lower()=='l':
            customer.Logout()
        elif cdl.lower()=='i':
            inventory.print()


        elif cdl.lower()=='a':
            print("\n------------------------{account_information}-------------------------\n".format(account_information = account_info))

            print("MENU: ")
            account_option = input("(E) Edit account information \n(O) View Order History\n(D) Delete Account\n(B) Go Back \n>>")
            account_edit = True
            while account_edit:

                if account_option.lower()=='e':
                    account_option2 = input ("(A) Edit name \n(B) Edit Address\n>>")
                    if account_option2.lower()=='a':
                        firstname = input("Update First Name: ")
                        lastname = input("Update Last Name: ")
                        customer.SetName(firstname, lastname)
                        print("Account Information updated.")
                        account_edit = False
                    if account_option2.lower() == 'b':
                        streetNumber = input("Update Street Number: ")
                        streetName = input("Update Street Name: ")
                        city = input("Update city: ")
                        state = input("Update state: ")
                        zip = input("Update zip: ")
                        customer.SetAddress(streetName, streetNumber, city, state, zip)
                        print("Account Information updated.")
                        account_edit = False
                elif account_option.lower()=='o':
                    order.print()
                    account_edit = False
                elif account_option.lower() == 'd':
                    customer.DeleteAccount(order)
                elif account_option.lower()=='b':
                    account_edit = False
                else:
                    print("INVALID INPUT -- returning to main menu")
                    account_edit = False

        elif cdl.lower() == 'c':
            cart = customer.GetCart()
            cart_edit = True
            while cart_edit:
                # read card information
                cart.print()
                adcb = input("\n(A) Add to Cart\n(I) View Inventory\n(D) Delete from cart -- by ISBN number\n(C) Checkout\n(B) Go Back\n(V) View Cart\n>>")
                if adcb.lower()=='a':
                    isbn = input("\nInput ISBN number:")
                    quantity = input("Number of items:")
                    # cart list
                    if inventory.checkQuantity(isbn, quantity)==1:
                        cart.AddToCart(isbn, quantity)
                        cart.RemoveFromInventory(inventory)
                    elif inventory.checkQuantity(isbn, quantity)==0:
                        print('Inventory doesn\'t have enough quantity.')
                        continue
                    elif inventory.checkQuantity(isbn, quantity)==-1:
                        print('Invalid ISBN number.')
                        continue
                if adcb.lower()=='d':
                    isbn = input("\nInput ISBN number for the book you want to remove:")
                    cart.AddBackToInventory(inventory)
                    cart.RemoveFromCart(isbn)
                elif adcb.lower()=='c':
                    cart.checkout(inventory, order)
                    cart_edit = False
                elif adcb.lower() == 'u':
                    inventory.print()
                elif adcb.lower() == 'v':
                    cart.print()
                elif adcb.lower() == 'i':
                    inventory.print()
                elif adcb.lower()=='b':
                    cart_edit = False
                else: 
                    print("Please select from the options below:")

