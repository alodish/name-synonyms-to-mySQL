import pandas as pd
import pymysql
from sqlalchemy import create_engine

all_lines = []
k = 0

with open('btn_givennames_synonyms.txt', 'r', encoding='cp437') as txt:
    for line in txt:
        if k >= 8:
            temp_line = line.strip('\n')
            temp_line = temp_line.split('\t')
            all_lines.append([temp_line[0], temp_line[2]])
        else:
            k += 1

columns = ['Name', 'Nicknames']
df = pd.DataFrame(all_lines, columns=columns)

table_name = 'name_synonyms'
sql_engine = create_engine('mysql+pymysql://root:password@127.0.0.1/names_nicknames', pool_recycle=3600)
db_connection = sql_engine.connect()

frame = df.to_sql(table_name, db_connection, if_exists='fail')
