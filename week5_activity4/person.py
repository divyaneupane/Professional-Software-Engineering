#superclass
class Person: 

    def __init__(self,id,name):
        self.id=id
        self.name=name
        
        
    def display(self):
        return f"ID: {self.id}, Name:{self.name}"
    
    
#Student class inherit from person
class Student(Person):
    def __init__(self,id,student_id,name):
        #  It inherits id and name from Person.
        super().__init__(id,name)        #call parent constructor
        
        self.student_id=student_id
        
    
    def display(self):
        return f"Student Id: {self.student_id},Name: {self.name}"
    
    


#Staff class inherit from Person

class Staff(Person):
    def __init__(self,id,name, staff_id, tax_num):
        super().__init__(id,name)
        
        self.staff_id=staff_id
        self.tax_num=tax_num
        
    
    def display(self):
        return f"ID: {self.id}, Name:{self.name},Staff ID:{self.staff_id},Tax No:{self.tax_num}"
        
        
    
#General Staff inherits from staff

class General(Staff):
    def __init__(self,id,name,staff_id,tax_num,rate_of_pay):
        super().__init__(id,name,staff_id,tax_num)
        self.rate_of_pay=rate_of_pay
        
    
    def display(self):
        return f"ID:{self.id},Name:{self.name},Staff ID:{self.staff_id},Tax No:{self.tax_num},Rate of Pay:{self.rate_of_pay}"

 # Academic staff inherits from Staff.   
class Academic(Staff):
  
    def __init__(self, id, name, staff_id, tax_num, publications):
        super().__init__(id, name, staff_id, tax_num)
        self.publications = publications

    def display(self):
        return f"{super().display()}, Publications: {self.publications}"
    
    

if __name__ == "__main__":
    student = Student(1, "S101", "Alice")
    general_staff = General(2, "Bob", "ST201", "TX123", 30.5)
    academic_staff = Academic(3, "Dr Smith", "ST301", "TX789", 12)

    print(student.display())
    print(general_staff.display())
    print(academic_staff.display())