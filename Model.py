from sklearn.ensemble import RandomForestRegressor
from TrainSplit import X_train
from TrainSplit import y_train

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)
