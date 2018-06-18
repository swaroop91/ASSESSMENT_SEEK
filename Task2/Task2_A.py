import pandas as pd
import numpy as np

# a) Write code to download the following Kaggle dataset: Weekly Sales Transaction Data: https://www.kaggle.com/crawford/weekly-sales-transactions
from urllib import request
url = 'https://www.kaggle.com/crawford/weekly-sales-transactions/downloads/Sales_Transactions_Dataset_Weekly.csv/1'
def download_data(csv_url):
	response = request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n")
	dest_url = r'C:/Files/Sales_Transactions_Dataset_Weekly.csv'
	fx = open(dest_url, "w")
	for line in lines:
		fx.write(line + "\n")
	fx.close()
download_data(url)
salesdf = pd.read_csv("C:/Files/Sales_Transactions_Dataset_Weekly.csv")
print(salesdf)
