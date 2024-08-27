class Employee:
    def __init__(self,id,name,email) -> None:
        self.id = id
        self.name = name
        self.email = email
    
   
class User_Database:
    def __init__(self) -> None:
        self.employees = []
    
    def add_emp(self,employee):
        self.employees.append(employee)
    
    def remove_emp(self,email):
        for em in self.employees:
            if em.email == email:
                self.employees.remove(em)
                return True
        return False
    
    def display(self):
        result ="Employee list are : \n"
        for index,em in enumerate(self.employees,start=1):
            result+= f"{index}. Id : {em.id}, Name : {em.name}, Email : {em.email}\n"
            print(result)



def main():
    db = User_Database()
    print("\nEmployee Managment System")
    while True:
        print('''
            1. Add Employee
            2. Remove Employee
            3. Display Employee 
            4. Exit
        ''')
        ch = input("Enter your choice : ")

        if ch=='1':
            id = int(input('Enter your ID : '))
            name = input('Enter your Name : ')
            email = input('Enter your Email : ')

            new_emp =Employee(id,name,email)
            db.add_emp(new_emp)
            print("Employee Added Successfully\n")
            

        elif ch == '2':
            email = input('Enter Email : ')
            if db.remove_emp(email):
                print("Employee remove successfully\n")
            else:
                print("Employee not found\n")
            
        
        elif ch == '3':
            db.display()
            
        elif ch == '4':
            print("You Exid the system")
            exit()
        else:
            print("Invalid choice, please choice correctly")

if __name__ == "__main__":
    main()


