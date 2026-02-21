#                                       DATA CLEANINIG ON NETFLIX DATASET 

import pandas as pd
netflix = pd.read_csv("netflix.csv")
# print(netflix.head)
#remove duplicate values
netflix = netflix.drop_duplicates()

# print(netflix.isnull().sum())    --> all nAn columns
"""" print(netflix["rating"].unique())  --> all uniqe rating items
netflix = netflix.fillna({"cast":"Unknown"})
"""
# nan data replace to unknown 
netflix.fillna({"cast":"Unknown","director":"Unknown","country":"Unknown"},inplace=True)
#print(netflix["country"].head(10))

#change datatype of date column
netflix["date_added"] =pd.to_datetime(netflix["date_added"],errors="coerce")
#print(netflix["date_added"].dtype)
#print(netflix["date_added"].head(10))

netflix = netflix.dropna(subset=["rating"])
#print(netflix["rating"].unique())
#print(netflix["rating" ])

#  deleting space between titles and listed in 
col = ["title", "listed_in","country"]
netflix[col] = netflix[col].apply(lambda x : x.str.strip())

#seprate columns for movie time and seasons 

netflix['duration_num'] = netflix['duration'].apply(lambda x: x.split(' ')[0] if isinstance(x, str) else 0)
netflix['duration_unit'] = netflix['duration'].apply(lambda x: x.split(' ')[1] if isinstance(x, str) else "Unknown")

#cahnge the data type of duration_num column
netflix = netflix.drop(columns=["duration"]) 
netflix["duration_num"]=netflix["duration_num"].astype(int)

# now save the cleaned file to new file 

#dnetflix.to_csv("netflix_cleaned.csv", index=False)           # index=False zaroor likhna

#print("File saved as netflix_cleaned .csv!")

#print(netflix["duration_num"])

#                                     SQL CONNENCT WITH PYTHON 

import sqlite3
from sqlalchemy import create_engine

# 1. Database file se connect karo (Ye file folder mein apne aap ban jayegi)
"""conn = sqlite3.connect('netflix.db')"""
engine = create_engine(f'mysql+mysqlconnector://root:gauravbrj09@localhost/netflix')
# 2. DataFrame ko SQL table mein convert karo
netflix.to_sql('movies_data', con=engine, if_exists='replace', index=False)
