# Add 2 columns for each Table
# First, Aggregate Tech Code to Tech Type - thus won't be dupes 
# Second, indicate if over 100M in download - High speed internet access

import pandas as pd
from sqlalchemy import create_engine
import pymysql
import sys

engine=create_engine('mysql+pymysql://root:Las1las1@35.245.122.202/FCC')
t = sys.argv[1]

query1 = """
ALTER TABLE {}
ADD COLUMN TechType varchar(8) 
GENERATED ALWAYS AS (CASE
    WHEN TechCode IN ('10','11','12','20','30') THEN "DSL"
    WHEN TechCode IN ('40','41','42','43') THEN "DOCSIS"
    WHEN TechCode = '50' THEN "FTTH"
    ELSE "Other"
END)
STORED;
""".format(t)

query2 = """
ALTER TABLE {}
ADD COLUMN HighSpeed tinyint(1)
GENERATED ALWAYS AS (IF(MaxAdDown>100,1,0))
STORED;
""".format(t)

with engine.connect() as con:
	con.execute(query1)
	con.execute(query2)

