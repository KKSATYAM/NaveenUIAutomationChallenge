import numpy as np
import matplotlib.pyplot as plt


a=np.arange(1,11)
b=a**2

plt.plot(a,b,marker='o')
plt.show()


# print(np.__version__)

# a= np.array([
#             [[1,2,3,4],
#             [5,6,7,8],
            
#             [9,10,11,12]],
         
#             [[13,14,15,16],
#             [17,18,19,20],
#             [21,22,23,24]]]
         
#          )
# print(a[0,1,3])

# for x in np.nditer(a[:,1:3,1:3],op_dtypes=str,flags=['buffered']):
#     print(x)

# for pos, element in np.ndenumerate(a):
#     print(f'{element}<===>{pos}')


