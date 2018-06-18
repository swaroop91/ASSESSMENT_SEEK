import pandas as pd
import numpy as np

# b) Find median, mean, min and max values for each product Weekly Sales Transaction Data: https://www.kaggle.com/crawford/weekly-sales-transactions
salesdf = pd.read_csv("C:/Files/Sales_Transactions_Dataset_Weekly.csv")
Mean=np.median(salesdf[salesdf.columns[1:53]],axis=1).tolist()
Median=np.mean(salesdf[salesdf.columns[1:53]],axis=1).tolist()
Min=np.min(salesdf[salesdf.columns[1:53]],axis=1).tolist()
Max=np.max(salesdf[salesdf.columns[1:53]],axis=1).tolist()
print("Mean:")
print(Mean)

print("Median:")
print(Median)

print("Min:")
print(Min)

print("Max:")
print(Max)