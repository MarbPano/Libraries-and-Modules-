#-------------------------#
#Functions
#Marb Pano
#==========================#
import random

#------inspiration-------#
def random_inspirational_words(List):#these parameters is to allow me to make diffirent varbs as dictionaries
    
    x = random.choice(List)
    print(x)
    
    return x
    
#------Printing dicts and lists----#
def print_operating_cost(operating_cost):#these parameters is to allow me to make diffirent varbs as dictionaries
    print("")

    for item, cost in list(operating_cost.items()):
        #for every item and cost in shopping_list print the {item} or key, {cost} or value. in dict
        print(f"{item}: ${cost}")
        
    return operating_cost
        
def print_employee_salary(employee_salary):#these parameters is to allow me to make diffirent varbs as dictionaries
    print("")
    
    for item, cost in list(employee_salary.items()):
        print(f"{item}: ${cost}")
        
    return employee_salary
        
    
        
def print_product_cost(product_cost):#these parameters is to allow me to make diffirent varbs as dictionaries
    print("")
     
    
    for item, cost in list(product_cost.items()):
        print(f"{item}: ${cost}")
        
    return product_cost
        
    


#------Adding info-------#    
def adding_employee_salary(employee_salary):#these parameters is to allow me to make diffirent varbs as dictionaries
    print(" ")
    
    while True:#the only problem with this is that if you have two employees with the same name, the more recent input employee
        #will overwrite the previous ones value
        try:
            for_question = int(input("How many Employees? "))
            
            for i in range(for_question):
                item = input("Emplyee Name: ")#the key in dictionary
                cost = float(input("Salary: "))#value in dictionary
                employee_salary[item] = cost#this is the only way I figured out how to add things to dictionary
            
            print("")   
            print("Contains")
            
            print_employee_salary(employee_salary)
            break
        
        except:
            print("ONLY USE NUMBERS(CONTINUE WHERE YOU LEFT OFF)")
            
    return employee_salary
    
    
def adding_operating_cost(operating_cost):#these parameters is to allow me to make diffirent varbs as dictionaries
    print("")
    
    while True:
        
        try:
            for item, cost in list(operating_cost.items()):
                
                x = float(input(f"Overall cost of {item} "))
                operating_cost[item] = x#i just wanted the value to change and not the set key
            
            print("")
            print("Contains")
            
            print_operating_cost(operating_cost)
            break# this is to exit out of the loop
            
        except:
            print("ONLY USE NUMBERS(CONTINUE WHERE YOU LEFT OFF") 
        
    return operating_cost
    
def adding_product_cost(product_cost):#these parameters is to allow me to make diffirent varbs as dictionaries
    print(" ")
    
    while True:
        try:
            for_question = int(input("How many Products? "))
            
            for i in range(for_question):
                item = input("Product Name: ")#the key in dictionary
                cost = float(input("Cost: "))#value in dictionary
                product_cost[item] = cost#this is the only way I figured out how to add things to dictionary
           
            print("")   
            print("Contains")
            
            print_product_cost(product_cost)
            break
        
        except:
            print("ONlY USE NUMBERS(CONTINUE WHERE YOU LEFT OFF)")
            
    return product_cost
    
def adding_cost(operating_cost,employee_salary,product_cost):#these parameters is to allow me to make diffirent varbs as dictionaries
    #to add up all the expenses so that we can calculate net income
    
    
    x = sum(value for key, value in operating_cost.items())#didnt know u can do this to this day 
    y = sum(value for key, value in employee_salary.items())#to add the values in each list
    z = sum(value for key, value in product_cost.items())
        
    a = x + y + z
           
    print(f"Overall Cost of Expenses: ${a}")
    
    return a

#-----removing things from lists-----#

def remove_operating_cost(operating_cost):#these parameters is to allow me to make diffirent varbs as dictionaries
    print("")#i WANTED only the value to be "removed" and not the key
    
    while True:
        
        print_operating_cost(operating_cost)
        
        expense = str(input('What Expense do you want removed?(Type "done" to exit) '))
        
        if expense == "done":#prety self explanatory
            break
        
        else:
            if expense in operating_cost: 
                operating_cost[expense] = 0#essentially not removing the value and making it "None" but change value to 0
                #this allows for math to be done, important for calc the net income
                
            else:
                print(f"{expense} is not in the Operating Cost") #fool proof
        
        print("") 
        
        print_operating_cost(operating_cost)#print often to show what is in list and what happen
        print("")
        
    return operating_cost
        
def remove_employee_salary(employee_salary):#these parameters is to allow me to make diffirent varbs as dictionaries
    print("")
    
    while True:
        print_employee_salary(employee_salary)
        
        employee = input('What Employee/Salary do you want removed?(Type "done" to exit) ')
        if employee == 'done':
            break
        
        else:
            if employee in employee_salary:
                del employee_salary[employee]#deletes the key along with value
                print_employee_salary(employee_salary)
                
            else:
                print(f"{employee} is not in the Employee List")
                
    return employee_salary

def remove_product_cost(product_cost):#these parameters is to allow me to make diffirent varbs as dictionaries
    #this function is created the same way basically as the remove_employee_salary() function 
    print("")
    
    while True:
        print_product_cost(product_cost)
        
        product = input('What Product do you want removed?(Type "done" to exit) ')#asking for specific key in dic
        
        if product == 'done':#i used your model so that whenever done is typed, it goes out of the loop 
            break
        
        else:
            if product in product_cost:
                del product_cost[product]#dont wanna make it too hard, so its better to just remove the key
                print_product_cost(product_cost)#i like to print the dict often to show user whats there and what was removed
                
            else:
                print(f"{product} is not in the Product Cost")
                
    return product_cost

#------TXT file work-------#

def save_list(operating_cost,employee_salary,product_cost):#these parameters is to allow me to make diffirent varbs as dictionaries 
    #the reason for saving the information onto a txt file is that it allows users to print the values in real life
    #a user can now print their business expenses into the real world, you can print what the user inputed here in this program.
    
    name = input("What is the name of the file? ")
    file = name + ".txt"
    #write mode makes it easier to edit the information, through running the program and removing and adding the info using this program
    #the purpose is to write the information down into the program, and then saving that information permanantly into a txt file to be printed or looked
    with open(file, 'w') as f:#to put every bit of information we recieve through this code into the same txt file
        f.write("===-----Business Expenses-----===")#the reason why this part is in writing mode is to clear the whole txt file just easier
        f.write('\n\n')#clearing the whole txt file so that any changes made are easily added and edited
        
        f.write('---Operating Costs---')
        for operating, cost in list(operating_cost.items()):
            f.write(f'\n{operating}: ${cost}')
            
    #add mode so that it does not clear everything         
    with open(file, 'a') as f:#to put every bit of information we recieve through this code into the same txt file
        f.write(f'\n\n')
        
        f.write('---Employees Salaries---')
        for employee, salary in list(employee_salary.items()):
            f.write(f'\n{employee}: ${salary}')
            
    #add mode so it does not clear the previous things saved      
    with open(file, 'a') as f:#to put every bit of information we recieve through this code into the same txt file
        f.write(f'\n\n')
        
        f.write('---Product Costs---')
        for product, cost in list(product_cost.items()):
            f.write(f'\n{product}: ${cost}')
            
        
            
            
    return file
    
            
def save_net_income(operating_cost,employee_salary,product_cost):#these parameters is to allow me to make diffirent varbs as dictionaries
    
    while True:
        question = str(input("""
        
    Options:
    1. Save and Read Current Txt File
    2. Exit 
    """))
        
        if question == '1':
            while True:
                
                try:
                        print('I NEED REVENUE...FOR CALCULATING...')
                        d = float(input("What was the business Total Revenue?(Only numbers) "))#gets the revenue
                        e = adding_cost(operating_cost,employee_salary,product_cost)
                                
                        net_income = d - e
                        
                        print(f"Net Income is ${net_income}")#after subtracting it prints
                        break
                        
                except:
                    print("ONLY INPUT NUMBERS")
                    
            file = save_list(operating_cost,employee_salary,product_cost)#now this way, the function above will be played first then it will go through this function
            
            #all the information that is going to be put down below are recieved by the questions above
            y = open(file, 'a')
            y.write('\n\n-----REVENUE-----')#header
            y.write(f'\n{d}')#writing down the revenue
            
            y.write('\n\n-----Operating Expenses-----')#header
            y.write(f'\n{e}')#writing down the operating expenses 
            
            y.write('\n\n-----NET INCOME-----')#header
            y.write(f'\n{net_income}')#writing down the net income
            y.close()
            
            
            x = open(file, 'r')#so we can see the results added in the txt file
            print(x.read())
            x.close#we need to close
            
            
        elif question == '2':
            break
        
        
    