
import pandas as pd
import numpy as np
import mllib
class LinearRegressionMV:
    def loadfile(self,filename):
        self.data=pd.read_csv(filename)

    def datacleaning(self,categorial,numerical,target):
        self.categorial=categorial
        self.numerical=numerical
        self.target=target
        self.data=mllib.encoder(self.data,categorial)
        self.data=self.data.dropna()
        self.actual_data=self.data.copy()

    def fit(self):
        x=self.data[self.categorial+self.numerical]
        y=self.data[self.target]
        x_train,x_test,y_train,y_test=mllib.test_train_splits(x,y)   
        x_train=x_train.to_numpy()
        x_train=np.column_stack((np.ones(x_train.shape[0]),x_train))
        y_train=y_train.to_numpy()

        result=((np.linalg.pinv(x_train.T @ x_train)) @ x_train.T ) @ y_train

        self.intercept=result[0]    
        self.slope=result[1:]
        for i,v in enumerate(self.categorial+self.numerical):
            print(v,self.slope[i])

 
    def predict(self,mydata):
        values=mydata.values()
        s=self.intercept
        for i,v in enumerate(values):
            s=self.slope[i]*v
        print(s)



model=LinearRegressionMV()
model.loadfile("D:/pythonnnnn/machinelearning/housingdata.csv")

column=['locality','city','property_type','furnished']
numerical_columns = ["area","bedroom_num","bathroom_num","balcony_num","age","total_floors"]
target_column = ["price"]

model.datacleaning(column,numerical_columns,target_column)
# print(model.data['furnished'])

model.fit()

mydata={"locality":1,
"city":1,
"property_type": 1,
"furnished" :0,
"area" :200,
"bedroom_num":3,
"bathroom_num" :3,
"balcony_num" :2,
"age":2,
"total_floors" :1}
model.predict(mydata)