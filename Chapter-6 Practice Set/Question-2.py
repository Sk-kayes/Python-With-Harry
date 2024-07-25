sub_1 = int(input("Enter marks: "))
sub_2 = int(input("Enter marks: "))
sub_3 = int(input("Enter marks: "))
total_marks = sub_1 + sub_2 + sub_3
avg_percent = float((100*total_marks)/300)
if(sub_1 >= 33 and sub_2 >= 33 and sub_3 >= 33 and avg_percent >= 40):
    print("Student passed.")
else:
    print("Student failed.")