# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name

# print(pet_names[0])


# #3. ✅ Return all pet names beginning from the 3rd index

# print(pet_names[3:]) #inclusive

# #4. ✅ Return all pet names before the 3rd index

# print(pet_names[:3])  #exclusive


# #5. ✅ Return all pet names beginning from the 3rd index and up to the 7th

# print(pet_names[3:8])  #Luke at index 3 , Tom at index of 7  3:7 exclusive


#6. ✅ Find the index of a given element => .index()

# print(pet_names.index('Rose'))
# print(pet_names.index('Paul'))

# #7. ✅ Reverse the original list => .reverse()

# print(pet_names.reverse())  # does not return anything
# print(pet_names)  #destructive, flips over all elements. this demonstrates the immutability of lists

#8. ✅ Return the frequency of a given element => .count()

# print(pet_names.count("Rose"))
# # print(pet_names.count("Tom"))


# # Updating Lists
# #9. ✅ Change the first name to all uppercase letters => .upper()

# pet_names[0] = pet_names[0].upper()
# print(pet_names[0])


# #10. ✅ Append a new name to the list => .append()
# pet_names.append("Bud")
# print(pet_names)


#11. ✅ Add a new name at a specific index => .insert()

#argument 1 => index
#argument 2 => value
# pet_names.insert(0, "Bud")
# pet_names.insert(-1, "Sally") # second item from the end, not the last one inserted, append is better to add an item to the end
# print(pet_names)


#12. ✅ Add two lists together => +

# new_list = pet_names + ["bud", "Sally"]
# print(new_list)


#13. ✅ Remove the final element from the list => .pop()

# pet_names.pop() # mutative (destructuve)
# pet_names.pop(-1)
# print(pet_names)

#14. ✅ Remove element by specific index => .pop()


#15. ✅ Remove a specific element => .remove()
# pet_names.remove("Princess Grace")
# print(pet_names)


#16. ✅ Remove all pet names from the list => .clear()
# print(pet_names)
# pet_names.clear()
# print(pet_names)


#Tuple
# why are tuples immutable?
#what advantages this provide for us ? in what situations
#would this serve us?

#tuples help us to preserve our data, keep it from being changed or altered in any way.

# 📚 Review:
    # Mutable, Immutable <=> Changeable, Unchangeable

#17. ✅ Create a Tuple of 10 pet ages => () 

pet_ages = (1,2,3,4,5,6,7,8,9,10)


#18. ✅ Print the first pet age => []
# print(pet_ages[0])
# print(pet_ages[-1])

# Testing Mutability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
# pet_ages.pop(0)  # no attribute pop
# print(pet_ages)


#20. ✅ Attempt to change the first element (should error) => []
# pet_ages[0] = 5 # tuple object does not support item assignment TypeError
# print(pet_ages[0])


# Tuple Methods
#21. ✅ Return the frequency of a given element => .count()

# print(pet_ages.count(1))

#22. ✅ Return the index of a given element  => .index()

# print(pet_ages.index(3))


#23. ✅ Create a Range 
# Note:  Ranges are primarily used in loops


# Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}

# Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name='Spot', age=25, breed='boxer')

# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
# print(pet_info_rose['temperament'])

#28. ✅ Print the pet attribute of "age" using ".get"

    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error

# print(pet_info_rose.get('temperament', "Attribute not found")) # returns None , no error out=> if we ["temperament"] and look for key, we will get key error.


# Updating 
#29. ✅ Update Rose's age to 12 => []

# pet_info_rose['age'] = 12  #reassign 
# print(pet_info_rose)


#30. ✅ Update Spot's age to 26 => .update({...})

# pet_info_spot.update({'age' : 26})
# print(pet_info_spot)

# # Deleting
# #31. ✅ Delete Rose's age using the "del" keyword => []

# del pet_info_rose['age']
# print(pet_info_rose)


#32. ✅ Delete Spot's age using ".pop"

#.pop('age)

#33. ✅ Delete the last item for Rose using "popitem()"

# final attribute item ;similar to pop()

# Loops 
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

#34. ✅ Loop through a range of 10 and print every number within the range
# for num in range(10):
#     print(num)


#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number

# for num in range(50, 60, 2):
#     print(num)

#36. ✅ Loop through the "pet_info" list and print every dictionary

# for pet in pet_info:
#     print(pet)


#37. ✅ Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_names" as an argument

# def loop_through_list(list):
#     for pet in pet_info:
#         print(pet)

# loop_through_list(pet_info)


#38. ✅ Create a function that takes a list as a parameter
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter

# def demonstrate_while(list):
#     counter = 0

#     while(counter < len(list) -1): # length is 10 , counter should be less than 9
#         counter += 1
#     return counter

# print(demonstrate_while(pet_names))



#39. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dictionaries", "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'

# def update_pet_age(list, name, age): # list of dictionaries
#     index = 0
#     while(list[index]["name"] != name and index < len(list) - 1):
#         index += 1
        
#         if (list[index]["name"] == name):
#             list[index]["age"] = age

#             return list[index]

#         else:
#             return 'Pet not found!'

# print(update_pet_age(pet_info, 'Bud', 26))

    

# map like 
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase

# pets = [pet.get('name').upper() for pet in pet_info]

# print(pets)

# find like
#41. ✅ Use list comprehension to find a pet named spot

# pet_spot = [pet for pet in pet_info if pet.get('name') == "Spot"]
# print(pet_spot)


# filter like
#42. ✅ Use list comprehension to find all of the pets under 3 years old

# pets_under_three = [pet for pet in pet_info if pet.get('age') < 3]
# print(pets_under_three)

#43. ✅ Create a generator expression matching the filter above

# young_pets = (pet for pet in pet_info if pet.get('age') < 3)
# list_convert = list(young_pets)
# print(list_convert)

