import pandas as pd

def encoder (data,col_list):
    for col in col_list:
        t=df[col].unique()
        t.sort()
        mapping={}
        for i,v in enumerate(t):
            mapping[v]=i
        df[col]=df[col].map(mapping)

df = pd.read_csv("D:/pythonnnnn/machinelearning/housingdata.csv")
print(t)

# print(mapping)

print(df['furnished'])