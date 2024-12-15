#Question 2 main

import question_b

def main():
     
    while True:

        print("MENU\n1-multiplication table\n2-Exit")
        option = int(input("Select 1 or 2: "))

        if option == 1:
            num1 = int(input("please enter the number for row: ")) #enter 10
            num2 = int(input("please enter the number for column: ")) #enter 5
            list = question_b.create_multiplication_table(num1, num2)
            question_b.display_multiplication_table(list, num1)

            while True:
                choice = input("Do you want to continue? y/n ").upper()

                if choice == 'Y':
                    break
                elif choice == 'N':
                    print("Exit")
                    exit()
                else:
                    print("Invalid value")
                    
        elif option == 2:
            print("Exit")
            break
            
        else:
            print("Invalid choice. Select 1 or 2")

main()