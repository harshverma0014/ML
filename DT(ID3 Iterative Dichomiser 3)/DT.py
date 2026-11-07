import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import OrdinalEncoder , LabelEncoder
from sklearn.tree import DecisionTreeClassifier , plot_tree

data = {
    "Outlook": [
        "Sunny", "Sunny", "Overcast", "Rain",
        "Rain", "Rain", "Overcast", "Sunny",
        "Sunny", "Rain", "Sunny", "Overcast",
        "Overcast", "Rain"
    ],
    "Temperature": [
        "Hot", "Hot", "Hot", "Mild",
        "Cool", "Cool", "Cool", "Mild",
        "Cool", "Mild", "Mild", "Mild",
        "Hot", "Mild"
    ],
    "Humidity": [
        "High", "High", "High", "High",
        "Normal", "Normal", "Normal", "High",
        "Normal", "Normal", "Normal", "High",
        "Normal", "High"
    ],
    "Wind": [
        "Weak", "Strong", "Weak", "Weak",
        "Weak", "Strong", "Strong", "Weak",
        "Weak", "Weak", "Strong", "Strong",
        "Weak", "Strong"
    ],
    "Play": [
        "No", "No", "Yes", "Yes",
        "Yes", "No", "Yes", "No",
        "Yes", "Yes", "Yes", "Yes",
        "Yes", "No"
    ]
}

df = pd.DataFrame(data)
x=df.drop('Play',axis=1)
y=df['Play']
print(df)
# print(x)
# print(y)


encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(x)

# print(X_encoded)

Label_Encoder = LabelEncoder()
y_Encoded =  Label_Encoder.fit_transform(y)

# print(y_Encoded)

model = DecisionTreeClassifier(
    criterion='entropy',
    random_state=0
)

model.fit(X_encoded , y_Encoded)


new_weather = pd.DataFrame([{
    "Outlook":"Sunny",
    "Temperature":"Cool",
    "Humidity": "Normal",
    "Wind": "Weak"
}])

new_encoded = encoder.fit_transform(new_weather)
prediction = model.predict(new_encoded)

result = Label_Encoder.inverse_transform(prediction)
# prob = 
print(result[0])

# plt.figure(figsize=(16,8))
plot_tree(
    model,
    feature_names = x.columns,
    class_names=Label_Encoder.classes_,
    filled=True,
    rounded=True
)

plt.title("TENNIS GAME DECISION TREE")
plt.show()