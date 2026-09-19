import numpy as np
import matplotlib.pyplot as plt


class linearregg:
    def __init__(self, x, y):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        print("constructor run sucessfullyy")
        

    def cc(self):
        n = len(self.x)
        sumx = self.x.sum()
        sumy = self.y.sum()
        numerator = (n * (self.x * self.y).sum()) - (sumx * sumy)
        denominator = np.sqrt(
            ((n * (self.x ** 2).sum()) - sumx ** 2)
            * ((n * (self.y ** 2).sum()) - sumy ** 2)
        )
        c_of_c = numerator / denominator
        return c_of_c

    def fit(self):
        meanx = self.x.mean()
        meany = self.y.mean()
        devx = self.x - meanx
        devy = self.y - meany
        self.b1 = (devx * devy).sum() / (devx ** 2).sum()
        self.b0 = meany - self.b1 * meanx
        return self

    def predict(self, value):
        value = np.array(value, dtype=float)
        self.predicted_value=self.b0 + self.b1 * value
        return  self.predicted_value

    def MSE(self):
        diff =self.y - self.predict(self.x)
        sq=diff**2
        mse = sq.mean()
        
        return mse

    def drawRegression(self):
        plt.scatter(self.x,self.y)
        plt.plot(self.x,self.predicted_value)
        plt.show()