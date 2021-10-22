import pandas as pd
excel = pd.read_excel("OrdersWithNullsHarshit.xlsx", index_col=0, sheet_name='Orders')
df = excel[["Order Date", "Sales"]].sort_values("Order Date", ascending=False)
df.to_csv("OrdersWithNullsHarshit.csv", index=False)