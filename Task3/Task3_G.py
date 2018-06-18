import pandas as pd

# G. Store the results in a new Dataframe/SQL table(s)
fields = ["Title",'Duration','Location','JobDescription','JobRequirment','RequiredQual','Salary','Deadline','AboutC','Company','date']
jobpostdf = pd.read_csv("C:\Files\online-job-postings\data job posts.csv",usecols=fields)
jobpostdf.Duration=jobpostdf.Duration.fillna("Duration value is NA")
print(jobpostdf.tail())
