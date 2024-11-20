# licence program
# Take user input name , age & typ
print("Welcome to the Driving Licence Application program")
typ = str(input("What is your licence type new/renewal:"))

"""Criteria
if the age is equal to greater than 18 print(you are eligible for the license)
if the age is less then 18 print(you are not eligible for the license)
if the license type is renewal then ask what your license number.
"""
alp = 0
num = 0
if typ == "new":
    name = str(input("Enter your name: "))
    age = int(input("enter your age: "))
    if age >=18:
        print("Applicant name:",name)
        print("Applicant age:",age)
        print("your are eligible for the licence")
    else:
        print("Yor are not eligible for the licence beacuse your age is under 18")
elif typ == "renewal":
    name = str(input("Enter your name: "))
    renew = str(input("Enter your Licence no:"))

    for i in renew:
        if i.isalpha(): # Check if character is an alphabet
            alp +=1

        elif i.isnumeric(): # Check if character is a digit
            num +=1

        elif i.isspace():
            continue        #if User entered space the code is skip space

    if alp + num == 15: #Check if character is equal to 10 digits
         print(f"Your Card name: {name}")
         print(f"Okay!, We will work on it and we'll dispatch your licence at your address.")
    else:
        print("you type wrong licence no, pls enter your 15 digit licence no")
