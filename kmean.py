import numpy as np

class kmean:
    def __init__(self, k):
        self.k = k
        self.centroid = None
        self.clusters = None

    def fit(self, data):
        self.centroid = [4, 11]

        
        for i in range(100):
            
            clusters = [[] for i in range(self.k)]

            for v in data:
                distance = []

                for c in self.centroid:
                    dis = abs(v - c)
                    distance.append(dis)

                cluster_index = distance.index(min(distance))

                clusters[cluster_index].append(v)

            print(clusters)

            nc=[]
            for cluster in clusters:
                if (len(cluster)>0):
                    nc.append(sum(cluster)/len(cluster))
                else:
                    nc.append(0) 

            print(nc)
            if(nc==self.clusters):
                break
            self.clusters=nc
        self.clusters=clusters

    def show(self):
        print('cluster:')
        print(self.clusters)
        print('centroid: ')
        print(self.centroid)

    def predict(self,value):
        distance=[]
        for centroid in self.centroid:
            dis=abs(value-centroid)
            distance.append(dis)

        return distance.index(min(distance))


model = kmean(2)

data = [2, 4, 10, 12, 3, 20, 30, 11, 25]

model.fit(data)
value=30
p=model.predict(value)
model.show()
print(value , 'belongs to clusters ',model.clusters[p])