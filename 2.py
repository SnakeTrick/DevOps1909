your_name = input("Enter your name: ")
print("are you aviel?" + str(your_name == "aviel"))
your_age = int(input("Enter your age: "))
print("are you old? " + str(your_age >= 18))
your_height = int(input("Enter your height(cm): "))
print("are you tall? " + str(your_height >= 180))
if your_name == "aviel":
    print("Welcome to my name")
else:
    print("Welcome to not my name")

