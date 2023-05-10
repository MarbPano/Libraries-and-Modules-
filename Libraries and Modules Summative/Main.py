#-------------------#
#libraries and Modules Summative
#By Marb Pano
#May 1
#------------------#
#------python modules-------#
import time

#------My own modules--------#
from sources import functions as f
from sources import dictionaries as d
from sources import varbs as intro 

def demonstration():
    
    a = intro.hello#taking varbs from 'varbs' and assigning them to these varbs and printing
    b = intro.intro
    c = intro.hope
    d = intro.begin
    
    print(a)
    time.sleep(2)
    
    print(b)
    time.sleep(2)
    
    print(c)
    time.sleep(3)
    
    print(d)
    time.sleep(4)
   
    
def dictionary():
    I = d.inspirational_words

    #Dicts Assigned to Varbs
    #this is easier because now I only need to put one thing
    #in parameter of functions
    O = d.operating_cost#operating cost = O
    E = d.employee_salary#employee salary = E
    P = d.product_cost#product cost = P
    
    return O,E,P,I

def main():
    O,E,P,I = dictionary() 
    
    while 1:
        print("") 
        f.random_inspirational_words(I)
        
    #asking a question #I used "str" to solve constant error for when you put random things in the input
        question = str(input("""
    Options:
    1. Print Current List's 
    2. Add Items to lists's 
    3. Remove Items from List's
    4. Pre-Tax Net Income
    5. Save list into TXT
    6. Exit
    """))
        
        if question == "1":#simply printing 
            
            print("Operating Cost")
            f.print_operating_cost(O)
            print("")
            
            print("Employee's Salaries") 
            f.print_employee_salary(E)
            print("")
            
            print("Product Cost's")
            f.print_product_cost(P)
            print("")
            
            e = f.adding_cost(O,E,P)
            
            
        elif question == "2":#adding items from lists
            
            while True:
                add_question = str(input("""
    What list do you want to Add To?

    1. Operating Cost
    2. Employee's Salaries
    3. Product Cost's
    4. Exit
    """))#since we are working with many lists
                
                if add_question == "1":
                    f.adding_operating_cost(O)
                   
                    
                elif add_question == "2":
                    f.adding_employee_salary(E)
                    
                    
                elif add_question == "3":
                    f.adding_product_cost(P)
                    
                    
                elif add_question == "4":
                    break
                
                else:
                    print("ONLY USE NUMBERS ABOVE")#This is for when the anwser is given a integer but not 1,2,3,4
                    
              
                        
            
        
        elif question == "3":#removing items from lists
            
            while True:
                remove_question = str(input("""
    What list do you want to Remove From?

    1. Operating Cost
    2. Employee's Salaries
    3. Product Cost's
    4. Exit
    """))#since we are working with many lists
                
                if remove_question == "1":
                    f.remove_operating_cost(O)
                   
                    
                elif remove_question == "2":
                    f.remove_employee_salary(E)
                    
                    
                elif remove_question == "3":
                    f.remove_product_cost(P)
                    
                    
                elif remove_question == "4":
                    break
                
                else:
                    print("ONLY USE NUMBERS ABOVE")#This is for when the anwser is given a integer but not 1,2,3,4
                
                
            
        
        elif question == "4":#net income 
            
            while True: 
            
                try:
                
                    d = float(input("What was the business Total Revenue?(Only numbers) "))#gets the revenue
                    e = f.adding_cost(O,E,P)
                            
                    net_income = d - e
                    
                    print(f"Net Income is ${net_income}")#after subtracting it prints
                    break
                    
                except:
                    print("ONLY NUMBERS")#fool proof so float numbers are inputed
                    continue 
                    
                                        
        elif question == "5":
            f.save_net_income(O,E,P)
            
        elif question == "6":
            time.sleep(3)
            break
        
        else:
            print("ONLY USE NUMBERS: 1,2,3,4,5")
            continue

#-----------Main Code-----------#
demonstration() 
main()