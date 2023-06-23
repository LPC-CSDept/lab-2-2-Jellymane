def main():
   
    workhours = int(input('Enter your workhours: '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78
    

   ##################################################
   # Code your program here
   ##################################################
    overtime = workhours - reg_hours
    overtime_wage = overtime * ov_rate
    regular_wage = reg_hours * reg_rate
    total_wage = regular_wage + overtime_wage

    print(f"Regular hours is {reg_hours} Regular Charge is {regular_wage}")
    print(f"Overtime hours is {overtime} Overtime Charge is {overtime_wage:.2f}")
    print(f"Total wage is {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
