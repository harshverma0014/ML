import numpy as np
import matplotlib.pyplot as plt
class SVM:
    def __init__(self):
        self.w = np.zeros(2)
        self.b = 0

    def fit(self,X,y,lr=0.01,epoch=1):
       for i in range (epoch):
        for i in range (len(X)):
            score = np.dot(self.w , X[i]) + self.b
            
            if y[i] * score < 1 :
                self.w = self.w + lr * y[i] * X[i]
                self.b = self.b + lr * y[i]

    def predict(self, X):
        score = np.dot(self.w,X) + self.b

        if score >0:
            return 'Dog'
        elif score < 0:
            return "Cat"
        else :
            return "hyperplane"

    def plot(self,X,y):
        plt.scatter(
            X[y == -1 , 0], X[y == -1 , 1],
            color='blue',label='Cat'
        )

        plt.scatter(
            X[y == 1 , 0], X[y == 1 , 1],
            color='red',marker='s',label='Dog'
        )

        plt.title('SVM: Cat vs Dog')
        plt.xlim(0,30)
        plt.ylim(0,75)
        plt.legend()
        plt.grid(True)
        plt.show()



X=np.array([
    [2,20],         #cat
    [3,25],         #cat
    [4,30],         #cat
    [15,50],        #dog
    [20,60],        #dog
    [25,70]         #dog
])

y=np.array([-1,-1,-1,1,1,1])

model=SVM()

model.fit(X,y,100)

new_animal = np.array([5,25])

print(model.predict(new_animal))
print(model.w)
print(model.b)


model.plot(X,y)