#a)Download the following Kaggle dataset: Jobposts Data https://www.kaggle.com/madhab/jobposts/

from urllib import request
url = 'https://www.kaggle.com/madhab/jobposts/downloads/data%20job%20posts.csv/1'
def download_data(csv_url):
	response = request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n")
	dest_url = r'C:\Files\online-job-postings\data job posts.csv'
	fx = open(dest_url, "w")
	for line in lines:
		fx.write(line + "\n")
	fx.close()
download_data(url)
