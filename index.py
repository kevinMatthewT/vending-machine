from typing import Final
from vending import machine
def make_list():
    shopping_list=[] 
    

    while True:
        number_amount=eval(input("Amount of different items to be bought: ")) 
        if number_amount<1: 
            print("One item must be bought at the least.")
        else:
            break 
    print("items available \n Chocolate:$1.00 , Chips:$0.50 , Soda:$1.25 , Juice:$0.75")
    for i in range (number_amount): 
        while True: 
            item_name=input("Name of Item: ")
            mass= eval(input("Number of this item to purchase: "))
            item=machine(item_name,mass)
            if item_name=="" or item.get_price()==0:
                    print("You need to enter a valid name.")
            elif mass<=0:
                    print("amount has to be more than 0")
            else:
                break
        shopping_list.append(item)

    return shopping_list 

def display(item_list):
    print("---------------------------------") 
    print("These are the items that you have purchased:")
    for i in range(len(item_list)):
        print(f"Item {i+1}") 
        print(item_list[i].total_price()) 
    

def cost_total(item_list):
    total=0
    for i in range(len(item_list)): 
        total += item_list[i].total_price()
    return total 

shopping_list=make_list() 
display(shopping_list)
print(f"Total amount: ${cost_total(shopping_list)}")

def bills():
    FinalCost=0
    while True:
            money_input=eval(input("Please enter your cash: ")) 
            if money_input == 1:
                FinalCost= money_input + FinalCost
                while True:
                    if FinalCost<cost_total(shopping_list):
                        print("Amount of money not sufficient")
                        money_input=eval(input("Please enter your cash: "))
                        FinalCost= money_input + FinalCost
                    else:
                        break
                break
            elif money_input == 2:
                FinalCost= money_input + FinalCost
                while True:
                    if FinalCost<cost_total(shopping_list):
                        print("Amount of money not sufficient")
                        money_input=eval(input("Please enter your cash: "))
                        FinalCost= money_input + FinalCost
                    else:
                        break
                break
            elif money_input == 5:
                FinalCost= money_input + FinalCost
                while True:
                    if FinalCost<cost_total(shopping_list):
                        print("Amount of money not sufficient")
                        money_input=eval(input("Please enter your cash: "))
                        FinalCost= money_input + FinalCost
                    else:
                        break
                break
            elif money_input == 20:
                FinalCost= money_input + FinalCost
                while True:
                    if FinalCost<cost_total(shopping_list):
                        print("Amount of money not sufficient")
                        money_input=eval(input("Please enter your cash: "))
                        FinalCost= money_input + FinalCost
                    else:
                        break
                break    
            else:
                print("Machine only accepts $bill of 1,2,5 & 20")
    
    money_cent = FinalCost * 100
    money_change = money_cent - cost_total(shopping_list)*100
    print(f"Here is your change:{int(money_change)}")

    
    change_penny = money_change// 25
    money_change=money_change-(change_penny*25)
    change_dime = money_change// 10
    money_change=money_change-(change_dime*10)
    change_nickel = money_change// 5
    money_change=money_change-(change_nickel*5)
    change_cent = money_change
    print(f"{int(change_penny)} pennies \n {int(change_dime)} dimes \n {int(change_nickel)} nickels \n {int(change_cent)} cents ")
   


print(bills())
