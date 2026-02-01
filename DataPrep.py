import numpy as np
from data import df
from featurize import make_morgan_fp

X = np.array([
  make_morgan_fp(mol)
  for mol in df["mol"]
             ])

Y = np.array([df["LD50_mg_kg_oral"]])
