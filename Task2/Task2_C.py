import pandas as pd
import numpy as np

# c) Identify the best performing product (based on volume)
salesdf = pd.read_csv("C:/Files/Sales_Transactions_Dataset_Weekly.csv")
products=salesdf[salesdf.columns[0]]
sumVal=np.sum(salesdf[salesdf.columns[1:53]],axis=1).to_frame()
sumVal.columns=['Quantity']
best_product=pd.concat([products,sumVal],axis=1)
top_product=best_product.sort_values(by=['Quantity'],ascending=False).iloc[0:1]
print("Best Product:")
print(top_product)