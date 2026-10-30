import numpy as np 

x1=np.array([1,2,3,4])
x2=np.array([4,5,8,2])
y=np.array([1,6,8,12])

x=np.hstack((np.ones((4,1)),x1.reshape((4,1)),x2.reshape((4,1))))
print(x)

a_cap=((np.linalg.inv(x.T @ x)) @ x.T ) @ y
print(a_cap)

intercept = a_cap[0]
slope1 = a_cap[1]
slope2 = a_cap[2]


final_expression = intercept + slope1*x1 + slope2*x2  
print(final_expression)