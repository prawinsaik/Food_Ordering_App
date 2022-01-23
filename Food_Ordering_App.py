class Restaurent:
    def __init__(self, res_name):
        self.R_name = res_name
        self.food = {}
        self.food_id = len(self.food)+1
        self.ordered_item = []
        self.personal_details = {}

# Admin functionalities
    def Add_Food_Items(self):
        try:
            self.name = input("Enter the food name: ")
            self.quantity = float(input("Enter the quantity: "))
            self.price = float(input("Enter the price: ₹ "))
            self.stock = float(input("Enter the stock in Kg: "))
            self.discount = float(input("Enter discount value: "))
            self.item = {"Name": self.name, "Quantity": self.quantity, "Price": self.price, "Discount": self.discount, "Stock": self.stock}
            self.food_id = len(self.food)+1
            self.food[self.food_id] = self.item
            print("\nFood Item: %s has been added successfully \n" %(self.food))
        except Exception as e:
            print("\n *-------Something went wrong once again try entering!-------*")

    def Remove_Food_Item(self):
        try:
            print("Do you really want to delete..?")
            k = int(input("Enter the food id you want to delete: "))
            if k in self.food.keys():
                del self.food[k]
                print("Item is deleted successfully..!")
                print("Remaining food items are: ", self.food)
            else:
                print("Please enter a valid ID..!")
        except Exception as e:
            print("\n *-------Something went wrong once again try entering!-------*")
            
    def Edit_Food_Item(self):
        try:
            self.Display_All_Food_Items()
            food_ID = int(input("Enter the food id you want to update: "))
            #{1: maggie, 2: noodle, 3: Dosa}        

            if food_ID in self.food.keys():
                print("Select the number from the list to update.... \n")
                print("1. Food name \n2. Quantity\n3. Price\n4. Discount\n5. Stock\n")
                k = int(input("Enter the number alone: "))
                if k == 1:
                    self.food[food_ID]["Name"] = input("Food Name: ")
                    print("Food name changed successfully !!\n")
                elif k == 2:
                    self.food[food_ID]["Name"] = int(input("Quantity: "))
                    print("Quantity of the food item changed successfully !!\n")
                elif k == 3:
                    self.food[food_ID]["Name"] = float(input("Price: "))
                    print("Price of the food item changed successfully !!\n")
                elif k == 4:
                    self.food[food_ID]["Name"] = float(input("Discount: "))
                    print("Discount on the food item changed successfully !!\n")
                elif k == 5:
                    self.food[food_ID]["Name"] = float(input("Stock left: "))
                    print("Stock of food item present changed successfully !!\n")
                else:
                    print("Please enter a number between 1 to 5..!")
            else:
                print("Invalid Entry...!")
        except Exception as e:
            print("\n *-------Something went wrong once again try entering!-------*")
                           
    def Display_All_Food_Items(self):
        print("\nList of all food items present are:\n")
        if len(self.food) != 0:
            for i in self.food:
                print("---> Food id :", i)
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print("\n")
        else:
            print("No Food Item is added !!!!!!!\n")

#User Functionalities
    def User_Registeration(self):
        try:
            while True:
                self.full_name = input("Enter your full name: ")
                self.phone_no = int(input("Enter your phone number: "))
                self.email = input("Enter your email : ")
                self.address = input("Enter the address: ")
                self.password = input('Enter the password: ')
                self.user_details = {"User Name": self.full_name, "Phone Number": self.phone_no, "Email ID": self.email, "Password": self.password, "Address": self.address}
                print("Cogratulations your account has been created successfully")
                print("Greeting from %s Restaurant\n" %(self.R_name))
                print("User Details: ")
                for i in self.user_details:
                    print(i, ':', self.user_details[i])
                break

        except Exception as e:
            print("\n *-------Something went wrong once again try entering!-------*")

    def User_Login(self):
        try:
            while True:
                email_id = input("Enter the email-id: ")
                password = input("Enter the password: ")
                if email_id == self.email:
                    if password == self.password:
                        print("Congratulations you have successfully logged in.")
                        while True:
                            print("\nChoose an option by entering a number\n")
                            k = int(input("1. Place New Order\n2. Check Order History\n3. Update Your Profile Details\n4. Exit\n"))
                            if k == 1:
                                self.Place_Order()
                            elif k == 2:
                                self.Ordered_History()
                            elif k == 3:
                                self.Update_Details()
                            elif k == 4:
                                break
                            else:
                                print("Invalid Number")
                    else:
                        print("\nIncorrect Password ...?\n")
                else:
                    print("\nNo Account found!\n\nPlease create a account first!!\n")
                    break
                break
        except Exception as e:
            print("\n!! Something went wrong please try again !!")  
                    
    def Place_Order(self):
        try:
            #Checking if there are any food items ...!
            if len(self.food) != 0:
                list_of_fooditems = []
                for items in self.food:
                    list_of_fooditems.append([self.food[items]["Name"], self.food[items]["Quantity"], self.food[items]["Price"]])
                print("\nMenu List...\n")                                    
                for k in list_of_fooditems:
                    print(k)
                print("\nChoose a number:")
                while True:
                    print("1. Place the Order\n2. Exit")
                    user_input = int(input())
                    if user_input == 1:
                        k = input("Enter the Food number separated by typing space: ").split(" ")
                        for num in k:
                            i = int(num)
                            if i <= len(list_of_fooditems):
                                self.ordered_item.append(list_of_fooditems[i-1])
                            else:
                                print("Please enter a valid number in the given range....!")
                        print("\nOrdered Items: ")
                        for num in self.ordered_item:
                            print(num)
                        print()
                    elif x == 2:
                        break
                    else:
                        print("\nInvalid Number....!\n")
            else:
                print("\nFood Items out of stock\n")
        except Exception as e:
            print("\n!! Something went wrong please try again !!")

    def Ordered_History(self):
        print("\nList of last order items: ")
        for i in self.ordered_item:
            print(i)

    def Update_Details(self):
        try:
            while True:
                print("Choose a number in order to Update your profile details\n")
                print("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Exit")
                num = int(input())                                    
                if num == 1:
                    self.user_details["User Name"]=input("Enter your full name : ")
                    print("\nName Changed Successfully...!\n")
                elif num == 2:
                    self.user_details["Phone No."]=int(input("Enter your updated 10 digit phone number : "))
                    print("\nPhone Number Changed Successfully...!\n")      
                elif num == 3:
                    self.user_details["Email_ID"]=input("Enter your updated email id : ")
                    print("\nEmail ID Changed Successfully...!\n")
                    
                elif num == 4:
                    self.user_details["Password"]=input("Enter your updated password : ")
                    print("\nPassword Changed Successfully...!\n")
                    
                elif num == 5:
                    self.user_details["Address"]=input("Enter your updated address with area PIN code ")
                    print("\nAddress Changed Successfully...!\n")
                    
                elif num == 6:
                    break
                else:
                    print("\nPlease a valid number\n")
                    continue
                    
                if num in [1, 2, 3, 4, 5]:
                    for i in self.user_details:
                        print(i, ":", self.user_details[i])
                else:
                    print("\nPlease Give Valid Input\n")
        except Exception as e:
            print("\n!! Something went wrong please try again !!")

try:
    def main():
        Res_Name = "Prawin's"
        Object = Restaurent(Res_Name)
        print("**--------------------- Greetings from %s Restaurant ---------------------**\n" %(Res_Name))
        print("\n**----------------------------- Hola Amigos -----------------------------**\n")
        while True:
            print("\n1. Admin\n2. User\n3. Exit")
            num = int(input())
            if num == 1:
                while True:
                    print("\n1. Add New Food Items\n2. Edit Food Items\n3. View Food Items \n4. Delete Food Items\n5. Exit")
                    x = int(input())
                    if x == 1:
                        Object.Add_Food_Items()
                    elif x == 2:
                        Object.Edit_Food_Item()
                    elif x == 3:
                        Object.Display_All_Food_Items()
                    elif x == 4:
                        Object.Remove_Food_Item()
                    elif x == 5:
                        break
                    else:
                        print("Invalid Number")
            elif num == 2:
                while True:
                    print("\nEnter the Below Options\n")
                    print("1. Register\n2. Login\n3. Exit")
                    x = int(input())
                    if x == 1:
                        Object.User_Registeration()
                    elif x == 2:
                        Object.User_Login()           
                    elif x == 3:
                        break
                    else:
                        print("\nInvalid Number ")        
            elif num == 3:
                break
            else:
                print("Invalid Number")
except Exception as e:
    print("something went wrong please give input carefully")
            
        # calling the main function 
        
if __name__ == "__main__":
    main()
    
print("THANK YOU, PLEASE VISIT AGAIN.")
                   
