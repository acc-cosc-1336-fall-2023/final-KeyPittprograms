#Question D main

import question_d

def get_string():
    while True:
        dna_string = input("please enter the DNA string: ").upper()
        if len(dna_string) > 8 and len(dna_string) <= 16:
            return dna_string
        else:
            print("invalid string")

def get_substring():
    while True:
        dna_substring = input("please enter the DNA substring: ").upper()
        if len(dna_substring) == 4:
            return dna_substring
        
        else:
            print("invalid substring")

def main():

    while True:
        print("MENU\n1-Enter string,substring\n2-Exit")
        option = int(input("Select 1 or 2: "))

        if option == 1:
            dna_string1 = get_string()
            dna_string2 = get_substring()
            print(question_d.get_most_likely_ancestor_consensus(dna_string1, dna_string2))

        elif option == 2:
            print("Exit")
            break
            
        else:
            print("Invalid choice. Select 1 or 2")

main()