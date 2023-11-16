# str1 = input("Enter a name")
# str2 = ""

# for i in str1:
#     str2 += i

# print(str1)
# print(str2)
# if str1 == str2 :
#     print(str1,"is a palindrome:")

# else:
#     print(str1,"is not apalindrome")


'''str1 = input("Enter a name")
str2 = ""

for i in str1[::-1]:
    str2 += i

print(str1)
print(str2)
if str1 == str2 :
    print(str1,"is a palindrome:")

else:
    print(str1,"is not apalindrome")'''

#1.	Accept a char input from the user and display it on the console.

'''name = input("Enter a name:")
print(name)'''

#2.	Accept two inputs from the user and output its sum.

'''num1 = int(input("Enter first number:"))
num2 = float(input("Enter Second number:"))
sum = num1+num2
print("Sum of two number is",sum)'''

# 3.	Write a program to find the simple interest.
# a.	Program should accept 3 inputs from the user and calculate simple interest for the given inputs. Formula: SI=(P*R*n)/100)

'''P = int(input("Enter principal amount:"))
R = float(input("Enter interest rate:"))
n = float(input("Enter number of years:"))

SI = (P*R*n)/100
print(SI)'''

# 4.	Write a program to check whether a student has passed or failed in a subject after he or she enters their mark (pass mark for a subject is 50 out of 100).
# a.	Program should accept an input from the user and output a message as “Passed” or “Failed”

'''mark = float(input("Enter a mark:"))
if mark>=50:
    print("Passed")

else:
    print("Failed")'''

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



