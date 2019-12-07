import pymysql
import requests
def say():
    print ("hi")
def dbcheck() :
    pw='당신의 db의 비밀번호를 넣어주세요'
    conn = pymysql.connect(host='localhost', user='root', password=pw,
                           db='testdb', charset='utf8')
    curs=conn.cursor()

    #genie 테이블이 없다면 테이블 생성

    check="""show tables like 'genie'"""
    curs.execute(check)
    result=curs.fetchall()
    result_genie=len(result)
    if result_genie==0 : #없다면생성
        print("db에 genie테이블이 없으시므로 테이블을 생성합니다.")
        make_table="""
    create table genie(
    title varchar(100),
    artist varchar(100),
    score int,
    primary key(title)
    );
    """
        curs.execute(make_table)
    else :
        print("이미 genie table이 db에 있습니다")
    #melon 테이블이 없다면 테이블 생성

    check="""show tables like 'melon'"""
    curs.execute(check)
    result=curs.fetchall()
    result_melon=len(result)

    if result_melon==0 : #없다면 생성
        print("db에 melon테이블이 없으시므로 테이블을 생성합니다.")
        make_table="""
    create table melon(
    title varchar(100),
    artist varchar(100),
    score int,
    primary key(title)
    );
    """
        curs.execute(make_table)
    else :
        print("이미 melon table이 db에 있습니다")
    #bugs 테이블이 없다면 테이블 생성

    check="""show tables like 'bugs'"""
    curs.execute(check)
    result=curs.fetchall()
    result_bugs=len(result)
    if result_bugs==0: #없다면 생성
        print("db에 bugs테이블이 없으시므로 테이블을 생성합니다.")
        make_table="""
    create table bugs(
    title varchar(100),
    artist varchar(100),
    score int,
    primary key(title)
    );
    """
        curs.execute(make_table)
    else :
        print("이미 bugs table이 db에 있습니다")

    conn.commit()
    conn.close()

