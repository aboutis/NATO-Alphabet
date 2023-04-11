import pandas as pd

name = input("Name: ").upper()
data = pd.read_csv("nato_phonetic_alphabet.csv")

lista = {row.letter: row.code for (index, row) in data.iterrows()}
output = [lista[letter] for letter in name]
print(output)
