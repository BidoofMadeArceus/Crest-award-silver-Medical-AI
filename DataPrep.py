import numpy as np
from data import df
from featurize import make_morgan_fp
from rdkit import RDLogger

RDLogger.DisableLog("rdApp.warning")

X = np.array([
  make_morgan_fp(mol)
  for mol in df["Mol"]
             ])

Y = np.array(df["LD50_mg_kg_oral"])

print(X)
print(Y)
