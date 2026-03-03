from Model import model
from TrainSplit import X_test
from TrainSplit import y_test
from sklearn.metrics import mean_squared_error

predictions = model.predict(X_test)
print(10 ** predictions)

error = mean_squared_error(y_test, predictions)
print("Error:", error)
