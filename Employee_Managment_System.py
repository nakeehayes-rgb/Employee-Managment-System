#Program that processes employee payroll records, calculates compensation with overtime, and gernerates summary reports. 

#Nakee Hayes
#CIS261
#Employee Managment System
#Phase 3

from datetime import datetime

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

def save_records_to_file(employee_records, filename):
    try:
        with open(filename, 'w') as file:
            for record in employee_records:
                date_str = record['date'].strftime("%Y-%m-%d")
                
                line = (
                    f"{record['first_name']}|{record['last_name']}|{record['employee_id']}|"
                    f"{record['hours']}|{record['rate']}|{record['gross_pay']}|"
                    f"{record['deductions']}|{record['net_pay']}|{date_str}\n"
                )
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
                    record = {
                        'first_name': parts[0],
                        'last_name': parts[1],
                        'employee_id': parts[2],
                        'hours': float(parts[3]),
                        'rate': float(parts[4]),
                        'gross_pay': float(parts[5]),
                        'deductions': float(parts[6]),
                        'net_pay': float(parts[7]),
                        'date': datetime.strptime(parts[8], "%Y-%m-%d")
                    }
                    employee_records.append(record)
        return employee_records
    except FileNotFoundError:
        print(f"\nNotice: '{filename}' not found. Starting with a fresh, empty database.")
        return []
    except Exception as e:
        print(f"\nError loading records from file: {e}")
        return []


#Main Function

def main():
    print("=" * 50)
    print("EMPLOYEE MANAGEMENT SYSTEM ")
    print("=" * 50)
    print("Instructions:\n")
    print(" - Enter employee information when prompted.")
    print(" - Type 'ESC' to end return process or when finished.")
    print(" - Overtime is calculated at 1.5 for hours over 40 per week.")
    print(" - Deductions are calculated at 25% of gross pay (15% for Federal 5% for State and 5% for Benefits).\n")
    print("=" * 50)

    filename = "employee_records.txt"
    
    employee_records = load_records_from_file(filename)
    print(f"Loaded {len(employee_records)} existing records from file.\n")

    total_employees = 0
    total_gross = 0.0
    total_deductions = 0.0
    total_net = 0.0

    while True:
        first_name, last_name = get_employee_name() 
        if first_name.upper() == "ESC":
            break
            
        employee_id = get_employee_id() 
        hours = get_hours_worked()
        rate = get_hourly_rate()
        gross = calculate_gross_pay(hours, rate)
        deductions = calculate_deductions(gross)
        net = calculate_net_pay(gross, deductions)
        
        total_employees += 1 
        total_gross += gross 
        total_deductions += deductions
        total_net += net
        
        display_employee_record(first_name, last_name, employee_id, hours, rate, gross, deductions, net) 
        
        record = {
            'first_name': first_name,
            'last_name': last_name,
            'employee_id': employee_id,
            'hours': float(hours),
            'rate': float(rate),
            'gross_pay': float(gross),       
            'deductions': float(deductions),
            'net_pay': float(net),           
            'date': datetime.now()
        }
        employee_records.append(record) 

    save_records_to_file(employee_records, filename)

    if employee_records:
        display_all_employees(employee_records)
        
        total_gross_calc, average_gross, highest_gross, lowest_gross = calculate_payroll_statistics(employee_records)
        display_summary(total_employees, total_gross, total_deductions, total_net, average_gross, highest_gross, lowest_gross)
    else:
        print("No employees were processed.")

    print("\n" + "=" * 50)
    print("RUNNING FILTER & SEARCH UTILITIES")
    print("=" * 50)
    
    search_id = input("\nEnter an Employee ID to search for (or press Enter to skip): ").strip()
    if search_id:
        id_matches = find_employee_by_id(employee_records, search_id)
        display_filtered_records(id_matches, f"Search Results for ID: {search_id}")
        
    search_name = input("\nEnter a Last Name to search for (or press Enter to skip): ").strip()
    if search_name:
        name_matches = find_employees_by_last_name(employee_records, search_name)
        display_filtered_records(name_matches, f"Search Results for Last Name: {search_name}")
        
    ot_matches = find_overtime_employees(employee_records)
    display_filtered_records(ot_matches, "Employees with Overtime (> 40 Hours)")
    
    high_earners = find_high_earners(employee_records, 1000.00)
    display_filtered_records(high_earners, "High Earners (Gross Pay >= $1,000.00)")


main()