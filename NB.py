# import pandas as pd
class NB:
    def fit(self,x,y):
        # self.classes=list(set(y))
        # print(self.classes)
        # self.data={}
        # for i in self.classes:
        #     l=[]
        #     for j in range(len(y)):
        #         if i == y[j]:
        #             l.append(x[j])
        #         self.data[i]=l
        # print(self.data)

        self.X=x
        self.Y=y
        self.classes=list(set(y))
        print(self.classes)
        self.data={}
        for c in self.classes:
            l=[]
            for i,v in enumerate(Y):
                if c ==v:
                    l.append(x[i])
                self.data[c]=l
        print(self.data)
        


X=[
    ['Sunny','Hot','Weak'],
    ['Sunny','Hot','Strong'],
    ['Rainy','Cool','Weak'],
    ['Rainy','Cool','Strong'],
    ['Sunny','Cool','Weak'],
    ['Rainy','Hot','Weak']
]
Y=['No','No','Yes','Yes','Yes','Yes']
model=NB()
model.fit(X,Y)