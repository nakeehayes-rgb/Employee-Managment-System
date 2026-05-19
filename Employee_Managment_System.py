#Program that processes employee payroll records, calculates compensation with overtime, and gernerates summary reports. 

#Nakee Hayes
#CIS261
#Employee Managment System
#Phase 1

#Input Functions

def get_employee_name():
    first_name = input("Enter your first name (or type 'ESC' to finish):  ")
    if first_name.upper() == "ESC":
        return "ESC", ""
    
    last_name = input("Enter your last name:  ")
    return first_name, last_name
    
def get_employee_id():
    employee_id = input("Enter your employee ID:  ")
    return employee_id

def get_hours_worked():
    hours = float(input("Enter the numerical value of the hours you worked:  "))
    return hours

def get_hourly_rate():
    rate = float(input("Enter the numerical value of your hourly wage:  "))
    return rate


#Calculation Functions 

def calculate_gross_pay(hours, rate): 
    gross_pay = hours * rate
    if hours > 40:
        standard_hours = 40
        overtime_hours = hours - 40 
        overtime_pay = overtime_hours * rate * 1.5
        gross_pay = overtime_pay + standard_hours * rate
        return gross_pay
    else:
        return gross_pay

def calculate_deductions(gross_pay):
    deductions = gross_pay * 0.25 
    return deductions

def calculate_net_pay(gross_pay, deductions):
    total_net = gross_pay - deductions
    return total_net

#Display Functions 

def display_employee_record(first_name, last_name, employee_id, hours, rate, gross_pay, deductions, total_net):
    employees = []
    print("=" * 50)
    print(" -- EMPLOYEE RECORDS --")
    print("=" * 50)
    print(f"Employee: {first_name} {last_name}")
    print(f"Employee ID: {employee_id}")
    print(f"Hours Worked: {hours}")
    print(f"Hourly Rate: {rate}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Deductions: ${deductions:.2f}")
    print(f"Net Pay: ${total_net:.2f} ")
    print("=" * 50)
    return first_name, hours, rate, gross_pay, deductions, total_net

def display_summary(total_employees, total_gross, total_deductions, total_net):
    print("=" * 50)
    print(" -- SUMMARY REPORTS --")
    print("=" * 50)
    print(f"Total Employees Processed: {total_employees}")
    print(f"Total Gross: ${total_gross:.2f}")
    print(f"Total Deductions: ${total_deductions:.2f}")
    print(f"Total Net: ${total_net:.2f}")
    print("=" * 50)
    return total_employees, total_gross, total_deductions, total_net

#Main Function

def main():
    print("=" * 50)
    print("EMPLOYEE MANAGMENT SYSTEM ")
    print("=" * 50)
    print("Instructions:\n")
    print(" - Enter employee information when prompted.")
    print(" - Type 'ESC' to end return process or when finsihed.")
    print(" - Overtime is calculated at 1.5 for hours over 40 per week.")
    print(" - Deductions are calculated at 25% of gross pay ( 15% for federal 5% for State and 5% for Benefits.\n")
    print("=" * 50)

    #Initalized four counters before the loop.. for memory of the totals  
    total_employees = 0
    total_gross = 0.0
    total_deductions = 0.0
    total_net = 0.0

    while True:
        first_name, last_name = get_employee_name() #Here we are Unpacking - getting info out of a function
        if first_name == "ESC":
            break
        employee_id = get_employee_id() #Since I used return when defining the function, i have to assign it a varible when calling it. 
        hours = get_hours_worked()
        rate = get_hourly_rate()

        gross = calculate_gross_pay(hours, rate)
        deductions = calculate_deductions(gross)
        net = calculate_net_pay(gross, deductions)

        total_employees += 1 #We use this formatting to update the totals. += means add to count
        total_gross += gross 
        total_deductions += deductions
        total_net += net
        
    #This has to be out the While True loop to work     
    display_employee_record(first_name, last_name, employee_id, hours, rate, gross, deductions, net) #We pass this info into the function, as its needed to run
    if len(first_name) > 0:
            print("No summary to display.")
    else:
            display_summary(total_employees, total_gross, total_deductions, total_net)
    

        
        


main()