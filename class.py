class Person:
    def __init__(self, name, surname, age, email):
        try: 
            b = name.lower()
            ascii_range = range(97, 123, 1)
            for item in range(0, len(b)):
                if ord(b[item]) not in ascii_range:
                    raise ValueError("Name coudln't contain non-letter symbols")
                else:
                    self.__name = name
        except:
            print("Name coudln't contain non-letter symbols")
        try: 
            b = surname.lower()
            ascii_range = range(97, 123, 1)
            for item in range(0, len(b)):
                if ord(b[item]) not in ascii_range:
                    raise ValueError("Name coudln't contain non-letter symbols")
                else:
                    self.__surname = surname
        except:
            print("Name coudln't contain non-letter symbols")
        try:
            if age < 0:
                raise ValueError("Age couldn't be negative")
            if age > 140:
                raise ValueError("Age couldn't be so big")
            else:
                self.__age = age
        except:
            print("Please insert correct age")
        try:
            if "@" not in email:
                raise ValueError("You entered not mail adress")
            d = email.split("@")
            if len(d) != 2:
                raise ValueError("You entered not mail adress")
            if "." not in d[1]:
                raise ValueError("You entered not mail adress")
            try:
                e = d[1].split(".")
                check = len(e[0]) / len(e[1])
                check = len(e[1]) / len(e[0])
            except:
                raise ValueError("You entered not mail adress")
            else:
                self.__email = email
        except:
            print("You entered not mail adress")

    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        try:
            if new_age < 0:
                raise ValueError("Age couldn't be negative")
            if new_age > 140:
                raise ValueError("Age couldn't be so big")
            else:
                self.__age = new_age
        except ValueError as v:
            print(v)
        

       
a = Person("at", "b", 23, "admin@mail.ru")
a.set_age(115)
print(a.get_age())