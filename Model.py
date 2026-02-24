from sklearn.linear_model import LinearRegression
from TestSplit import X_train
from TestSplit import y_train

model = LinearRegression()
model.fit(X_train, y_train)
