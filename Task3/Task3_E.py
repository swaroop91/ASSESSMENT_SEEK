import pandas as pd

# E. Clean text and generate new text from Job Responsibilities column: The new text shall not contain any stop words, and the plural words shall be converted into singular words.
import nltk
stopwords = nltk.corpus.stopwords.words('english')
RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))
fields = ["Title",'Duration','Location','JobDescription','JobRequirment','RequiredQual','Salary','Deadline','AboutC','Company','date']
jobpostdf = pd.read_csv("C:\Files\online-job-postings\data job posts.csv",usecols=fields)
words = (jobpostdf.JobRequirment
           .str.lower()
           .replace([r'\|', RE_stopwords], [' ', ''], regex=True)
)
jobpostdf.JobRequirment=words
print(jobpostdf.tail())