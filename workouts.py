

#1.	Accept a char input from the user and display it on the console.

name = input("Enter a name:")
print(name)

#2.	Accept two inputs from the user and output its sum.

num1 = int(input("Enter first number:"))
num2 = float(input("Enter Second number:"))
sum = num1+num2
print("Sum of two number is",sum)

# 3.	Write a program to find the simple interest.
# a.	Program should accept 3 inputs from the user and calculate simple interest for the given inputs. Formula: SI=(P*R*n)/100)

P = int(input("Enter principal amount:"))
R = float(input("Enter interest rate:"))
n = float(input("Enter number of years:"))

SI = (P*R*n)/100
print(SI)

# 4.	Write a program to check whether a student has passed or failed in a subject after he or she enters their mark (pass mark for a subject is 50 out of 100).
# a.	Program should accept an input from the user and output a message as “Passed” or “Failed”

mark = float(input("Enter a mark:"))
if mark>=50:
    print("Passed")

else:
    print("Failed")

# 5.	 Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
# a.	Program should accept an input from the user and display their grade as follows

mark = float(input("Enter your mark:"))
if mark>=90:
    print("A")
elif mark>=80 and mark<=89:
    print("B") 
elif mark>=70 and mark<=79:
    print("C")
elif mark>=60 and mark<=69:
    print("D")
elif mark>=50 and mark<=59:
    print("E")
else:
    print("Failed")

# 6.	Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows. 


print("1.Sunday,\n2.monday,\n3.Tuesday,\n.Wednesday,\n4.Thursay,\n5.Friday,\n6.Saturday,\n7.Sunday")

x = int(input("Enter a number:"))

if x == 1:
    print("Sunday")

elif x ==2:
    print("Monday")

elif x ==3:
    print("Tuesday")

elif x ==4:
    print("Wednesday")

elif x ==5:
    print("Thursday")

elif x == 6:
    print("friday")

elif x == 7:
    print("Saturday")

else:
    print("invalid input!!!")

# 7.	Write a program to print the multiplication table of given numbers. Using for and while
# a.	Accept an input from the user and display its multiplication table

# Using for loop

num = int(input("input a number:"))

for i in range (1,11):
    k = i*num
    print(f" {i} x {num} = {k}")

for i in range(1,11):
    print(f"{i} x {num} = {i*num}")


# Using While loop

num = int(input("Enter a number:"))
count = 1

print("The multiplication table is:")

while count<=num:
    print(f"{num} x {count} = {num*count}")
    count+=1

# 8.	Write a program to print the following pattern (hint: use nested loop)

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num  = int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()

# 9, Program should accept a string and display whether the string is a palindrome or not
# Eg: Output: Enter a string
# Input: MALAYALAM
# Output: Entered string is a palindrome

name = input("Enter a name:")
if name == name[::-1]:
    print(name,"It is a palindrome")
else:
    print(name,"is not a palindrome")


def palindrome(x):
    x = x.upper()

    x = ''.join(x.split())
    if x == x[::-1]:
        return True
    else:
        return False
    
word = input("enter a word:")
    
if palindrome(word):
    print("Entered string is a palindrome")

else:
    print("Enterd string is not a palindrome")

# 10.	Write a program to print the following pattern (hint: use nested loop)

# *
# * *
# * * *
# * * * *
# * * * * *

num = int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*", end = "")
    print()

# 11.	Write a program to print the following pattern (hint: use nested loop)

# * * * * *
# * * * *
# * * *
# * * 
# * 


num = int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(i,num+1):
        print("*",end = "")
    print()


