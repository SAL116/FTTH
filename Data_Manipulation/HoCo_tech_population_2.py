import pandas as pd
# returns each HoCo Ecach TechCode and their popluation
# this needs to be fixed - dupe blockCode

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
# import os.path
# import time
# import pickle
# file = open('blockpop.pickle', 'rb')
# ref = pickle.load(file)    

# def get_pop(data,state):
#     global ref
#     pop = 0
#     for i in data.split('$')[:-1]:
#         pop += int(ref[state][i])
#     return pop
allyear = list()
for year in table_list:
	year_list = list()
	for state in state_list:
		name = "/home/analysis/sql_results/providers/HCP/new2/"+year[:7]+"_"+state+".csv"
		# while not os.path.exists(name):
		# 	time.sleep(10)
		df = pd.read_csv(name,dtype=object)
		#df['pop'] = df[df.columns[2]].apply(lambda x: get_pop(x,state))
		year_list.append(df)
	year_out = pd.concat(year_list)
	year_out['population'] = year_out['population'].astype(float)
	year_out = year_out.groupby(['HocoNum','TechCode'])['population'].sum().reset_index()
	year_out['year'] = year[:7]
	year_out.to_csv("national/{0}_national.csv".format(year),index=False)
	allyear.append(year_out)
allyear = pd.concat(allyear)
allyear.to_csv("national/HoldingCompany_pop.csv",index=False)



