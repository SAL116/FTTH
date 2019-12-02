#return for each timestamp
#each ISP's population by tech type, UNIQUE 

import pandas as pd
from sqlalchemy import create_engine
import pymysql
import sys
import os
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
file = open('/home/analysis/Final/ISP/blockpop_int.pickle', 'rb')
ref = pickle.load(file)   

year = sys.argv[1]
out_list = list()
#for year in table_list:
for state in state_list:
	# query = """
	# SELECT BlockCode,TechType,MAX(HighSpeed) AS HighSpeed
	# FROM {0}
	# WHERE StateAbbr = \"{1}\"
	# AND Consumer = 1
	# GROUP BY BlockCode,TechType
	# ;
	# """.format(year,state)
	#df = pd.read_sql(query, engine)
	df = pd.read_csv("/home/analysis/Final/population/{0}/{1}.csv".format(year[:7],state),dtype=object)
	df['BlockCode'] = df['BlockCode'].astype(str)
	#df.to_csv("/home/analysis/Final/population/{0}/{1}.csv".format(year[:7],state),index=False)
	df['population'] = df['BlockCode'].apply(lambda x: int(ref[state][x]))
	df = df.groupby(['TechType','HighSpeed'])['population'].sum().reset_index()
	df['state'] = state
	out_list.append(df)
allstates = pd.concat(out_list)
allstates.to_csv("/home/analysis/Final/population/{0}/techtype_each_state.csv".format(year[:7]),index=False)
out = allstates.groupby(['TechType','HighSpeed'])['population'].sum().reset_index()
out.to_csv("/home/analysis/Final/ISP/population/{0}/techtype_pop.csv".format(year[:7]),index=False)