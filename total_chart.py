import requests
import new
import pymysql
import bugs1
import melon1
import genie1
import pandas as pd
import matplotlib.pyplot as plt
import platform
import matplotlib
from matplotlib import font_manager,rc, style
from sqlalchemy import create_engine

from bs4 import BeautifulSoup



new.dbcheck()
melon1.melon1()
bugs1.bugs1()
genie1.genie1()
pw='gusgh4528'
#테이블이 있는지 확인하는 모듈의 함수
conn = pymysql.connect(host='localhost', user='root', password=pw,
                       db='testdb', charset='utf8')
curs=conn.cursor()
sql="truncate table total"#데이터베이스 초기화 시킨다.
curs.execute(sql)
check="""show tables like 'total'"""
curs.execute(check)
result=curs.fetchall()
result_total=len(result)
if result_total==0 : #없다면생성
    print("db에 total테이블이 없으시므로 테이블을 생성합니다.")
    make_table="""
create table total(
title varchar(100),
artist varchar(100),
img varchar(150),
score float,
count int,
primary key(score)
);
"""
    curs.execute(make_table)
else :
    print("이미 total table이 db에 있습니다")


engine = create_engine('mysql+pymysql://root:gusgh4528@localhost/testdb')
conn1 = engine.connect()

Mdata = pd.read_sql_table('melon', conn1)

Gdata = pd.read_sql_table('genie', conn1)
Bdata = pd.read_sql_table('bugs', conn1)


temp_total=[]
mtmp = Mdata.values.T.tolist()
gtmp = Gdata.values.T.tolist()
btmp = Bdata.values.T.tolist()
count=1
for i in range(len(mtmp[0])):
    total_title=mtmp[0][i]
    total_artist=mtmp[1][i]
    total_img=mtmp[2][i]
    total_score=float(mtmp[3][i])*0.6312312
    total_list=[total_title,total_artist,total_img,total_score,count]
    temp_total.append(total_list)
    print(temp_total[i])
print("rnqnsnsndansjlfnkaslnlkasnkldnaskldnlkasndkl")
print(len(temp_total))
print("")
print("")
sql="""INSERT INTO total (title, artist, img,score,count) VALUES (%s, %s, %s ,%s,%s)"""
for i in range(len(gtmp[0])):
    check_ex=0
    for j in range (len(temp_total)) :
        if temp_total[j][0] == gtmp[0][i] :
            temp_total[j][4]=int(temp_total[j][4])+1 #카운트 값 증가
            temp_total[j][3]+=float(gtmp[3][i])*1.0123123# 스코어값 증가
            break
        else :
            check_ex+=1
    if check_ex==len(temp_total)  :# 모든 temp_total값을 다돌아도 해당하는 제목이 없다면
        total_title=gtmp[0][i]
        total_artist=gtmp[1][i]
        total_img=gtmp[2][i]
        total_score=float(gtmp[3][i])*1.0123123
        total_list=[total_title,total_artist,total_img,total_score,1]
        temp_total.append(total_list)
        print(total_list)
print("")
print ("또 구분")
print("")
print(len(temp_total))

for i in range(len(gtmp[0])):
    
    
    check_ex=0
    for j in range (len(temp_total)) :
        if temp_total[j][0] == btmp[0][i] :
            temp_total[j][4]=int(temp_total[j][4])+1 #카운트 값 증가
            temp_total[j][3]+=float(btmp[3][i])*1.93213# 스코어값 증가
            break
        else :
            check_ex+=1
    if check_ex==len(temp_total)  :# 모든 temp_total값을 다돌아도 해당하는 제목이 없다면
        total_title=btmp[0][i]
        total_artist=btmp[1][i]
        total_img=btmp[2][i]
        total_score=float(btmp[3][i])*1.93213
        total_list=[total_title,total_artist,total_img,total_score,1]
        temp_total.append(total_list)
        print(total_list)
print("tbasjdknaskld")
for j in range (len(temp_total)) :
    
    rc=j+1
    temp_total[j][3]=temp_total[j][3]/float(temp_total[j][4])
    print(temp_total[j])
    curs.execute(sql,(temp_total[j][0],temp_total[j][1],temp_total[j][2],temp_total[j][3],temp_total[j][4]) )
    conn.commit()

print(len(temp_total))


conn.commit()
conn.close()