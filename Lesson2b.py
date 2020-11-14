# A function:  a block of codes/statements performing specific task
# functions name should be in small letters
# Functions should not have spaces, use underscore
# before every function , put 2 empty lines
# A functions MUST be used/called
# Functions names are case sensitive


def welcome_home():
    print('=====Payroll calculator=====')



def payroll():
    basic_salary = 50000
    transport_allowance = 2300
    nssf = 0.02 * basic_salary
    nhif = 500

    # find gross
    gross_pay = basic_salary + transport_allowance
    print('Your Gross is KES ', gross_pay)
    print('Your Gross in USD', gross_pay/108)


    # find net pay
    net_pay = gross_pay - (nssf + nhif)
    print('Your Net is KES ', net_pay)
    print('Your Net in USD ', net_pay/108)





# Create a function to find Simple Interest : prt/100
def simple_interest():
    p  =60000
    r = 1.6
    t = 3

    interest = p*r*t/100
    print('Your Interest is ', interest)



# A function:  a block of codes/statements performing specific task
# functions name should be in small letters
# Functions should not have spaces, use underscore
# before every function , put 2 empty lines
# A functions MUST be used/called
# Functions names are case sensitive


def welcome_home():
    print('=====Payroll calculator=====')



def payroll():
    basic_salary = 50000
    transport_allowance = 2300
    nssf = 0.02 * basic_salary
    nhif = 500

    # find gross
    gross_pay = basic_salary + transport_allowance
    print('Your Gross is KES ', gross_pay)
    print('Your Gross in USD', gross_pay/108)


    # find net pay
    net_pay = gross_pay - (nssf + nhif)
    print('Your Net is KES ', net_pay)
    print('Your Net in USD ', net_pay/108)





# Create a function to find Simple Interest : prt/100
def simple_interest():
    p  =60000
    r = 1.6
    t = 3

    interest = p*r*t/100
    print('Your Interest is ', interest)

# Functions can have parameters and return values
# advanced

# below weight and height are parameters
# parameters don't have values
def body_mass_index(weight, height):
    bmi = weight/(height ** 2)
    print('Your BMI is ', bmi)




# below we call body_mass_index() and provide values for weight,height
body_mass_index(weight = 89.5, height=1.4)
body_mass_index(weight=70.4, height=1.8)
body_mass_index(height=1.5, weight=78.4)









# Advantages of using functions
# 1. Functions splits your code into smaller bits, making easy to manage, understand, maintain
# 2. The length of your source can be reduced functions
# 3. A function may be used by other programs, code reuse
























# Advantages of using functions
# 1. Functions splits your code into smaller bits, making easy to manage, understand, maintain
# 2. The length of your source can be reduced functions
# 3. A function may be used by other programs, code reuse

















