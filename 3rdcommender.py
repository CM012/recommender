import pandas as pd

df = pd.DataFrame({
    'Variable':['A', 'B', 'C'],
    'Weight': [1.5, 2, 3],
    'Carbon': [5, 3, 4],
    'Protein': [2, 2, 6],
    'Fat': [2, 1, 3]
})

from pulp import *
prob = LpProblem('Total_nutrition', LpMaximize ) # Objective function

inv_item = list(df['Variable']) # Variable name

inv_vars= LpVariable.dicts('Vairable', inv_item, lowBound=0, cat='float')

