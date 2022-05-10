'''A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is the student allowed to sit in exam or not.'''

total_class = int(input("write total number of classes"))
attend_class = int(input("write total number of classes you attend"))
percentage = attend_class/total_class * 100
if percentage >= 75:
    print("percentage of class attend", percentage)
    print("This student is allowed to sit in the exam")
else:
    print("percentage of class attend", percentage)
    print("This student is not allowed to sit in the exam")