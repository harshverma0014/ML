import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def test_train_splits(data_x, data_y):
    l = len(data_x)

    train_size = int(l * 0.8)

    return [
        data_x.iloc[:train_size],
        data_x.iloc[train_size:],
        data_y.iloc[:train_size],
        data_y.iloc[train_size:]
    ]

column=['locality','city','property_type','furnished']

data = pd.read_csv("D:/pythonnnnn/machinelearning/housingdata.csv")

data_y = data['price']

data_x = data.drop(['price'], axis=1)

x_train, x_test, y_train, y_test = test_train_splits(data_x, data_y)


data_x.drop(['title'],inplace=True,axis=1)

ori = pd.get_dummies(
    data=data_x,
    columns=column,
    drop_first=True,
    dtype=int
)


print(ori)

# ori.to_csv("ori.csv", index=False)
# print(x_train)
# print(y_train)
# print(x_test)
# print(y_test)


# print(data.columns)
# Index(['title', 'price', 'area', 'price_per_sqft', 'locality', 'city',
#        'property_type', 'bedroom_num', 'bathroom_num', 'balcony_num',
#        'furnished', 'age', 'total_floors', 'latitude', 'longitude'],
#       dtype='str')

