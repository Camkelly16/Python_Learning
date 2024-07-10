
#if name is less than 3 characters long name must be at least 3 characters otherwise
#if it's more than 50 characters long name can be a maximum of 50 characters
#otherwise name looks good

#Ask the user to enter there name
#Allow the user to enter there name
#Court the character in the name
#Follow the condtion statements

print("What is your name?")
name = input()

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name)> 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")
