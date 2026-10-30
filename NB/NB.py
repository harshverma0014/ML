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
        #     l=[]
        #     for i,v in enumerate(Y):
        #         if c ==v:
        #             l.append(x[i])
        #         self.data[c]=l
        # print(self.data)
        
            self.data[c]=[ X[i] for i in range(len(Y)) if (c==Y[i])]
        print(self.data)

            
        self.prob={}
        for c in self.classes:
            self.prob[c]=(len(self.data[c])/len(Y))
        print(self.prob)

    def predict(self,x):
        result={}
        for c in self.classes:
            rows=self.data[c]
            p=self.prob[c]
            for j in range(len(x)):
                count=sum( x[j]==row[j] for row in rows)
                values=len(set(row[j] for row in self.X))
                p*=( count+1 ) / ( len(rows) + values )
            result[c]=p
        print(result)
        evidence=sum(result.values())
        print(evidence)
        for r in result:
            result[r]=result[r]/evidence
        print(result)
        print(max(result,key=result.get))


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
model.predict(['Sunny','Cool','Weak'])
