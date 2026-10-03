import numpy as np
import matplotlib.pyplot as plt
class Kmean:
    def __init__(self,k):

        self.k=k
        self.centroid=None
        self.clusters=None

    def fit(self,data):
        
        data=np.array(data,float)
        self.centroid=data[:self.k] 
        
        for i in range(100):  
          clusters=[[] for i in range(self.k)]
          for v in data:
            distance=[]
            for c in self.centroid:
                dis=np.sqrt(np.sum(v-c)**2)
                distance.append(dis)
            cluster_index=distance.index(min(distance))    
            clusters[cluster_index].append(v)
          #print(clusters)
          nc=[]    
          for cluster in clusters:
             if(len(cluster)>0):
                 nc.append(sum(cluster)/len(cluster))
             else:
                 nc.append(0) 
          #print(nc)        
          if(nc==self.clusters):
            break
          self.centroid=nc
        self.clusters=clusters
    def show(self): 
        print('Clusters:')
        print(self.clusters)
        print('Centroid:')
        print(self.centroid)
    def predict(self,value):
       distance=[]    
       value=np.array(value,float)
       for centroid in self.centroid:
           dis=np.sqrt(np.sum(value-centroid)**2)
           distance.append(dis)
       return  distance.index(min(distance))   
    def showPlot(self):
        color=['r','b']
        for i in range(self.k):
           plt.scatter(self.clusters[i],[i+1]*len(self.clusters[i]),c=color[i])
       
        plt.scatter(self.centroid,range(1,self.k+1),c="g",s=100,marker='*')
        plt.yticks(range(1,self.k+1))
        plt.show()


model=Kmean(2)
data=[[2,4],[10,12],[3,20],[30,11],[25,10],[2,4],[5,9],[13,21],[25,31],[15,18]]        
model.fit(data)
model.show()
value=[30,10]

p=model.predict(value)
print(value,"Belongs to cluster",model.clusters[p])
# model.showPlot()