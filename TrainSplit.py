from sklearn.model_selection import train_test_split
from DataPrep import X
from DataPrep import y

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.1,
    random_state=42
)
