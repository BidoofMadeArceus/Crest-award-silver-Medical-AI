import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem


def make_morgan_fp(mol, radius=2, nBits=1024):
  fp= AllChem.GetMorganFingerprintAsBitVect(
    mol,
    radius=radius,
    nBits=nBits
  )
  return np.array(fp)
