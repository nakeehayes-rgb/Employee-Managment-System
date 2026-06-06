#Program that processes employee payroll records, calculates compensation with overtime, and gernerates summary reports. 

#Nakee Hayes
#CIS261
#Employee Managment System
#Phase 4

from datetime import datetime

class Employee:
    def __init__(self, first_name, last_name, employee_id, hours, rate, record_date_str=None):
        # Use self to store all parameters as attributes
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.hours = float(hours)
        self.rate = float(rate)
        self.record_date_str = record_date_str
        
        # Handle record_date: if None, use now(); if provided, convert string to datetime
        if record_date_str is None:
            self.record_date = datetime.now()
        else:
            self.record_date = datetime.strptime(record_date_str, "%Y-%m-%d")
            
        # Initialize financial attributes to 0.0
        self.gross_pay = 0.0
        self.deductions = 0.0
        self.net_pay = 0.0
        
        # Automatically call calculation methods
        self.calculate_gross_pay()
        self.calculate_deductions()
        self.calculate_net_pay()

    # Calculation methods
    def calculate_gross_pay(self):
        if self.hours > 40:
            self.gross_pay = (40 * self.rate) + ((self.hours - 40) * self.rate * 1.5)
        else:
            self.gross_pay = self.hours * self.rate

    def calculate_deductions(self):
        self.deductions = self.gross_pay * 0.25

    def calculate_net_pay(self):
        self.net_pay = self.gross_pay - self.deductions

    # Helper methods
    def worked_overtime(self):
        return self.hours > 40

    def is_high_earner(self, minimum=1000):
        return self.gross_pay >= minimum

    # File and display methods
    def to_file_string(self):
        # Cleaned up to use self.record_date matching your constructor
        date_str = self.record_date.strftime("%Y-%m-%d")
        return (
            f"{self.first_name}|{self.last_name}|{self.employee_id}|"
            f"{self.hours}|{self.rate}|{self.gross_pay}|"
            f"{self.deductions}|{self.net_pay}|{date_str}"
        )

    def __str__(self):
        date_str = self.record_date.strftime('%m/%d/%Y')
        return (
            f"Employee: {self.first_name} {self.last_name}\n"
            f"ID: {self.employee_id} | Hours: {self.hours} | Rate: ${self.rate:.2f}\n"
            f"Gross: ${self.gross_pay:.2f} | Deductions: ${self.deductions:.2f} | Net: ${self.net_pay:.2f}\n"
            f"Processed: {date_str}\n"
        )


class HRUser:
    def __init__(self, username, password, role, full_name):
        self.username = username
        self.password = password
        self.full_name = full_name
        if role in ["HR Manager", "HR Staff"]:
            self.role = role
        else:
            self.role = "HR Staff"


def create_default_users():
    manager = HRUser(
        username="hrmanager",
        password="hr2024",
        role="HR Manager",
        full_name="Admin User"
    )
    staff = HRUser(
        username="hrstaff",
        password="staff123",
        role="HR Staff",
        full_name="Staff User"
    )
    return [manager, staff]


def display_login_screen():
    print("=" * 50)
    print(" EMPLOYEE MANAGEMENT SYSTEM LOGIN")
    print("=" * 50)
    print("Please enter your credentials below to access the system.\n")


def authenticate_user(users, username, password):
    for user in users:
        if user.username.lower() == username.lower() and user.password == password:
            return user
    return None


def display_access_granted(username, role):
    print("\n" + "=" * 50)
    print(" ACCESS GRANTED")
    print("=" * 50)
    print(f"Welcome back, {username}!")
    print(f"Current System Role: {role}")
    print("-" * 50)
    if role == "HR Manager":
        print("Permissions: Full administrative access.")
        print(" -> Can process payroll, view reports, and manage user accounts.")
    elif role == "HR Staff":
        print("Permissions: Restricted access.")
        print(" -> Can view reports only. User management and data entry locked.")
    print("=" * 50 + "\n")


def display_access_denied():
    print("\n" + "!" * 50)
    print(" ACCESS DENIED: INVALID CREDENTIALS")
    print("!" * 50)
    print("The username or password you entered is incorrect.")
    print("The application will now shut down for security purposes.")
    print("=" * 50 + "\n")


def add_new_user(users):
    username = input("Enter new username: ")
    password = input("Enter password: ")
    role = input("Enter role (HR Manager or HR Staff): ")
    full_name = input("Enter full name: ")
    new_user = HRUser(username, password, role, full_name)
    users.append(new_user)
    print(f"Success! Created user profile for {username}.")


def display_all_users(users):
    print("\n--- User Directory ---")
    for user in users:
        print(f"Username: {user.username} | Role: {user.role} | Name: {user.full_name}")
    print("----------------------")


def save_users_to_file(users, filename):
    try:
        with open(filename, 'w') as file:
            for user in users:
                file.write(f"{user.username}|{user.password}|{user.role}|{user.full_name}\n")
    except Exception as e:
        print(f"Error saving user accounts: {e}")


def load_users_from_file(filename):
    users = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 4:
                    users.append(HRUser(parts[0], parts[1], parts[2], parts[3]))
        return users
    except FileNotFoundError:
        print(f"Notice: '{filename}' not found. Seeding default users.")
        return create_default_users()
    except Exception as e:
        print(f"Error loading users: {e}")
        return create_default_users()


def display_user_management_menu():
    print("\n--- User Management Menu ---")
    print("1. Add New User")
    print("2. View All Users")
    print("3. Return to Main Menu")
    print("----------------------------")


def manage_user_accounts(users, users_filename):
    while True:
        display_user_management_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_new_user(users)
            save_users_to_file(users, users_filename)
        elif choice == "2":
            display_all_users(users)
        elif choice == "3":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please pick 1, 2, or 3.")


def display_menu(role):
    print("\n" + "=" * 50)
    print(" MAIN MENU")
    print("=" * 50)
    if role == "HR Manager":
        print("1. Process Employee Records")
        print("2. View Reports")
        print("3. Manage User Accounts")
        print("4. Exit")
    elif role == "HR Staff":
        print("1. View Reports")
        print("2. Exit")
    print("=" * 50)


def get_menu_choice():
    return input("Enter your choice: ").strip()


def process_employee_records(filename):
    print("\n" + "=" * 50)
    print("PROCESS EMPLOYEE RECORDS")
    print("=" * 50)
    print("Instructions: Enter values. Type 'ESC' as First Name to finish.\n")
    
    employee_records = load_records_from_file(filename)
    while True:
        first_name = input("Enter first name: ").strip()
        if first_name.upper() == "ESC":
            break
        last_name = input("Enter last name: ").strip()
        employee_id = input("Enter employee ID: ").strip()
        try:
            hours = float(input("Enter hours worked: "))
            rate = float(input("Enter hourly wage rate: "))
        except ValueError:
            print("\n Error: Hours and rate must be numbers. Discarding this entry.\n")
            continue
            
        new_emp = Employee(first_name, last_name, employee_id, hours, rate)
        employee_records.append(new_emp)
        
        print("\nEmployee Added Successfully:")
        print(new_emp)
        
        save_records_to_file(employee_records, filename)


def view_reports(filename):
    employee_records = load_records_from_file(filename)
    if not employee_records:
        print("\nNotice: No employee records found in the database.")
        return
    generate_report(employee_records)


def generate_report(employee_records):
    print("\n" + "=" * 50)
    print(" COMPREHENSIVE PAYROLL REPORT")
    print("=" * 50)
    overtime_count = 0
    high_earners_count = 0
    gross_pays = []
    total_deductions = 0.0
    total_net = 0.0
    
    for count, emp in enumerate(employee_records, 1):
        print(f"Record #{count}")
        print(emp)
        
        gross_pays.append(emp.gross_pay)
        total_deductions += emp.deductions
        total_net += emp.net_pay
        
        if emp.worked_overtime():
            overtime_count += 1
        if emp.is_high_earner(minimum=1000):
            high_earners_count += 1
            
    total_employees = len(employee_records)
    total_gross = sum(gross_pays)
    average_gross = total_gross / total_employees
    highest_gross = max(gross_pays)
    lowest_gross = min(gross_pays)
    
    print("=" * 50)
    print(" FINAL SUMMARY STATISTICS")
    print("=" * 50)
    print(f"Total Employees Processed: {total_employees}")
    print(f"Total Gross Pay: ${total_gross:.2f}")
    print(f"Total Deductions: ${total_deductions:.2f}")
    print(f"Total Net Pay: ${total_net:.2f}")
    print(f"Average Gross Pay: ${average_gross:.2f}")
    print(f"Highest Gross Pay: ${highest_gross:.2f}")
    print(f"Lowest Gross Pay: ${lowest_gross:.2f}")
    print("-" * 50)
    print(f"Employees with Overtime (>40 Hours): {overtime_count}")
    print(f"High Earners (Gross >= $1,000.00): {high_earners_count}")
    print("=" * 50 + "\n")


def save_records_to_file(employee_records, filename):
    try:
        with open(filename, 'w') as file:
            for employee in employee_records:
                line = employee.to_file_string() + "\n"
                file.write(line)
        print(f"\nSuccess: Saved {len(employee_records)} records to '{filename}'.")
    except Exception as e:
        print(f"\nError saving records to file: {e}")

def load_records_from_file(filename):
    employee_records = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 9:
                    # Creates Employee objects (not dictionaries!)
                    employee = Employee(
                        first_name=parts[0],
                        last_name=parts[1],
                        employee_id=parts[2],
                        hours=parts[3],
                        rate=parts[4],
                        record_date_str=parts[8]
                    )
                    employee_records.append(employee)
        return employee_records
    except FileNotFoundError:
        print(f"\nNotice: '{filename}' not found. Starting with a fresh, empty database.")
        return []
    except Exception as e:
        print(f"\nError loading records from file: {e}")
        return []


#Input Functions

def get_employee_name():
    first_name = input("Enter your first name (or type 'ESC' to finish):  ")
    if first_name.upper() == "ESC":
        return "ESC", ""
    last_name = input("Enter your last name:  ")
    return first_name, last_name
    
def get_employee_id():
    return input("Enter your employee ID:  ")
    
def get_hours_worked():
    return float(input("Enter the numerical value of the hours you worked:  "))
    
def get_hourly_rate():
    return float(input("Enter the numerical value of your hourly wage:  "))

#Calculation Functions 

def calculate_gross_pay(hours, rate): 
    if hours > 40:
        return (40 * rate) + ((hours - 40) * rate * 1.5)
    return hours * rate

def calculate_deductions(gross_pay):
    return gross_pay * 0.25 

def calculate_net_pay(gross_pay, deductions):
    return gross_pay - deductions

def calculate_payroll_statistics(employee_records):
    gross_pays = [record['gross_pay'] for record in employee_records]
    if not gross_pays:
        return 0,0,0,0
    
    total_gross = sum(gross_pays)
    average_gross = total_gross / len(gross_pays)
    highest_gross = max(gross_pays)
    lowest_gross = min(gross_pays)

    return total_gross, average_gross, highest_gross, lowest_gross

#Display Functions 

def display_employee_record(first_name, last_name, employee_id, hours, rate, gross_pay, deductions, total_net):
    print("=" * 50)
    print(" -- EMPLOYEE RECORDS --")
    print("=" * 50)
    print(f"Employee: {first_name} {last_name}")
    print(f"ID: {employee_id} | Hours: {hours} | Rate: {rate:.2f}")
    print(f"Gross: ${gross_pay:.2f} | Deductions: ${deductions:.2f} | Net: ${total_net:.2f} ")
    print("=" * 50)

def display_summary(total_employees, total_gross, total_deductions, total_net, average_gross, highest_gross, lowest_gross):
    print("=" * 50)
    print(" -- FINAL SUMMARY REPORT --")
    print("=" * 50)
    print(f"Total Employees Processed: {total_employees}")
    print(f"Total Gross: ${total_gross:.2f}")
    print(f"Total Deductions: ${total_deductions:.2f}")
    print(f"Total Net: ${total_net:.2f}")
    print(f"Average Gross: ${average_gross:.2f}")
    print(f"Highest Gross: ${highest_gross:.2f}")
    print(f"Lowest Gross: ${lowest_gross:.2f}")
    print("=" * 50)

def display_all_employees(employee_records):
    print("=" * 50)
    print(" -- All PROCESSED EMPLOYEES --")
    print("=" * 50)
    for count, record in enumerate(employee_records, 1):
        print(f"\nEmployee Record #{count}")
        print("=" * 50)
        print(f"\nEmployee Name: {record['first_name']} {record['last_name']}")
        print(f"\nEmployee ID: {record['employee_id']}")
        print(f"\nHours worked: {record['hours']} | Pay rate: {record['rate']:.2f} ")
        print(f"\nGross pay: {record['gross_pay']:.2f} | Deductions: ${record['deductions']:.2f} | Net: ${record['net_pay']:.2f}")
        print(f"Processed: {record['date'].strftime('%m/%d/%Y')}")
        print("=" * 50)

def find_employee_by_id(employee_records, employee_id):
  
    return [record for record in employee_records if record['employee_id'].lower() == employee_id.lower()]


def find_employees_by_last_name(employee_records, last_name):

    return [record for record in employee_records if record['last_name'].lower() == last_name.lower()]


def find_overtime_employees(employee_records):

    return [record for record in employee_records if record['hours'] > 40]


def find_high_earners(employee_records, minimum_gross):

    return [record for record in employee_records if record['gross_pay'] >= minimum_gross]


def display_filtered_records(employee_records, filter_description):
    print(f"\n=== {filter_description} ===")
    print(f"Matching Records Found: {len(employee_records)}")
    
    if not employee_records:
        print("No matching records found.")
        return
        
    for count, record in enumerate(employee_records, 1):
        print(f"\n  [{count}] ID: {record['employee_id']} | Name: {record['last_name']}, {record['first_name']}")
        print(f"      Hours: {record['hours']} | Rate: ${record['rate']:.2f}")
        print(f"      Gross: ${record['gross_pay']:.2f} | Net: ${record['net_pay']:.2f}")
        date_str = record['date'].strftime("%Y-%m-%d") if isinstance(record['date'], datetime) else str(record['date'])
        print(f"      Record Date: {date_str}")


#Main Function

def main():
    # 1. Set filenames
    employees_filename = "employee_records.txt"
    users_filename = "hr_users.txt"
    
    # 2. Load users
    users = load_users_from_file(users_filename)
    
    # 3. Display login screen
    display_login_screen()
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    
    # 4. Authenticate
    current_user = authenticate_user(users, username, password)
    if current_user is None:
        display_access_denied()
        return  # Exit program completely
        
    # 5. Display access granted
    display_access_granted(current_user.username, current_user.role)
    
    # 6. Menu loop
    while True:
        display_menu(current_user.role)
        choice = get_menu_choice()
        
        # Route choices based on user roles
        if current_user.role == "HR Manager":
            if choice == "1":
                process_employee_records(employees_filename)
            elif choice == "2":
                view_reports(employees_filename)
            elif choice == "3":
                manage_user_accounts(users, users_filename)
            elif choice == "4":
                print("\nExiting Employee Management System. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter 1, 2, 3, or 4.")
                
        elif current_user.role == "HR Staff":
            if choice == "1":
                view_reports(employees_filename)
            elif choice == "2":
                print("\nExiting Employee Management System. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter 1 or 2.")
                
    # 7. Save users before exit
    save_users_to_file(users, users_filename)

# Change this at the very bottom of your file:
if __name__ == "__main__":
    main()

