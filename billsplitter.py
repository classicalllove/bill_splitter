import random

number_of_people = input('Enter the number of friends joining (including you): ')
number_of_people = int(number_of_people)
print()
if number_of_people < 1:
    print("No one is joining for the party")
else:
    list_of_names = []
    print('Enter the name of every friend (including you), each on a new line: ')
    list_of_names_dict = {}
    for i in range(0, number_of_people):
        name = input()
        list_of_names.append(name)
    list_of_names_dict = dict.fromkeys(list_of_names, 0)
    print()
    bill = int(input('Enter the total bill value: '))
    print()
    share = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    print()
    if share == 'Yes':
        for price in list_of_names_dict:
            list_of_names_dict[price] = round(bill / (number_of_people - 1), 2)
        Name = random.choice(list_of_names)
        list_of_names_dict[Name] = 0
        print(f'{Name} is the lucky one!')

    else:
        print('No one is going to be lucky')
        for price in list_of_names_dict:
            list_of_names_dict[price] = round(bill / number_of_people, 2)
    print()
    print(list_of_names_dict)
