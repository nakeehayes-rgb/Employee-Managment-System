#Program that processes employee payroll records, calculates compensation with overtime, and gernerates summary reports. 

#Nakee Hayes
#CIS261
#Employee Managment System
#Phase 2

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

def calculate_payroll_statistics(gross_pays):
    total_gross = sum(gross_pays)
    average_gross = sum(gross_pays) / len(gross_pays)
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

def display_all_employees(first_names, last_names, employee_ids, hours_list, rates_list, gross_pays, deductions_list, net_pays):
    print("=" * 50)
    print(" -- All PROCESSED EMPLOYEES --")
    print("=" * 50)
    for i in range(len(first_names)): #For every item in the list provide me the corresponding name #You can use this one index (i) to pull from other aligned lists 
        print(f"\nEmployee Record #{i + 1}")
        print("=" * 50)
        print(f"\nEmployee Name: {first_names[i]} {last_names[i]}")
        print(f"\nEmployee ID: {employee_ids[i]}")
        print(f"\nHours worked: {hours_list[i]} | Pay rate: {rates_list[i]} ")
        print(f"\nGross pay: {gross_pays[i]:.2f} | Deductions: ${deductions_list[i]:.2f} | Net: ${net_pays[i]:.2f}")
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

    #Initializing lists - to keep a record of entires

    first_names = []
    last_names = []
    employee_ids = []
    hours_list = []
    rates_list = []
    gross_pays = []
    deductions_list = []
    net_pays = []


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
        total_gross += gross #+= Means add and update 
        total_deductions += deductions
        total_net += net

        display_employee_record(first_name, last_name, employee_id, hours, rate, gross, deductions, net)  #We pass this info into the function, as its needed to run
        
        first_names.append(first_name) #This how we add to the lists we initilized 
        last_names.append(last_name)
        employee_ids.append(employee_id)
        hours_list.append(hours)
        rates_list.append(rate)
        gross_pays.append(gross)
        deductions_list.append(deductions)
        net_pays.append(net)


    #This has to be out the While True loop to work     
    display_all_employees(first_names, last_names, employee_ids, hours_list, rates_list, gross_pays, deductions_list, net_pays)
    

    if total_employees > 0:
        total_gross_calc, average_gross, highest_gross, lowest_gross = calculate_payroll_statistics(gross_pays)

        display_summary(total_employees, total_gross, total_deductions, total_net, average_gross, highest_gross, lowest_gross)
    else:
        print("No employees were processed. ")
    

        
        


main()