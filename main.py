import admin as admin
from user import  Application
user=Application(str,str,str,str,str)

temp_variable=1
temp=True
Temp_var=True
while Temp_var :

    inp=int(input("Where You Want to Login?? 1. Admin  2. User  3.  Registration 4. Leave "))
    if temp_variable == 0:
        temp=True

    if inp == 1:
       print("Login as Admin ")
       username=input("Enter your Username  ")
       password = input("Enter your Password  ")
       if admin.admin_details[username] == password:
         print("$$$$$LOGIN DONE$$$$ ")
         while Temp_var:
            admin_input = int(input(
                "Choose the  below options  1.Add new Dish 2.Remove Dish 3.Edit Dish Name 4.View Menu List  5.leave"))
            if admin_input == 1:
                admin.add_new_dishes()
            elif admin_input == 2:
                admin.edit_food_item()
            elif admin_input == 3:
                admin.display_menu_item()
            elif admin_input == 4:
                admin.remove_food_item()
            elif admin_input == 5:
                print(f"You  are Exit to the admin pane  {username}")
                Temp_var = False
            else:
                print("Wrong input Please Read Carefully Instruction  !!!")

       else :
           print("Invalid  ")


    elif inp == 2 :
      print("Login as User ")
      email_enter = input("Enter your Email ")
      password = input("Enter your Password")

      if Application.login(email_enter,password):

        while temp:
            choice_user = int(input(f"{email_enter},Enter the option 1. Place your order 2. your Order history 3. Update Profile 4. Leave "))
            if choice_user == 1:
                user. place_your_order()

            elif choice_user == 2:
                user.order_history_view()

            elif choice_user ==3:
                user.profile_update()
                temp=False
                temp_variable=0

            elif choice_user == 4:
                print("$$$$$$$$ LOGOUT DONE $$$$$$$")
                temp = False
                temp_variable = 0

            else:
                print("Invalid  Number  follow this Instruction  ")

    elif inp == 3:

      new_email = input("Enter new  Email ")
      if new_email in user.login_details.keys():
        print("Email Already Registered.......")
      else :
        print("$$$$$Enter the Detail $$$$$")
        new_name = input("Enter new  Name ")
        new_phone_no = int(input("Enter new  contact No "))
        new_Address = input("Enter new  Address ")
        new_password = input("Enter new  Password  ")
        user=Application(new_email,new_name,new_phone_no,new_Address,new_password)

        print("$$$$$$$$ Registered Successfully $$$$$$$$$$")
        print("Login  ")


    elif inp == 4:
        Temp_var=False
        exit()

    else :
      print("follow the options")




