# Inventory Manager
#### Description
This inventory manager takes in a text file containing the inventory of the warehouse and has the following functions\
Search products by code\
Determine the product with the lowest quantity and restock it\
Determine the product with the highest quantity\
Calculate the total value of each stock item\
The total value is calculated by multiplying the cost by the quantity for each item entered into the system.\

#### Contents
1.Installation\
2.Usage\
3.Credits

# Installation
Before you start the program please ensure you place **inventory.py** and a text file named **inventory.txt** in the same directory
**inventory.txt** should contain the product information in the following format
'''
Country,Code,Product,Cost,Quantity
'''

# Usage
## Menu
To start the program type
```
python inventory.py
```
into the command line

The displayed menu will present the following options
'''
v - View all stock
a - Add a new item
r - Check items due for restock
s - Search for an item
f - Check items for sale
h - Check stock value
e - Exit
'''

## Shoes Class
Attributes of class:
● country\
● code\
● product\
● cost\
● quantity\

o Inside
This class defines the following methods:\
▪ get_cost - Returns the cost of the shoes.\
▪ get_quantity -Returns the quantity of the shoes.\
▪ __str__ This method returns a string representation of a
class.\

## read_shoes_data
This function will open the file inventory.txt and read the data from this file, then create a shoes object and append this object into the shoes list. One line in inventory.txt should representd data to create one object of shoes. If the inventory is not in the same directory as the program then you will be prompted to add it to the directory.

## capture_shoes 
This function will allow a user to capture data about a shoe and use this data to create a shoe object and append this object inside the shoe list.

## view_all 
This function will iterate over the shoes list and print the details of the shoes returned from the __str__ function.

## re_stock 
This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked. Ask the user if they want to add this quantity of shoes and then update it. This quantity will be updated on the file for this shoe.

## search_shoe
This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.

## value_per_item
This function will calculate the total value for each item . The formula used is; value = cost * quantity. This information will be printed on the console for all the shoes.

## highest_qty 
This function will determine the product with the highest quantity and print this shoe as being for sale.

# Credit
Credit to HyperionDev for the specification
