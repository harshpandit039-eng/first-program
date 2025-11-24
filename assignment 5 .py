"""
task:1
create a dictionary of a student marks
"""

stu_marks={"alice:99","bob:78","casey:87","dan:89"}
user_input=input("enter students name : ")
if user_input in stu_marks:
    print("students found")
else:
    print("student not found")


"""
task:2
demonstrate list slicing
"""

my_list=[1,2,3,4,5,6,7,8,9,10]
print(my_list)
first_five_of_list=my_list[:5]
print(first_five_of_list)
reverse_of_first_five_of_list=first_five_of_list[::-1]
print(reverse_of_first_five_of_list)