import pandas as pd

# F. Write functions to identify null/NA values and to replace null/NA values with a custom message in “Duration” column
import nltk
fields = ["Title",'Duration','Location','JobDescription','JobRequirment','RequiredQual','Salary','Deadline','AboutC','Company','date']
jobpostdf = pd.read_csv("C:\Files\online-job-postings\data job posts.csv",usecols=fields)
jobpostdf.Duration.fillna("Duration value is NA")