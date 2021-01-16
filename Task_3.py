contact_list = []

def add(lst, name, contact):
    for i in range( 0, len(lst)):
        if lst[i][0] == name :
            print('\nContact with name "'+name+'" already exist !!!')
            print('Do you want to add the number "'+contact+'" to the existing contact ?\nYes or No')
            if input() == "Yes":
                if contact in lst[i][1]:
                    print("----> Contact number with same name and number already exist !!!")
                else:
                    lst[i][1].append(contact)
                    print("----> Contact added successfully.")
            else:
                print("----> OK, contact is not added to existing contact.")
            break
        elif lst[i][0] > name:
            lst.insert(i, [name, contact.split()])
            print("----> Contact added successfully.")
            break
    else:
        lst.append([name, contact.split()])
        print("----> Contact added successfully.")

def add_num(lst, name, contact):
    for ele in lst:
        if ele[0] == name:
            if contact in ele[1]:
                print("Contact number "+contact+" already exist with name "+name)
            else:
                ele[1].append(contact)
                print("----> Contact number added successfully.")
            break
    else :
        print('\nContact with name "' + name + '" not exist !!!')
        print("\nDo you want to add this contact as new entry ?\nYes or No")
        res = input()
        if res == "Yes":
            add(lst, name, contact)
            
def try_name(name):
    try:
        if not name:
            raise ValueError('----> ValueError : Name is empty')
        if (not name[0:1].isalpha()) and name[0] != '_':
            raise ValueError('----> ValueError : first character should be Alphabet or Underscore.')
    except ValueError as e:
        print(e)
        return 1
    return 0
    
def try_contact(contact):
    try:
        if not contact:
            raise ValueError('----> ValueError : contact is empty')
        if not (contact[1:].isnumeric() and (contact[0].isnumeric() or contact[0] == '+')):
            raise ValueError('----> ValueError : characters of contact number should be numerical.')
    except ValueError as e:
        print(e)
        return 1
    return 0
    
def main():
    print('''\n
_____________________________________________________________

1) Add a new contact
2) Add a new number to existing contact
3) Search with keyword
4) Display all contacts
5) Exit
\nEnter Your Choice''')

    choice = int(input())

    if choice == 1:
        name = input('\nEnter the name of the new contact\n')
        if try_name(name): main()
        contact = input('\nEnter the contact number (without any space)\n')
        if try_contact(contact): main()
        add(contact_list, name, contact)
        main()

    elif choice == 2:
        name = input('\nEnter the name of the existing contact\n')
        if try_name(name): main()
        contact = input('\nEnter the contact number which you want to add (without any space)\n')
        if try_contact(contact): main()
        add_num(contact_list, name, contact)
        main()

    elif choice == 3:
        kw = input('\nEnter the keyword you want to search with\n')
        result = list(filter(lambda ele : ele[0].lower().find(kw.lower()) != -1, contact_list))
        
        if len(result) :
            print('\n\nHere is the list of cotacts withe keyword "'+kw+'"')
            for ele in result:
                print(ele[0],end=" - ")
                for i in range(0,len(ele[1])-1):
                    print(ele[1][i], end=", ")
                print(ele[1][len(ele[1])-1])
        
            name = input('\nEnter a name which you want to choose\n')
            for ele in result:
                if ele[0] == name:
                    print('\nHere is your selected contact :')
                    print(ele[0], end=" - ")
                    result_contacts = ele[1]
                    for i in range(0,len(ele[1])-1):
                        print(ele[1][i], end=", ")
                    print(ele[1][len(ele[1])-1])
                    break
            else:
                print('\nThe contact number with name "'+name+'" not exist')
        else:
            print('\nNo contacts found with keyword '+kw)
        main()    
        
    elif choice == 4:
        if contact_list:
            print('''\n\nHere is the list of all contacts :''')
            for ele in contact_list:
                print(ele[0],end=" - ")
                for i in range(0,len(ele[1])-1):
                    print(ele[1][i], end=", ")
                print(ele[1][len(ele[1])-1])
        else:
            print("There is no contacts saved yet")
        main()
    elif choice == 5:
        return
    else :
        print("\nInvalid Choice\nPlease enter valid choice.")
        main()

if __name__ == "__main__":
    main()