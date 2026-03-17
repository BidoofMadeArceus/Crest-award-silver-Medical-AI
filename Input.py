from Model import model
from featurize import make_morgan_fp

predictThis = input("please input valid SMILES code for LD50 prediction: ")

make_morgan_fp(predictThis)

prediction = model.predict(fp)

print(prediction)
