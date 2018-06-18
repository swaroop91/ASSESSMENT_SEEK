import pandas as pd

# b) Extract the following fields from the jobpost column:
fields = ["Title",'Duration','Location','JobDescription','JobRequirment','RequiredQual','Salary','Deadline','AboutC']
jobpostdf = pd.read_csv("C:\Files\online-job-postings\data job posts.csv",usecols=fields)
print(jobpostdf.columns)
print(jobpostdf.tail())