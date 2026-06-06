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

#Display Functions 

def display_employee_record(first_name, last_name, employee_id, hours, rate, gross_pay, deductions, total_net):
    print("=" * 50)
    print(" -- EMPLOYEE RECORDS --")
    print("=" * 50)
    print(f"Employee: {first_name} {last_name}")
    print(f" ID: {employee_id} | Hours: {hours} | Rate: {rate:.2f}")
    print(f"Gross: ${gross_pay:.2f} | Deductions: ${deductions:.2f} | Net: ${total_net:.2f} ")
    print("=" * 50)

def display_summary(total_employees, total_gross, total_deductions, total_net):
    print("=" * 50)
    print(" -- FINAL SUMMARY REPORT --")
    print("=" * 50)
    print(f"Total Employees Processed: {total_employees}")
    print(f"Total Gross: ${total_gross:.2f}")
    print(f"Total Deductions: ${total_deductions:.2f}")
    print(f"Total Net: ${total_net:.2f}")
    print("=" * 50)

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
        if first_name.upper() == "ESC":
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

        display_employee_record(first_name, last_name, employee_id, hours, rate, gross, deductions, net)  #We pass this info into the function, as its needed to run
        
    #This has to be out the While True loop to work     
    
    if total_employees > 0:
        display_summary(total_employees, total_gross, total_deductions, total_net)
    else:
        print("No employees were processed. ")
    

        
        


main()