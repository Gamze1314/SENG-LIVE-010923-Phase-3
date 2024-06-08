#!/usr/bin/env python3

# 📚 Review:
    # Python environment set up
	# Python debugging tools 
	# Python datatypes 

# 🚨 To enable ipdb debugging, first import "ipdb"
import ipdb

pet_mood = "xyz"
pet_name = "Rose"

# 1. ✅ Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."

# ipdb.set_trace()  # stop the execution at any point. we can override values in the ipdb session, then c command to execute the file.(exit out)

if pet_mood == "Hungry!":  # control the flow of our code 
    print("Rose needs to be fed")
elif pet_mood == "Rowdy!":
    print("Rose needs a walk")
else:
    print("Rose is all good")

    # Note => Feel free to set your own values for "pet_mood" to view various outputs.

# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
    # If pet_food is "Hungry!" => "Rose needs to be fed."
    # In all other cases => "Rose is all good."

# print("Rose needs to be fed.") if pet_mood == "Hungry" else print("Rose is all good.")


# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
    # Test invocation of "say_hello" in ipdb using "say_hello()"
    # say_hello() => "Hello, world!"

def say_hello(param = "Default"): # we can invoke function with default parameter, without args.
    print("Hello, world!")

# say_hello()

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"

name = "Bud"  # global scope variable


def pet_greeting():
    print(f"{name} says hello!")

# pet_greeting("Rose") #invokation with or without arguments.
# pet_greeting()

# ipdb.set_trace()

# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
    # Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
    # pet_status("Rose", "Hungry!") => "Rose needs to be fed."
    # pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
    # pet_greeting("Bud", "Relaxed") => "Bud is all good."
    
    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred" 

def pet_birthday(age):

    ipdb.set_trace()

    try:
        age = age + 1
        print(f"Happy Birthday! Your pet is now {age}")
    except TypeError:
        print("Type Error Occurred!")
    # except NameError:
    #     print("Name Error Occurred!")
    # except ValueError:
    #     print("Value Error Occurred!")


pet_birthday(10)
# pet_birthday("ee")
# pet_birthday("10")

    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:



