import re

#========The beginning of the class==========
class Shoe:
    #initalising function with attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    #method to fetch cost of shoe
    def get_cost(self):
        return self.cost
    #method to fetch quantity of shoe
    def get_quantity(self):
        return self.quantity
    #print attributes as formatted string method
    def __str__(self):
        return (f"\n\nProduct Code: {self.code}\n\
Product Name: {self.product}\nCountry of Origin: {self.country}\nCost: R{self.cost}\nQuantity: {self.quantity}")


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    #using try except to open inventory as read only return 0 if file does not exist (EnvironmentError)
    try:
        with open('inventory.txt', 'r') as inventory:
            #store first line in headings variable
            headings = inventory.readline()
            for line in inventory:
                #for each line split line by comma, initalise a Shoe object with each attribute from inventory.txt
                #append shoe object to shoe list
                shoe_data = line.split(",")
                shoe_obj = Shoe(shoe_data[0], shoe_data[1], shoe_data[2], int(shoe_data[3]), int(shoe_data[4]))
                shoe_list.append(shoe_obj)
    except EnvironmentError:
        return 0

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    #collect country of origin for product
    usr_country = input("Enter the country of origin: ").strip(" ").capitalize()
    #collect product code continually query using a while loop until a valid code is entered
    while True:

        usr_code = input("Enter the product code: ").strip(" ").upper()
        #use regex to verify that product code is in form 'SKU12345'
        if re.search('SKU\d{5}', usr_code):

            break
        else:

            print("\nYou have entered an invalid product code")
    #enter the product name
    usr_product = input("Enter the product name: ").strip(" ").capitalize()
    #enter the cost using while loop and try except to continually query if cost is not a float
    while True:

        try:

            usr_cost = int(input("Enter the cost: "))
            break
        except ValueError:

            print("You have not entered a valid cost!")
    #enter the cost using while loop and try except to continually query if cost is not an int
    while True:

        try:

            usr_quantity = int(input("Enter the quantity: "))
            break
        except ValueError:

            print("You have not entered a valid quantity!")

    #create new shoe object and append to list
    new_shoe = Shoe(usr_country, usr_code, usr_product, usr_cost, usr_quantity)
    shoe_list.append(new_shoe)


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    #each shoe in object if iterated over and printed using --str-- method
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    #shoe list is sorted accoridng to quantity attribute
    shoe_list.sort(key=lambda x: x.quantity)
    #shoe quantity is stored in variable
    shoe_quantity = shoe_list[0].get_quantity()
    #message and shoe details printed 
    print(f"Restock required for:\n{shoe_list[0]}\n\nThere are {shoe_quantity} items remaining")
    #while loop to continually query user to select a menu option
    while True:
        #selecting y will update quantity, selecting n will allow user to return to menu
        select_function = input(('''\nWould you like to update the quantity for this item?:
y - Update Quantity
n - Return to Menu
\n: ''')).strip(" ").lower()

        if select_function == "y":
            #while loop used to collect new quantity
            while True:
                try:
                    #shoe.quantity attribute is updated with new value
                    new_quantity = int(input("\nEnter the new quantity: "))
                    shoe_list[0].quantity = new_quantity
                    break
                #if quantity is not an integer then error message printed
                except ValueError:
                    print("You have not entered a valid quantity!")
                    break
            break
        #if n selected then loop is broken to allow user to return to menu
        elif select_function == "n":
            break
        #error message if incorrect menu option selected
        else:
            print("You have not selected a valid option!")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    #use while loop to continually query user for code to search for
    while True:
        search_code = input("\nEnter the code for the product you would like to search for: ").upper()
        #use reg ex if statement to determine whether the search code is valid or not
        #re.search returns truthy and falsy values
        if re.search('SKU\d{5}', search_code):
            #shoe list iterated over to find the matching shoe by code attribute
            #when found the details are printed and loop is broken
            for shoe in shoe_list:
                if search_code == shoe.code:
                    print(f"\nFound item\n{shoe}")
                    break
            #if end of loop is reached and no shoe has been found a message is printed and loop broken
            else:
                print("Item not found!")
            break
        #message if invalid product code entered
        else:
            print("\nYou have entered an invalid product code")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    #for each shoe in list the value is calculated
    for shoe in shoe_list:
        #use the get cost and get quanitty method to fetch cost and quantity and print values
        shoe_value = shoe.get_cost() * shoe.get_quantity()
        #print shoe code, name and quantity along with calculated value
        print(f"\nProduct Code: {shoe.code}\nProduct Name: {shoe.product}\n\
Quantity: {shoe.quantity}\nTotal Value: R{shoe_value}")

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    #use sort method to sort list by quantity but in reverse
    shoe_list.sort(key=lambda x: x.quantity, reverse=True)
    #print the shoe details and a message stating it is for sale
    print(f"\nThe following product{shoe_list[0]}\n\nis now for sale!")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
#====Welcome Section====
# welcome message with border
print("\nWelcome to Warehouse Inventory Manager\n")
print("*"*50 + "\n" + "*"*50)
#if read_shoes_data returns 0 then the inventory file does not exist and program exits
if read_shoes_data() == 0:
    print("Inventory cannot be accessed! Please check inventory exists!")
    exit()
#====Main section====
#call login function and if true then execute the code in the loop
while True:
    #Menu title
    print("\n\nMenu\n")
    print("*"*50 + "\n" + "*"*50)
    menu = input('''\nSelect one of the following Options below:
v - View all stock
a - Add a new item
r - Check items due for restock
s - Search for an item
f - Check items for sale
h - Check stock value
e - Exit
\n: ''').lower()
    #call view function if v is selected
    if menu == 'v':
        view_all()
    #call capture_shoe fucntion if a is selected. 
    #Once a shoe has been added all the shoes in the inventory will be displayed
    elif menu == 'a':
        capture_shoes()
        view_all()
    #call the re_stock function if r is selected
    elif menu == 'r':
        re_stock()
    #call the search_soe function if s is selected
    elif menu == 's':
        search_shoe()
    #call the highest_qty function if f is selected
    elif menu == 'f':
        highest_qty()
    #call the value_per_item if h is selected
    elif menu == 'h':
        value_per_item()
    #print goodbye and exit if e is selected
    elif menu == 'e':
        print("\nGoodbye")
        exit()
    #print error message and continue loop if incorrect menu item is entered
    else:
        print("You have not selected a valid option!")

    #pauses the program until the user wants to continue
    input("\n\nPress Enter to return to the menu.")