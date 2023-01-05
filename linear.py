import pandas as pd
from matplotlib import pyplot as plt
dataset = pd.read_csv('slr.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,:-1].values
from sklearn.model_selection import train_test_split
x_test,x_train,y_test,y_train=train_test_split(x,y,test_size=1/3,random_state=0)
from sklearn.linear_model import LinearRegression
models=LinearRegression()
models.fit(x_train,y_train)
y_pred = models.predict(x_test)
plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,models.predict(x_train),color='blue')
plt.title('Train_Data')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.show()
plt.scatter(x_test,y_test,color='red')
plt.plot(x_test,models.predict(x_test ),color='blue')
plt.title('Test_Data')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.show()
