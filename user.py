import admin as admin
class Application :
      login_details = {}
      def __init__(user,email,name,contact_no,address,password):
          user.email = email
          user.name = name
          user.contact_no = contact_no
          user.address = address
          user.password = password
          Application.login_details[user.email] ={'Email':user.email,
                                               'Full_Name':user.name,
                                               'contact_no':user.contact_no,
                                               'Address':user.address,
                                               'Password':user.password,
                                               }
          user.order_history = {}

      def place_your_order(user):
          print("What you want to order ")
          admin.display_menu_item()
          choice_user = int(input("select any option if you want to order 1.YES  2.NO"))
          if choice_user == 1:
              n=int(input("How many Item do You Want to Order "))
              total_bill=0
              total_discount=0
              for i in range(n):
                  itemid = int(input("Enter the Item id here: "))
                  quantity = int(input("Enter the quantity of the item: "))
                  total_bill = total_bill + admin.menu_list[itemid]['Price'] * quantity
                  total_discount += admin.menu_list[itemid]['Discount']
                  admin.menu_list[itemid]['Stock'] = admin.menu_list[itemid]['Stock']-quantity
# Add Item in User List
                  user.order_history[itemid] = {
                      "Name": admin.menu_list[itemid]["Name"],
                      "Price": admin.menu_list[itemid]["Price"],
                      "Quantity": quantity,
                  }
              confirmation_msg = input(" for confirmation--- Yes Otherwise NO ")
              if confirmation_msg == 'Yes':
                  print(f"Total Discount Allowed is {total_discount} ")
                  print(f"After Deduced Discount It costs is {total_bill-total_discount} INR in total")
                  print("You're order is successfully placed...")

              elif confirmation_msg=="No":
                  print("Your Order has been Cancelled ")
                  user.order_history.clear()

              else :
                  print("Invalid Input ")

          elif choice_user == 2:
              print("You Selected 2 option So we Cancelled This....")

          else:
              print(" Invalid no!!! ")


      def order_history_view(user):
        print(user.order_history)


      def profile_update(user):
          print("Update Profile")
          email=input("Enter Your Mail id ")
          if email in Application.login_details.keys():
              print("Email Matched !")
              del Application.login_details[email]

# update
              new_email=input("Enter new  Email ")
              new_name = input("Enter new  Name ")
              new_contact_no = int(input("Enter new  Phone No "))
              new_Address = input("Enter new  Address ")
              new_password = input("Enter new  Password ")

              Application.login_details[new_email] = {'Email': new_email,
                                                    'Full_Name': new_name,
                                                    'Phone_no': new_contact_no,
                                                    'Address': new_Address,
                                                    'Password': new_password,
                                                    }
              print("Profile Updated Successfully!!! ")

          else :
              print("Please Register your Email to login  ")

      @classmethod
      def login(cls, email, password):
          if  email in cls.login_details.keys():
              if cls.login_details.get(email)['Password'] == password:
                 print(f"logged in Successfully!!! {cls.login_details.get(email)['Full_Name']}")
                 return True
              else:
                 print("Email or password is not valid! ")
                 return False
          else:
              print(f"{email} This Email address is not registered , please register!")
              return False

