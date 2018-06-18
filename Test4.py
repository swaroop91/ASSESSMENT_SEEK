#a) Download test.csv from https://www.kaggle.com/rishisankineni/text-similarity/data
#b) Load the data to a Spark/Pandas data frame
#c) Calculate similarity between description_x and description_y and store resultant scores in a new column
#d) Parallelise the matching process using SPARK environment.

#a)Download the following Kaggle dataset: Jobposts Data https://www.kaggle.com/madhab/jobposts/

from urllib import request
url = 'https://www.kaggle.com/rishisankineni/text-similarity/downloads/test.csv/1'
def download_data(csv_url):
	response = request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n")
	dest_url = r'/home/cloudera/Desktop/test.csv'
	fx = open(dest_url, "w")
	for line in lines:
		fx.write(line + "\n")
	fx.close()
download_data(url)

pyspark --packages com.databricks:spark-csv_2.10:1.4.0
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
descdf = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('file:///home/cloudera/Desktop/test.csv')
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()
from difflib import SequenceMatcher
descdf.map(lambda row:(row[0],row[1],row[2],similar(row[1],row[2]))).toDF(["test_id","description_x","description_y","similarity"]).show()
