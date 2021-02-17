import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, sys
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.types import INT,FLOAT, VARCHAR, SMALLINT
from importlib import reload
import time


reload(sys)

mySqlAddress = sys.argv[1]
mySqlUserName = sys.argv[2]
mySqlPassword = sys.argv[3]

day = time.strftime('%Y-%m-%d',time.localtime(time.time())).split("-")
mySqlDataBase = "_".join(day)
hour = time.strftime('%H',time.localtime(time.time()))
mySqlTable = "hour_" + hour

currentPath = os.getcwd()

pd.set_option('expand_frame_repr', False)
table_0 = pd.read_csv(
        filepath_or_buffer = currentPath + '/' + 'EPS_2.csv',
        sep = ','
        )
table_0 = table_0.dropna(how = 'any').reset_index(drop=True)

# 连接数据库MySql
con = mysql.connector.connect(
    host=myS

qlAddress,
    user=mySqlUserName,
    password=mySqlPassword,
    database="mysql"
)

# 获取游标
cursor = con.cursor()
# 创建database
cursor.execute("CREATE DATABASE IF NOT EXISTS " + mySqlDataBase)
cursor.execute("USE " + mySqlDataBase)
# 创建table
cursor.execute("CREATE TABLE IF NOT EXISTS " + mySqlTable + " (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, Ticker VARCHAR(10), Year SMALLINT UNSIGNED, EPSIE FLOAT)")
con.commit()
cursor.close()
con.close()

# SQLAlchemy创建表连接
connect_info = 'mysql+mysqlconnector://' + mySqlUserName + ':' + mySqlPassword + '@' + mySqlAddress + ':3306/' + mySqlDataBase
engine = create_engine(connect_info)

# 插入数据，如果存在则替换
print("Insert data into " + mySqlDataBase + ":" + mySqlTable + "\n")
table_0.to_sql(name= mySqlTable,
               con=engine,
               if_exists='replace',
               index_label='id',
               dtype = {
                   'id': INT(),
                   'Ticker': VARCHAR(length=10),
                   'Year': SMALLINT(),
                   'EPSIE': FLOAT()
               }
               )

# 读取数据
print("load data from " + mySqlDataBase + ":" + mySqlTable + "\n")
sql = "SELECT Ticker, Year, EPSIE FROM " + mySqlTable
table_0 = pd.read_sql(sql, con=engine)

company_name = np.unique(table_0['Ticker'].tolist())
print(table_0.Year)
time_0 = 2009 #start time
time_T = 2019 #end time
period = time_T-time_0-1
coef = 1 #set deviation coefficient
eps = 0.00001

#过去3年间连续2年EPS均偏离均值coef*std, return True
def f(L):
    L = L.split(',')
    if len(L) > 1:
        if int(L[-1])-int(L[-2])==1 and int(L[-1]) > time_period[-2]:
            return True
        else:
            return False
    else:
        return False
    
#data formatting
time_period = list(range(time_0,time_T))
df = pd.DataFrame(columns=time_period, index = company_name)
for t in time_period:
    for name in company_name:
        temp = table_0[(table_0.Year==t)&(table_0.Ticker==name)].index.tolist()
        if temp !=[]:
            df.at[name,t] = table_0.iat[temp[0], -1]
        else:
            df.at[name,t] = 0

#selecting stocks with increasing EPS for certain time period
for i in range(len(time_period)-1):
    df = df[df[time_period[i+1]]>df[time_period[i]]]
    
#calculate slope and standard deviation
df['k'] = (df[time_period[-1]]-df[time_period[0]])/period 
df2 = df[time_period].T.diff().T
df2['std'] = df2.std(1)
df2['k'] = df['k']
df2 = df2.dropna(how = 'any', axis = 1)
name_list = df2._stat_axis.values.tolist()

#'info' shows which year has obvious deviation
df2['info_up'] = ''
df2['info_down'] = ''
time_period = time_period[1:]
for i in name_list:
    df2.at[i,'info_up'] = ''
    df2.at[i,'info_down'] = ''
    L_up = []
    L_down = []
    for j in time_period:
        if (df2.at[i,j] - (df2.at[i,'k'] + coef * df2.at[i,'std'])) > eps:
            L_up.append(str(j))
            df2.at[i,'info_up'] =','.join(L_up)
        elif df2.at[i,'k'] - coef * df2.at[i,'std'] - df2.at[i,j] > eps:
            L_down.append(str(j))
            df2.at[i,'info_down'] =','.join(L_down)

df['std'] = df2['std']
df['info_up'] = df2['info_up']
df['info_down'] = df2['info_down']
df['info'] = df['info_up'].map(f)
selected_stock = df[df['info']==True].index.tolist()
print(selected_stock)

df1 = df.iloc[:, 0:10]
ax = df1.plot(kind='bar')
fig = ax.get_figure()

# 保存图片
day1 = time.strftime('%Y-%m-%d',time.localtime(time.time()))
figureFolder = currentPath + '/' + "figure" + '/' + day1
if not os.path.isdir(figureFolder):
    os.makedirs(figureFolder)
fig.savefig(figureFolder + '/' + hour + ".png")

df.to_csv('output.csv', index = True)


