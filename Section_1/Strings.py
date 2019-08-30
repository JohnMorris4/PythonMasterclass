string_with_quotes = "This is a double quote"
string_with_single_quotes = 'This is with single quotes'
age = 57
print("you are ", age)

"""
This is a f string for a simplified string
"""
print(f"You are {age}")

name = "John"
greeting = f"Hello, {name}"
print (greeting)

# This is a compound formatted string
emp_name = "Jennifer"
final_greeting = "How are you today {}?"
jennifer_greeting = final_greeting.format(emp_name)
print(jennifer_greeting)
