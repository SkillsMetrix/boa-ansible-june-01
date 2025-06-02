# CLASS
class Employee():
    uname=''
    email=''
    income=''

    # constructor to initialize the object
    def __init__(self,uname,email,income):
        self.uname=uname
        self.email=email
        self.income=income
    
    def __str__(self):
        return(f"{self.uname} , {self.email} , {self.income}")

  # Object
Manohar=Employee('Manohar CH','manohar@mail.com','123456')
Swati=Employee('Swati Arora','swati@mail.com','9870')

print(Manohar)
print(Swati)



        
