from sklearn.linear_model import RandomForestRegressor
from TestSplit import X_train
from TestSplit import y_train

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)
