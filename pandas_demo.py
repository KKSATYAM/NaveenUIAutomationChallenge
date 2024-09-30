# import pandas as pd 
# # student_list=["Bunny","Chinny","Pinny","Sunny","Tinny"]
# # student_marks=[30,40,60,48,89]


# # s=pd.Series(index=student_list,data=student_marks,name="Student List")
# # print(s)

# # s=pd.Series(data=dict(zip(student_list,student_marks)))
# # print(s)
# # series=pd.Series([i for i in range(0,50)])
# # # print(series.tail(-40))

# # print(series.head(15).tail(-10))
# # print("*******************************************************")
# # print(series.head(15).tail(5))

# # print("*******************************************************")
# # print(series.tail(-10).head())


# from string import ascii_uppercase as au
# # alphabet=list(au)
# # print(au)


# # print(["LABEL-"+word for word in au])

# series=pd.Series(data=list(au),index=["LABEL_"+word for word in au])
# print(series["LABEL_A":"LABEL_K"])

import pandas as pd
import numpy as np

# series=pd.Series([i for i in range(20)])


# def odd_selection(s):
#     return [True if i%2==1 else False for i in s]
# print(series[odd_selection])


series=pd.Series([10,20,pd.NA,np.nan,None])
# print(series.isnull().sum())
# print(series.size-series.count())
# print(series[series.isnull()].count())
# print(series[series.notnull()].count)
print(series[1])













