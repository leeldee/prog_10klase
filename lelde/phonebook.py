contacts =  []
 
while(True):
    response = input("(1)add contact (2)print contact (3)exit: ")
    if response == "1" :
        person_name = input('name: ')
        person_surname = input('surname: ')
        person_phone = input('phone: ')
        person_email = input('email: ')
        person_contact = {
            "name": person_name,
            "surname": person_surname,
            "phone": person_phone,
            "email": person_email
            }
        contacts.append(person_contact)
    elif response == '2':
        print(contacts)
    elif response == '3':
        print('Bye bye!')
        exit()
    
   
  
      




person_contact = {
    "name": person_name,
    "surname": person_surname,
    "phone": person_phone,
    "email": person_email
}






person_name = input('name: ')
person_surname = input('surname: ')
person_phone = input('phone: ')
person_email = input('email: ')

person_contact = {
    "name": person_name,
    "surname": person_surname,
    "phone": person_phone,
    "email": person_email
}

contacts.append(person_contact)
print(contacts)