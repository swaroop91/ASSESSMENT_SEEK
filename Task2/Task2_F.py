import pandas as pd
import numpy as np

# f) Identify outliers from the data and output the corresponding week numbers
salesdf = pd.read_csv("C:/Files/Sales_Transactions_Dataset_Weekly.csv")
salesdfSubset=salesdf[salesdf.columns[1:53]]
for n in range(51):
	n=n+1
	colDF=salesdfSubset[salesdfSubset.columns[n]]
	outliers = colDF[colDF > colDF.mean() + 3 * colDF.std()]
	print(outliers.to_frame().columns[0] +" Outliers")
	print(outliers.tolist())