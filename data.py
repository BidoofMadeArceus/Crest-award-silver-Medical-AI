import pandas as pd

df = pd.read_csv("dataset.csv")
df = df.dropna(subset=["SMILES"])

from rdkit import Chem

df["Mol"] = df["SMILES"].apply(Chem.MolFromSmiles)
df = df[df["Mol"].notna()].reset_index(drop=True)
