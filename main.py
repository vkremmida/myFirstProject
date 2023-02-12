import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv("finance_liquor_sales_1.csv")
df.groupby(['zip_code','store_number']).sum()
#df["Percentage of sales per store"] = df.groupby(['store_number'])["sale_dollars"] / df["sale_dollars"].sum() * 100)
df.to_csv('finance_liquor_sales_2.csv')
x = np.array(df['zip_code'])

y = np.array(df['bottles_sold'])

plt.scatter(x, y)
plt.title("Bottles Sold")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")

plt.show()
