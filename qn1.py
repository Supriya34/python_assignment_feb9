class UpperCase:
    def __init__(self):
        self.str = str

    def get_string(self):
        self.str = input("Enter the string: ")


    def print_string(self):
        print(self.str.upper())


u= UpperCase()
print(u.get_string())
print(u.print_string())