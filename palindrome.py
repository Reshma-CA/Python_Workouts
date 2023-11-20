# def palindrome(string):
#     if len(string) <= 1:
#         return True
#     if string[0] == string[-1]:
#         return palindrome(string[1:-1])
    
#     else:
#         return False

# result = palindrome('malayalam')
# print(result)

class Average:
    def __init__(self,written_test,lab_exams,Assignments):
        self.written_test = written_test
        self.lab_exams = lab_exams
        self.Assignments = Assignments

    def Avg(self):
        result = (self.written_test*70)/100+(self.lab_exams*20)/100+(self.Assignments*10)/100
        return result
    
written_test = int(input("Enter your written test mark :"))
lab_test = int(input("enter your lab exam mark:"))
Assignment = int(input("Enter your Assignment Mark:"))  
    
student = Average(written_test,lab_test,Assignment)

k = student.Avg()
print("Grade of the student",k)
