
# Output:
# Each Company Each techCode's Population BY State
# Will redo since TechCode has duplicates in BlockCodes

import pandas as pd
from sqlalchemy import create_engine
import pymysql

engine=create_engine('mysql+pymysql://root:Las1las1@35.245.122.202/FCC')

table_list = [
"dec2014_v3",
# "dec2015_v4",
# "dec2016_v2",
# "dec2017_v2",
# "jun2015_v4",
# "jun2016_v3",
# "jun2017_v2",
"jun2018_v1"
]

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


for year in table_list:
	for state in state_list:
		query = """
		SELECT HocoNum,TechCode,BlockCode 
		FROM {0}
		WHERE StateAbbr = \"{1}\"
		;
		""".format(year,state)
		df = pd.read_sql(query, engine)
		df['population'] = df['BlockCode'].apply(lambda x: int(ref[state][x]))
		df['population'] = df['BlockCode'].apply(lambda x: int(ref[state][x]))
		df = df.groupby(['HocoNum','TechCode'])['population'].sum().reset_index()
		df.to_csv("{0}_{1}.csv".format(year[:7],state),index=False)


