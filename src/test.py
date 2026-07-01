from sklearn.linear_model import LogisticRegression

import pandas as pd

df = pd.DataFrame({'name': 'Filip', 'age': 50})

birth_year = 2026 - df['age']

print("Filip was born in the year:", birth_year[0])

print("oops, filip is quite old!")
