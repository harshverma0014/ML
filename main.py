from linreg import linearregg

amount=[34,108,64,88,99,51]
tip=[5,17,11,8,14,5]

model=linearregg(amount,tip)


model.cc()

model.fit()

predicted_value=model.predict([34,108,64,88,99,51])
print("pridicted value ",predicted_value)

mse_value=model.MSE(predicted_value)
print("mse value ",mse_value)

model.drawRegression()














# model.cc()

# model.fit()
# print(model.b0,model.b1)
# # test=[70,2000]
# # # p=model.predict(test)
# # p2=model.predict(amount)


# # k=model.MSE(p2)
# # print(k)