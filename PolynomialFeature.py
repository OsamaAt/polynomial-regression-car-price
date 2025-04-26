import numpy as np 
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

x_train=np.array([1,2,3,4,5,6,7,8,9]) #cars in year
y_train=np.array([30,27,24,20,17,15,13,12,11]) #price in 1000 dollars

x_train=x_train.reshape(-1,1)

poly=PolynomialFeatures(degree=2) # Can Change The Degree
x_train_poly=poly.fit_transform(x_train)

model=LinearRegression()
model.fit(x_train_poly , y_train)

x_test=np.array([[5]])
x_test_poly=poly.transform(x_test)

predict_price=model.predict(x_test_poly)
print(f'Predicted Price For 5 Years Old Car is  : ${predict_price[0]*1000:.2f}')

x_fit=np.linspace(1,9,100).reshape(-1,1)
x_fit_poly=poly.transform(x_fit)
y_fit=model.predict(x_fit_poly)

plt.scatter(x_train , y_train , color='red' ,label='Original Data')
plt.plot(x_fit , y_fit , color='blue' , label='Polynomial Fit')
plt.xlabel('Car Age In Years')
plt.ylabel('Price In $')
plt.legend()
plt.show()
