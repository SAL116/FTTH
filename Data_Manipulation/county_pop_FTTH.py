#return for each timestamp
#each county's popluation with FTTH
#this is fixed - no dupe blockcodes

import pandas as pd
from sqlalchemy import create_engine
import pymysql
import sys
engine=create_engine('mysql+pymysql://root:Las1las1@35.245.122.202/FCC')


state_list = ["AL",
"AK",
"AZ",
"AR",
"CA",
"CO",
"CT",
"DE",
"DC",
"FL",
"GA",
"HI",
"ID",
"IL",
"IN",
"IA",
"KS",
"KY",
"LA",
"ME",
"MD",
"MA",
"MI",
"MN",
"MS",
"MO",
"MT",
"NE",
"NV",
"NH",
"NJ",
"NM",
"NY",
"NC",
"ND",
"OH",
"OK",
"OR",
"PA",
"RI",
"SC",
"SD",
"TN",
"TX",
"UT",
"VT",
"VA",
"WA",
"WV",
"WI",
"WY"]

import pickle
file = open('blockpop_int.pickle', 'rb')
ref = pickle.load(file)   

year = sys.argv[1]
#for year in table_list:
out_list = list()
for state in state_list:
	query = """
	SELECT DISTINCT BlockCode 
	FROM {0}
	WHERE StateAbbr = \"{1}\"
	AND Consumer = 1
	AND TechCode = 50
	;
	""".format(year,state)
	df = pd.read_sql(query, engine)
	df['population'] = df['BlockCode'].apply(lambda x: int(ref[state][x]))
	df['county_code'] = df['BlockCode'].apply(lambda x: x[:5])
	df = df.groupby(['county_code'])['population'].sum().reset_index()
	out_list.append(df)
out = pd.concat(out_list)
out.to_csv("{0}.csv".format(year[:7]),index=False)


