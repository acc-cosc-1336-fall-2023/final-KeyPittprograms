#Question 3 main

import question_c

def main():
    while True:
        print("MENU\n1-Display stock purchase history\n2-Exit")
        option = int(input("Select 1 or 2: "))

        if option == 1:
            stock_list = question_c.get_stock_list()

            for stock in stock_list:
                print(stock.get_symbol() + " " + stock.get_company_name())

        elif option == 2:
            print("Exit")
            break
            
        else:
            print("Invalid choice. Select 1 or 2")

main()