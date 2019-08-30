age = int(input("Enter your age: "))
# can_you_learn_programming = 0 < age < 100
# print(f"You can learn programming: {can_you_learn_programming}")
usually_not_working = age < 18 or age > 70
print(f"At {age}, you are more than likely not working: {usually_not_working}")