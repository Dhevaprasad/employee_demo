employees = ["John", "Sarah", "Mike"]

def get_employees():
    return employees

def display_employees():
    print("Employee Directory")
    
    for index, employee in enumerate(employees, start=1):
        print(f"{index}. {employee}")

if __name__ == "__main__":
    display_employees()
