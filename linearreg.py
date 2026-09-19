import numpy as np
import pandas as pd
import math 

x=np.array([34,108,64,88,99,51])
y=np.array([5,17,11,8,14,5])

sumx=sum(x)
sumy=sum(y)
# print(sumx)
# print(sumy)

meanx=sumx/len(x)
meany=sumy/len(y)

# print(meanx)
# print(meany)

n=len(x )
billdevx=x-meanx
tipdevy=y-meany

# print(billdevx)
# print(billdevy)

deviationprod=billdevx*tipdevy
deviationprodsum=sum(deviationprod)
# print(deviationprodsum)
# print(deviationprod)

bill_dev_squar=billdevx**2
bill_dev_squar_sum=sum(bill_dev_squar)
# print(bill_dev_squar_sum)
# print(bill_dev_squar)



# cofficent od correlation

numerator=(n*(sum(x*y)))-((sumx)*(sumy))
denomenator=math.sqrt( ((n*(sum(x**2)))-sumx**2) *((n*(sum(y**2))-(sumy**2) )))

cofficent_of_correlation=numerator/denomenator

# print(cofficent_of_correlation)

# slope

b1=sum(billdevx*tipdevy)/sum(billdevx**2)
# print(b1)


#  intercept

b0=meany-b1*meanx
# print(b0)

# bivariate linear regression
# n=int(input("enter value of x : "))
# bivariate_linear_regression=b0+b1*n
# print(bivariate_linear_regression)



