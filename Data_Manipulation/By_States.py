import pandas as pd
from sqlalchemy import create_engine
import pymysql

engine=create_engine('mysql+pymysql://root:Las1las1@35.245.122.202/FCC')
table_list = [
"dec2014_v3",
"dec2015_v4",
"dec2016_v2",
"dec2017_v2",
"jun2015_v4",
"jun2016_v3",
"jun2017_v2",
"jun2018_v1"
]

for t in table_list:
	query_consumer = "SELECT StateAbbr,AVG(MaxAdDown) AS download,AVG(MaxAdUp) AS upload, \
	COUNT(DISTINCT blockcode) AS blocks, COUNT(DISTINCT `Provider_Id`) AS providers \
	FROM {} \
	WHERE consumer = 1 \
	GROUP BY `StateAbbr`;".format(t)
	
	query_business = "SELECT StateAbbr,AVG(MaxAdDown) AS download,AVG(MaxAdUp) AS upload, \
	COUNT(DISTINCT blockcode) AS blocks, COUNT(DISTINCT `Provider_Id`) AS providers \
	FROM {} \
	WHERE business = 1 \
	GROUP BY `StateAbbr`;".format(t)

	state_consumer = pd.read_sql(query_consumer, engine)
	state_business = pd.read_sql(query_business, engine)

	state_consumer.to_csv(t+'_consumer_results.csv',index = None, header=True)
	state_business.to_csv(t+'_business_results.csv',index = None, header=True)









