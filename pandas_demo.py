import pandas as pd 
student_list=["Bunny","Chinny","Pinny","Sunny","Tinny"]
student_marks=[30,40,60,48,89]

# s=pd.Series(index=student_list,data=student_marks,name="Student List")
# print(s)

s=pd.Series(data=dict(zip(student_list,student_marks)))
print(s)
