#  Password and Profile Management Project

import random

class Innomatics:

    #class attributes
    institute_name = "Innomatics" 
    otp = random.randint(1,1000)
    serial_number_of_student = 0 #can be used while assigning registration code field.
    Users = {"Usernames":[],    #dataset
            "Users":[]}

        
    def user_registration________(self):
        # name = input("Enter name::")
        for user in Innomatics.Users["Users"]:
            if user["username"] == self.username:
                print("User already exists. Duplicate not added.")
                return

        Innomatics.Users["Users"].append({
        "name_of_user": self.name,
        "username": self.username,
        "password": self.pass_word,
        "course_enrolled": self.course_enrolled,
        "email": self.email,
        "phone_number": self.phone_number,
        "address": self.address
        })

        print("Profile added successfully.")
        
    #methods
    def user_registration(self):

        name = input("Enter name::")

        while True:

            username = input("Enter username::")

            if username in Innomatics.Users["Usernames"]:
                print("Username already exists.")

            else:
                password = f"Inno@{username}2026"
                course = input("Enter course::")

                Innomatics.Users["Users"].append({
                    "name_of_user": name,
                    "username": username,
                    "password": password,
                    "course_enrolled": course,
                    "email": "",
                    "phone_number": "",
                    "address": ""
                })

                Innomatics.Users["Usernames"].append(username)

                print("Password:", password)
                break
                
    def user_registration_(self):
        name = input("Enter name::")
        serial_number = f'Innomatics{Innomatics.serial_number_of_student}'
        while True: #Fails until a new user name is added.
            name_of_user = name
            user_name = input("Enter the username::") #user given user name
            pass_word = f'Inno@{user_name}2026' #default password
            course_enrolled = input("Enter the course you want to Enrol::")
            if user_name in Innomatics.Users["Usernames"]:
        
                print("Username already exists.")
            else:
                Innomatics.Users["Users"].append({"name_of_user":name_of_user,"username":user_name,"course_enrolled":course_enrolled, "password":pass_word}), 
                Innomatics.Users["Usernames"].append(user_name)
                Innomatics.serial_number_of_student += 1
                print("Your Password is",pass_word)
                break
    
    @classmethod        
    def login(cls,username, password):
        validity = False
        for i in cls.Users["Users"]:

            if(i["password"] == password) and username == i["username"]:
                name = i["name_of_user"]
                validity = True
                print(f"Log in Successful. Welcome {name} to {cls.institute_name}")
                return True
        print("Username not present. Please navigate to registration.")
        return False
    
   
    def show_details_(self,user_name,pass_word):
        name = ''
        institute = Innomatics.institute_name

        usernames = Innomatics.Users["Usernames"]
        validity = False
        username= ''
        for i in Innomatics.Users["Users"]:
            if(i["password"] == pass_word) and user_name == i["username"]:
                name = i["name_of_user"]
                validity = True
                
            
                username_position =  Innomatics.Users["Usernames"].index(user_name) if validity else 'No user name'
                username = Innomatics.Users["Usernames"][username_position]
                break
        return f"{(name).capitalize()}, is student of {institute}. Username of the student is {username}."
    def show_details(self, user_name, pass_word):
        # print(user_name,pass_word)
        for user in Innomatics.Users["Users"]:
            # print(user)
            if user["username"] == user_name and user["password"] == pass_word:
    
                print("-" * 40)
    
                for key, value in user.items():
                    if key != "password":
                        print(f"| {key:<12} | {str(value):<18} |")
    
                print("-" * 40)
                break
    
        else:
            print("No matching user found")    
    @staticmethod
    def logout():
        print("Logged out successfully. Thank You.!")
        

import random 
class PersonalAccountManager(Innomatics):

    @classmethod            
    def login(cls,username, password):
        validity = False
        for i in cls.Users["Users"]:

            if(i["password"] == password) and username == i["username"]:
                name = i["name_of_user"]
                validity = True
                print(f"Log in Successful.....! Welcome {name.capitalize()} to {cls.institute_name}")
                # break
                return True
        print("Username not present....! Press ok to navigate to registration.")
        return False
          
    #methods

    def check_if_user_is_present(self,username):

        for user in Innomatics.Users["Usernames"]:
            if user == username:
                return True
        else:
            return False
        
    def user_registration(self):
        name = input("Enter name::")
        serial_number = f'Innomatics{Innomatics.serial_number_of_student}'
        while True:
            name_of_user = name
            user_name = input("Enter the username::") #user given user name
            pass_word = f'Inno@{user_name}2026' #default password
            course_enrolled = input("Enter the course you want to Enrol::")
            if user_name in Innomatics.Users["Usernames"]:
        
                print("Username already exists.")
            else:
                Innomatics.Users["Users"].append({"name_of_user":name_of_user,"username":user_name,"course_enrolled":course_enrolled, "password":pass_word})
                Innomatics.Users["Usernames"].append(user_name)
                Innomatics.serial_number_of_student += 1
                print("Your Password is::",pass_word)
                break
    
    def changeName(self, username):

        new_name = ''

        for user in Innomatics.Users["Users"]:
            if username == user["username"]:
                new_name = user["name_of_user"]
                break

    
        while False:
    
            newpassword = input("Enter new password:: ")
    
            if newpassword == oldpassword:
                print("New password cannot be same as old password.")
                continue
    
            countspecial = 0
            countCapital = 0
            countNumber = 0
            countsmall = 0
    
            caps = [chr(x) for x in range(65, 91)]
            smalls = [chr(x) for x in range(97, 123)]
    
            for p in newpassword:
    
                if p in "!@#$%^&*()_+=<>.,":
                    countspecial += 1
    
                elif p in caps:
                    countCapital += 1
    
                elif p in smalls:
                    countsmall += 1
    
                elif p.isdigit():
                    countNumber += 1
    
            strong_Validity = (
                len(newpassword) >= 10 and
                countspecial > 0 and
                countNumber > 0 and
                countCapital > 0 and
                countsmall > 0
            )
    
            moderate_Validity = (
                len(newpassword) >= 8 and
                countspecial > 0 and
                countNumber > 0 and
                countCapital > 0 and
                countsmall > 0
            )
    
            if strong_Validity:
                print("Password is strong")
                break
    
            elif moderate_Validity:
                print("Password is moderate")
                break
    
            else:
                print("Password is weak. Try again.")
        enteredotp = int(input(f"Enter otp {Innomatics.otp} :: "))
        if enteredotp == Innomatics.otp:
    
            for user in Innomatics.Users["Users"]:
                if username == user["username"]:
                    user["name_of_user"] = name_of_user
                    break
    
            print("Name successfully changed.")
    
        else:
            print("Invalid OTP")
    def changePassword(self, username):

        oldpassword = ''

        for user in Innomatics.Users["Users"]:
            if username == user["username"]:
                oldpassword = user["password"]
                break
    
        print("Password must contain:")
        print("- atlease one special character from !,@,#,$,%,^,&,*,(,),_,+,=,<,>,.,,")
        print("- atleast one number.")
        print("- atlease one capital letter.")
        print("Password must contain atleast 8 characters.")
    
        while True:
    
            newpassword = input("Enter new password:: ")
    
            if newpassword == oldpassword:
                print("New password cannot be same as old password.")
                continue
    
            countspecial = 0
            countCapital = 0
            countNumber = 0
            countsmall = 0
    
            caps = [chr(x) for x in range(65, 91)]
            smalls = [chr(x) for x in range(97, 123)]
    
            for p in newpassword:
    
                if p in "!@#$%^&*()_+=<>.,":
                    countspecial += 1
    
                elif p in caps:
                    countCapital += 1
    
                elif p in smalls:
                    countsmall += 1
    
                elif p.isdigit():
                    countNumber += 1
    
            strong_Validity = (
                len(newpassword) >= 10 and
                countspecial > 0 and
                countNumber > 0 and
                countCapital > 0 and
                countsmall > 0
            )
    
            moderate_Validity = (
                len(newpassword) >= 8 and
                countspecial > 0 and
                countNumber > 0 and
                countCapital > 0 and
                countsmall > 0
            )
    
            if strong_Validity:
                print("Password is strong")
                break
    
            elif moderate_Validity:
                print("Password is moderate")
                break
    
            else:
                print("Password is weak. Try again.")
        enteredotp = int(input(f"Enter otp {Innomatics.otp} :: "))
        if enteredotp == Innomatics.otp:
    
            for user in Innomatics.Users["Users"]:
                if username == user["username"]:
                    user["password"] = newpassword
                    break
    
            print("Password successfully changed.")
    
        else:
            print("Invalid OTP")
                
    def changePassword_(self,username):
            
        oldpassword = ''
        # username = input("Enter username:: ")
        for name in Innomatics.Users["Users"]:
            if(username == name["username"]):
                oldpassword = name["password"]
                
        print("The password must have a special character from '!@#$%^&*()_+=<>.,', a number, a capital letter")
        newpassword = input("enter new password:: ")
        
        if newpassword == oldpassword:
            return 'New password cannot be same as old password.'
        countspecial = 0
        countCapital = 0
        countNumber = 0
        countsmall = 0
        
        caps = [chr(x) for x in range(65,65+26)]
        smalls = [chr(x) for x in range(97,97+26)]
        for p in newpassword:
            if p in "!@#$%^&*()_+=<>.,":
                countspecial += 1
            elif p in caps:
                countCapital += 1
            elif p in smalls:
                countsmall += 1
            elif p.isdigit():
                countNumber += 1

        strong_Validity = len(newpassword) >= 10 and countspecial > 0 and countNumber > 0 and countCapital > 0 and countsmall>0

        moderate_Validity = len(newpassword) >= 8 and countspecial > 0 and countNumber > 0 and countCapital > 0 and countsmall>0
            
           
        if strong_Validity:
            print("Password is strong")
        elif moderate_Validity:
            print("Password is moderate.")
        else:
            print("Password is weak. The password must be atleast have a special character from '!@#$%^&*()_+=<>.,', a number, a capital letter.")
       
        if moderate_Validity or strong_Validity:  
                
            enteredotp = int(input(f'enter otp {Innomatics.otp} :: '))
            
            
            if enteredotp == Innomatics.otp:
                for name in Innomatics.Users["Users"]:
                    if(username == name["username"]):
                        name["password"] = newpassword
                        break
                print(f"Password successfully changed.") #try to show old password here
            else:
                return "Invalid OTP"

#Profile Management and Tracking

class ProfileManagement(PersonalAccountManager):

    def __init__(self,name='', username='',courseenrolled='',email='',phone_number='',address=''):

        self.name = name
        self.username = username
        self.course_enrolled = courseenrolled
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.pass_word = f'Inno@{self.name}2026'
        # self.username = username
        self.progress_count = 0
        self.progress_percent = 0
            

    #track the progress of profile
    def _track_progress(self):

        for user in Innomatics.Users["Users"]:
    
            if user["username"] == self.username:
    
                fields = [
                    self.name,
                    self.username,
                    # self.pass_word,
                    self.course_enrolled,
                    self.email,
                    self.phone_number,
                    self.address 
                ]
    
                self.progress_count = sum(
                    1 for value in fields if value != '' and value != 0
                )
    
                self.progress_percent = (self.progress_count / len(fields)) * 100
    
                break
                

    def show_progress(self):
        
        if self.progress_count == 0:
            return (f"{(self.name).capitalize()} Complete the Profile Details.")
        else:    
            return (f"{(self.name).capitalize()}, Profile is {self.progress_percent}% completed.")
       
        
    #setters #edit the existing entity

    def setName(self,username):

        new_name = input(f"{username}, Edit Name::")
    
        for user in Innomatics.Users["Users"]:
            if user["username"] == username:
                user["name_of_user"] = new_name
                # self._track_progress()
                print("Name updated successfully.")
                break
    
        else:
            print("User not present.")
            
                
    def setUsername(self,username):

        new_username = input(f"{username}, Edit Username::")
    
        for user in Innomatics.Users["Users"]:
            if user["username"] == username:
                user["name_of_user"] = new_username
                # self._track_progress()
                print("Username updated successfully.")
                break
    
        else:
            print("User not present.")
                    

    def setCourse_Enrolled(self): 
        username = self.username
        new_course_enrolled = input(f"{username}, Edit Course to Enrol::")
        for user in Innomatics.Users["Users"]:
            if user["course_enrolled"] == self.course_enrolled:
                
                self.course_enrolled = new_course_enrolled
                user["course_enrolled"] = new_course_enrolled
                # self._track_progress()
                break
        else:
            print("User Not Present.")
            
    def setCourse_Enrolled(self,username):

        new_course_enrolled = input(f"{username}, Edit Username::")
    
        for user in Innomatics.Users["Users"]:
            if user["username"] == username:
                user["course_enrolled"] = new_course_enrolled
                # self._track_progress()
                print("Course updated successfully.")
                break
    
        else:
            print("User not present.")
            
    def setEmail(self,username):

        new_email = input(f"{username}, Edit Email::")
    
        for user in Innomatics.Users["Users"]:
            if user["username"] == username:
                user["email"] = new_email
                # self._track_progress()
                print("Email updated successfully.")
                break
    
        else:
            print("User not present.")
            
    def setPhoneNumber(self,username): 
        
        new_phone_number = input(f"{username}, Edit Phone Number::")
        for user in Innomatics.Users["Users"]:
            if user["username"] == username:
                # self.phone_number = new_phone_number
                user["phone_number"] = new_phone_number
                # self._track_progress()
                print("Phone Number updated successfully.")
                break
        else:
            print("User Not Present.")

    def setAddress(self,username): 
         # = self.username
        new_address = input(f"{username}, Edit Address::")
        for user in Innomatics.Users["Users"]:
            if user["username"] == username:
                
                # self.address = new_address
                user["address"] = new_address
                # self._track_progress()
                print("Address updated successfully.")
                break
        else:
            print("User Not Present.")
        


profile = ProfileManagement()

profile.Users
logged_in = False
current_user = ""


while True:

    username = ''
    password = ''
    print("-" * 35)
    print(f"| {'Choice':<10} | {'Operation':<18} |")
    print("-" * 35)
    print(f"| {'1':<10} | {'Register':<18} |")
    print(f"| {'2':<10} | {'Login':<18} |")
    print(f"| {'3':<10} | {'Change Password':<18} |")
    print(f"| {'4':<10} | {'Show Details':<18} |")
    print(f"| {'5':<10} | {'Edit Name':<18} |")
    print(f"| {'6':<10} | {'Edit Username':<18} |")
    print(f"| {'7':<10} | {'Edit Email':<18} |")
    print(f"| {'8':<10} | {'Edit Phone Number':<18} |")
    print(f"| {'9':<10} | {'Edit Address':<18} |")
    print(f"| {'10':<10} | {'Edit Course Name':<18} |")
    print(f"| {'11':<10} | {'Logout':<18} |")
    print(f"| {'12':<10} | {'Exit the Application':<18} |")
    print("-" * 35)
    

    choice = input("Choose option: ")

    if choice == "1":
        profile.user_registration()

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        result = profile.login(username, password)

        if result:
            logged_in = True
            current_user = username

    elif choice == "3":
        if logged_in:
            profile.changePassword(current_user)
        else:
            print("Login first")

            
    elif choice == "4":
        # username = input("Enter username: ")
        password = input("Enter password: ")
        if logged_in:
            profile.show_details(current_user,password)
        else:
            print("Login first")
            
    elif choice == "5":
        if logged_in:
            profile.setName(current_user)
            
        else:
            print("Login first")  
    
    elif choice == "6":
        if logged_in:
            profile.setUsername(current_user)
            
        else:
            print("Login first") 
    
    elif choice == "7":
        if logged_in:
            profile.setEmail(current_user)
            
        else:
            print("Login first") 
            
    elif choice == "8":
        if logged_in:
            profile.setPhoneNumber(current_user)
            
        else:
            print("Login first")             

    elif choice == "9":
        if logged_in:
            profile.setAddress(current_user)
            
        else:
            print("Login first") 
    elif choice == "10":
        if logged_in:
            profile.setCourse_Enrolled(current_user)
            
        else:
            print("Login first") 

    elif choice == "11":
        if logged_in:
            profile.logout()
            break
        else:
            print("Login first")

    elif choice == "12":
        # if logged_in:
        #     profile.logout()
        break
        # else:
        #     print("Login first")
    
    

    else:
        print("Invalid choice")

# profile.Users