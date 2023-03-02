
#========The beginning of the class==========

#Initiliaze class
class Shoe:

    '''
        This function initialises the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product 
        self.cost = cost
        self.quantity = quantity
       

    #method that returns cost of shoe
    def get_cost(self):
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    #method that returns quantity of the shoes
    def get_quantity(self):
        return self.quantity
    

    #returns string representation of the class
    def __str__(self):
        return (f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}")
        


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============


#Function to read all relevant shoe data
#Opens inventory - iterates through it as well as stripping and splitting for use
def read_shoes_data():
    with open("inventory.txt", "r") as file:
        temp = file.readlines()
            
    for x in temp:
        temp2 = x.strip()
        inventory_info = temp2.split(",")

        #Try - except fucntion for error handling
        #removes first line and appends everything else to shoe_list
        try:
            if inventory_info[0] == "Country":
                raise Exception
            shoe = Shoe(inventory_info[0], inventory_info[1], inventory_info[2], inventory_info[3], inventory_info[4])
            shoe_list.append(shoe)

        except Exception:
            del inventory_info
                

#Function to allow user to capture a shoe
#receives input with relevant info - uses this data to create show object that is then appended to the shoe list
def capture_shoes():
    print("To capture data about a shoe - some information is needed. Please fill out the relevant information. ")
    user_country = input("Country:  ")
    user_code = input("Code: ")
    user_product = input("Product: ")
    user_cost = input("Cost: ")
    user_quantity = input("Quantity: ")

    user_shoe = Shoe(user_country, user_code, user_product, user_cost, user_quantity)
    shoe_list.append(user_shoe)
    


#Iterates through shoes list and prints the details of the shoes from __str__function
def view_all():
    for x in shoe_list:
        print(x)
  

#Restock function - finds the show with the lowest quantity (one that needs to be restocked)
#ALlows the user to choose whether they would like to change the quantity -
#  if yes can input quantity and the new info is written back to inventory.txt

def re_stock():
    #relevant initilazer lists and counters
    restock_list = []
    lowest_quantity = 10000000

    #iterates through shoe_list
    #appends shoe object to list if the quantity is lower that the counter - then changes the counter to the quantity of that object
    #item with the lowest quantity by taking the last item from that list with [-1]
    #prints relevant low quantity item 
    for x in shoe_list:
        x = str(x)
        x = x.split(", ")
        if int(x[4]) < lowest_quantity:
            restock_list.append(x)
            lowest_quantity = int(x[4])     
    restock_item = restock_list[-1]
    restock_quantity = restock_item[-1]
    print(f"This is the information on the shoe with the lowest stock : {restock_item}\nThe current stock of this shoe is {restock_quantity}")
    
    #Takes input for changing quantity and reassigns quantity if Yes selected
    change_quantity = (input("Would you like to add to the quantity of this shoe? Y/N: "))
    if change_quantity == "y" or change_quantity == "Y":
        new_quantity = int(input("Input the new quantity of the shoe: "))
        restock_item[4] = new_quantity
    else:
        print("No changes have been made")
    

    #Code for writing new information to the file
    #Initializer lists
    category_headings = []
    final_item_list = []

    #reads from file
    with open("inventory.txt", "r") as file:
        temp = file.readlines()      
    for x in temp:
        temp2 = x.strip()
        inventory_info = temp2.split(",")

        if inventory_info[0] == "Country":
            category_headings.append(inventory_info)
            del inventory_info
        
        #deletes shoe object of the item that has been altered as to avoid doubles
        elif inventory_info[2] == restock_item[2]:
                del inventory_info
        
        #all other shoe objects appended to a final list
        else:
                final_item_list.append(inventory_info)
        
    #adds category heading that were seperated earlier to final_list to be written again
    final_item_list = category_headings + final_item_list

    #Now that the final_list doesn't include the unedited version of the shoe object 
    #This now appends the altered item to the final list
    final_item_list.extend([restock_item])

    #writes the final list to the file with correct formatting
    with open("inventory.txt", "w") as file:
        for sublist in final_item_list:
            line = "{},{},{},{},{}\n".format(sublist[0],sublist[1],sublist[2], sublist[3], sublist[4])
            print(line)
            file.write(line)



# Function searches through file and - determines which shoe matches code and outputs the relevant shoe
def search_shoe():

    #relevant input
    user_search = input("Please input the shoe code for the shoe you are searching for: ")

    #reading through file - easier to do this way than calling with read_shoes_data when making specific alterations
    with open("inventory.txt", "r") as file:
        temp = file.readlines()      
    for x in temp:
        temp2 = x.strip()
        inventory_info = temp2.split(",")
        if inventory_info[1] == user_search:
            print(f"The follow shoes match this code:\n{inventory_info}")
    print("If you did not receive information for your shoes - check your ID code and try again")
        


#Function finds all information from shoes and ouputs the final value alongside the all shoe info
#again uses try- except for error handling

def value_per_item():
    with open("inventory.txt", "r") as file:
        temp = file.readlines()  
    print(f"The total stock value for each shoe - displayed alongside shoe info:\n")
    for x in temp:
        temp2 = x.strip()
        inventory_info = temp2.split(",")
        try:
            if inventory_info[0] == "Country":
                raise Exception

            #calculation for calculting total_value
            total_value = int(inventory_info[3]) * int(inventory_info[4])

            
            print(f"{inventory_info}  --  Stock Value = ${total_value}\n")
        except Exception:
            del inventory_info
        

#function finds the highest quantity and outputs that shoe info
def highest_qty():

    #initial lists
    highest_quantity = 0
    highest_quantity_list = []

    #reads file
    with open("inventory.txt", "r") as file:
        temp = file.readlines()  
    for x in temp:
        temp2 = x.strip()
        inventory_info = temp2.split(",")
        try:
            if inventory_info[0] == "Country":
                raise Exception

            #Logic for determining which shoe has the highest quantity - appends successive highest inputs to list
            # similar startegy before that the hughest is then gained by using [-1] on list
            if int(inventory_info[4]) > highest_quantity:
                highest_quantity = int(inventory_info[4])
                highest_quantity_list.append(inventory_info)

          
        except Exception:
            del inventory_info
    print(f"""SALE recommendation - shoe with the highest quantity:
{highest_quantity_list[-1]}""")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

#Menu provides user with different selection for the relevant functions written.
#for each selection calls the relevant functions needed 
#if any inputs are chosen that are not in the list - else function catches them and reprompts the user 
while True:
    user_selection = input("""\nWould you like to: 
    1. View all the shoes
    2. Input/Capture shoe data
    3. Shoe Re-Stock
    4. Search for a shoe
    5. Item Value
    6. Highest Quantity (SALE)
    7. Quit application
    
    Enter Selection: """)

    if user_selection == "1":
        read_shoes_data()
        view_all()
    
    elif user_selection == "2":
        read_shoes_data()
        capture_shoes()
    
    elif user_selection == "3":
        read_shoes_data()
        re_stock()
    
    elif user_selection == "4":
        search_shoe()
    
    elif user_selection == "5":
        value_per_item()
    
    elif user_selection == "6":
        highest_qty()

    elif user_selection == "7":
        break

    else:
        print("Oops. There seems to have been a problem. Try again.")
