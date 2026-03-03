from Model import model
from TrainSplit import X_test
from TrainSplit import y_test
from sklearn.metrics import mean_squared_error

predictions = model.predict(X_test)
predictions = 10 ** predictions
print(predictions)

error = mean_squared_error((10 ** y_test), predictions)
print("Error:", error)
