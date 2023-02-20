#Lab 1 Section:

#1.1 python.org

#1.2 Hello World Typos

#1.3 Infinite Skills: 1. Tech Repair Website/App 2. Meal Prep/Planner App. 3. Budgeter App. 

#Lab 2 Section:

#2.1 Simple Message: 
#2.2 Simple Messages:
#message = "Hello, Python Crash Course reader (O'Reilley)"
#new_message = "Hello, Python Crash Course reader (O'Reilley)"
#print(message)
#print(new_message)

#2.3 Personal Messages:
#p1_first_name = "Eric"
#p1_last_name = "Jones"
#print(p1_first_name)
#print(p1_last_name)

#2.4 Name Cases: 
#p1_full_name = p1_first_name + p1_last_name
#print(p1_full_name)
#print(p1_full_name.upper())
#print(p1_full_name.lower())
#print(p1_full_name.title())

#2.5 Famous Quote: 
#fav_author = "Albert Einstein once said, "
#fav_quote = '“A person who never made a mistake never tried anything new.”'
#print(fav_author + fav_quote)

#2.6 Famous Quote v2:
#famous_person = "Walt Disney once said, "
#famous_quote = '"The way to get started is to quit talking and begin doing."'
#message = (famous_person + famous_quote)
#print(message)

#2.7 Stripping Names:
#my_name = ' Charlie '
#print(my_name.rstrip())
#print(my_name.lstrip())
#print(my_name.strip())

#2.8 Number Eight
#print(5+3)
#print(11-3)
#print(8*1)
#print(8/1)

#2.9 Favourite Number
#fav_num = 21
#message = (fav_num)
#print(message)

#2.10 Adding Comments
#Say hello to everyone.
#print("Hello, Python People!")

#2.11 The Zen of Python
#import this

#Lab 3 Section:

#3.1 Names/Lists:
#names = ['Ben', 'Andrico', 'Rhys']
#print(names[0])
#print(names[1])
#print(names[2])

#3.2 Greetings:
#names = ['Ben', 'Andrico', 'Rhys']
#greeting = "Hello, "
#print(greeting + names[0])
#print(greeting + names[1])
#print(greeting + names[2])
#OR
#msg1 = "Ben"
#msg2 = "Andrico"
#msg3 = "Rhys"
#print(greeting, msg1)
#print(greeting, msg2)
#print(greeting, msg3)

#3.3 Your Own List:
#bike_list = ['Honda', 'Ducati', 'Surron']
#fav_veh = "I would like to own a " 
#print(fav_veh + (bike_list[0]))
#print(fav_veh + (bike_list[1]))
#print(fav_veh + (bike_list[2]))

#Modifying an Element in a List:
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)
#motorcycles[0] = 'ducati'
#print(motorcycles)

#Appending Elements to the End of a List:
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)
#motorcycles.append('ducati')
#print(motorcycles)

#motorcycles = []
#motorcycles.append('honda')
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')
#print(motorcycles)

#Inserting Elements into a List:
#motorcycles = ['honda', 'yamaha', 'suzuki']
#motorcycles.insert(0,'ducati')
#print(motorcycles)

#Removing an Item from the List using the del Statement:
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)
#del motorcycles[0]
#print(motorcycles)

#Removing an Item Using the pop() Method
#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)
#popped_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycle)

#Popping Items from any Position in a List
#motorcycles = ['honda', 'yamaha', 'suzuki']
#first_owned = motorcycles.pop(0)
#print(f"The first motorcycle I owned was a {first_owned.title()}.")
#NOTE: when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

#Removing an Item by Value
#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)
#too_expensive = 'ducati'
#motorcycles.remove(too_expensive)
#print(motorcycles)
#print(f"\nA {too_expensive.title()} is too expensive for me.")#

#3.4 Guest List:
guest_list = ['Andrico ', 'Ben, ', 'Rhys, '] 
#message1 = "Dear " + (guest_list[0]) + "I would like to respectfully invite you to my party tonight!"
#message2 = "Dear " + (guest_list[1]) + "I would like to respectfully invite you to my party tonight!"
#message3 = "Dear " + (guest_list[2]) + "I would like to respectfully invite you to my party tonight!"
#print(message1)
#print(message2)
#print(message3)

#3.5 Changing Guest List
#print('Unfortuntely, ' + (guest_list[0]) + ' cannot make it.')
#guest_list[0] = 'Alfie, '
#message1 = "Dear " + (guest_list[0]) + "I would like to respectfully invite you to my party tonight!"
#message2 = "Dear " + (guest_list[1]) + "I would like to respectfully invite you to my party tonight!"
#message3 = "Dear " + (guest_list[2]) + "I would like to respectfully invite you to my party tonight!"
#print(message1)
#print(message2)
#print(message3)

#3.6 More Guests:
#print("Bigger dinner table!")
#guest_list.insert(0, 'Stevie, ')
#guest_list.insert(2, 'Wonder, ')
#guest_list.insert(4, 'Chakakhan, ')
#message1 = "Dear " + (guest_list[0]) + "I would like to respectfully invite you to my party tonight!"
#message2 = "Dear " + (guest_list[1]) + "I would like to respectfully invite you to my party tonight!"
#message3 = "Dear " + (guest_list[2]) + "I would like to respectfully invite you to my party tonight!"
#message4 = "Dear " + (guest_list[3]) + "I would like to respectfully invite you to my party tonight!"
#message5 = "Dear " + (guest_list[4]) + "I would like to respectfully invite you to my party tonight!"
#print(message1)
#print(message2)
#print(message3)
#print(message4)
#print(message5)

#3.7 Shrinking Guest List:
#not_coming1 = guest_list.pop(0)
#print(f"The first guest that cannot come is {not_coming1.title()}.")
#not_coming2 = guest_list.pop(1)
#print(f"The second guest that cannot come is {not_coming2.title()}.")
#not_coming3 = guest_list.pop(2)
#print(f"The third guest that cannot come is {not_coming3.title()}.")
#print(guest_list)
#print(message1)
#print(message2)
#del guest_list[0]
#del guest_list[0]
#del guest_list[0]
#print(guest_list)

#3.8 Seeing the World:
#holidays = ['Spain', 'France', 'Canada', 'USA', 'Japan']
#print(holidays)
#print(sorted(holidays))
#holidays.reverse()
#print(holidays)
#holidays.reverse()
#print(holidays)
#holidays.sort(reverse=False)
#print(holidays)

#3.9 Dinner Guests:
#coming = len(guest_list)

#4.1 Pizzas:
fav_pizza = ['Pepperoni', 'Meat Feast', 'BBQ Chicken']
for fav_pizza in fav_pizza:
    print(fav_pizza)