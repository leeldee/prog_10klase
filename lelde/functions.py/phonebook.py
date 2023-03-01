contacts = []

while(True):
    response = input('N-add new, P-print, E-exit: ')
    if response == 'N':
        name = input('Enter name: ')
        surname = input('Enter surname: ')
        number = input('Enter number: ')
        email = input('Enter email: ')

        contact = {
            'name': name, 
            'surname': surname, 
            'number': number,
            'email': email
        }

        contacts.append(contact)
        print(contacts)
    elif response == 'P':
        for contact in contacts:
            print(f"{contact['name']} {contact['surname']} {contact['number']} {contact['email']}")
    elif response == 'E':
        break