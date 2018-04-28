import pandas as pd

adv = pd.read_csv('Advertising.csv')
tv_budget_x = adv.TV.tolist()

print(tv_budget_x)
