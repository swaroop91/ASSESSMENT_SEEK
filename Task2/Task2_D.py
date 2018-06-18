import pandas as pd
import numpy as np

# d) Identify the most promising product (emerging product)
salesdf = pd.read_csv("C:/Files/Sales_Transactions_Dataset_Weekly.csv")
products=salesdf[salesdf.columns[0]]
sd=np.std(salesdf[salesdf.columns[1:53]],axis=1).to_frame()
sd.columns=['Product_SD']
emerging_product=pd.concat([products,sd],axis=1)
emerging_product_1=emerging_product.sort_values(by=['Product_SD'],ascending=False).iloc[0:1]
print("Emerging Product:")
print(emerging_product_1)