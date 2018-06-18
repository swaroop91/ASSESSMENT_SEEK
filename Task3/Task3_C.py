import pandas as pd

# c.Identify the company with the most number of job ads in the past 2 years
fields = ["Title",'Duration','Location','JobDescription','JobRequirment','RequiredQual','Salary','Deadline','AboutC','Company','date']
jobpostdf = pd.read_csv("C:\Files\online-job-postings\data job posts.csv",usecols=fields)
jobpostadsdf=jobpostdf.groupby(['Company']).size().reset_index(name='Counts').sort_values(by='Counts',ascending=False).iloc[0:1]
print(jobpostadsdf)