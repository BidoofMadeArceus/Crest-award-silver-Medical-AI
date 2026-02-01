import numpy as nfrom rdkit import chem
from rdkit.chem import allchem

def make_morgan_fp(mol, radius=2, nBits=1024):
  fp= AllChem.GetMorganFingerprintAsBitVect(
    mol,
    radius=radius,
    nBits=nBits
  )
  return np.array(fp)
