from linreg import linearregg

amount=[34,108,64,88,99,51]
tip=[5,17,11,8,14,5]

model=linearregg(amount,tip)


model.cc()

model.fit()
print(model.b1,model.b0)

input=[10,20,30]
predicted_value=model.predict(input)
print("pridicted value ",predicted_value)

mse=model.MSE()
print("mse value ",mse)

model.drawRegression()

