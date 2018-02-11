class Student:
    def __init__(self):
        self.fname=""
        self.lname =""

    def get_email(self):
        self.email = self.fname + self.lname + "@deerwalk.edu.np"
        return self.email.lower()

    def get_name(self):
        self.fname=input("enter your first name: ")
        self.lname=input("enter your last name: ")


s= Student()
s.get_name()
print("Your email is ",s.get_email())