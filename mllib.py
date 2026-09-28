def test_train_splits(data_x, data_y):
    l = len(data_x)

    train_size = int(l * 0.8)

    return [
        data_x.iloc[:train_size],
        data_x.iloc[train_size:],
        data_y.iloc[:train_size],
        data_y.iloc[train_size:]
    ]

def encoder (data,col_list):
    for col in col_list:
        t=data[col].unique()
        # t.sort()
        mapping={}
        for i,v in enumerate(t):
            mapping[v]=i
        data[col]=data[col].map(mapping)

    return data

