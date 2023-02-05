import pandas as pd
import numpy as np
df = pd.read_csv("finance_liquor_sales_1.csv")
df["Percentage of sales per store"] = ((df["sale_dollars"] / df["sale_dollars"].sum()) * 100)
cn = df.groupby(['zip_code','Percentage of sales per store'])
print(cn.aggregate(np.sum))
df.to_csv('finance_liquor_sales_2.csv')



