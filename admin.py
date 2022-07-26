admin_details={"Yashashri":"admin$123"}

menu_list={1:{'foodId':1,'Name':'puran poli','Quantity':12,'Price':70,'Discount':4,'Stock':10},
           2:{'foodId':2,'Name':'Misal paw','Quantity':23,'Price':150,'Discount':4,'Stock':40},
           3:{'foodId':3,'Name':'paw Bhaji','Quantity':22,'Price':150,'Discount':4,'Stock':60},
           4:{'foodId':4,'Name':'Dosa','Quantity':55,'Price':200,'Discount':4,'Stock':25},
           5:{'foodId':5,'Name':'delux thali','Quantity':30,'Price':800,'Discount':4,'Stock':30},
           6:{'foodId':6,'Name':'Bahuali Thali','Quantity':18,'Price':1200,'Discount':4,'Stock':15},
   
           }
food_id=3
def add_new_dishes():
    global food_id
    food_id+=1
    dish_name=input("Enter dish Name ")
    dish_quantity = int(input("Enter dish Quantity "))
    dish_price = int(input("Enter dish Price "))
    dish_discount = int(input("Enter dish Discount "))
    dish_stock = int(input("Enter dish Stock "))

    if food_id in menu_list.keys():
        print("This dish is already present,Add new dish")
    else :
        menu_list[food_id]={'foodId':food_id,
                            'Name':dish_name,
                            'Quantity':dish_quantity,
                            'Price':dish_price,
                            'Discount':dish_discount,
                            'Stock':dish_stock
                            }
        print("Deshes added is Successfully ")

def edit_food_item():
    
    item_id = int(input("Enter food item id "))
    if item_id in menu_list.keys():
        print("Id  is Correct You can Edit ")
        dish_name = input("Enter food item Name ")
        dish_quantity = int(input("Enter food item Quantity "))
        dish_price = int(input("Enter food item Price "))
        dish_discount = int(input("Enter food item Discount "))
        dish_stock = int(input("Enter food item Stock "))
        # Update the Menu 
        menu_list[item_id]['Name']=dish_name
        menu_list[item_id]['Quantity']=dish_quantity
        menu_list[item_id]['Price'] = dish_price
        menu_list[item_id]['Discount'] = dish_discount
        menu_list[item_id]['Stock'] = dish_stock
        print(f"{item_id}  is Updated Successfully!!!")

    else :
        print(f"{item_id}  is Not Present Inside the Menu List")


def display_menu_item():
    i=0
    for values in menu_list.values():
        i+=1
        print(i, values)

def remove_food_item():
    
    item_id = int(input("Enter food item id "))
    if item_id in menu_list.keys():
        del  menu_list[item_id]
        print(f"{item_id} is Deleted Successfully..!!!")
    else :
        print(f"{item_id} is Not Here in Menu List")
