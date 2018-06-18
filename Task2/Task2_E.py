import pandas as pd
import numpy as np

# e) Identify the top 5 worst performing products on a biweekly basis
salesdf = pd.read_csv("C:/Files/Sales_Transactions_Dataset_Weekly.csv")
products=salesdf[salesdf.columns[0]]
weekDf=salesdf[salesdf.columns[1:53]]
for n in range(len(weekDf.columns)-1):
	weekSubSet=weekDf[weekDf.columns[n:n+2]]
	sumVal=np.sum(weekSubSet,axis=1).to_frame()
	sumVal.columns=['Quantity']
	worst_product=pd.concat([products,sumVal],axis=1)
	worst_product_5=worst_product.sort_values(by=['Quantity'],ascending=True).iloc[0:5]
	print("BiWeek:"+str(n+1))
	print(worst_product_5)