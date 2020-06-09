# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 02:35:59 2020

@author: dhk13
"""
import cx_Oracle

#한글 지원 방법
import os
os.putenv('NLS_LANG', '.UTF8')

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
connection = cx_Oracle.connect('admin','','lolgg.culykwl5fmgv.ap-northeast-2.rds.amazonaws.com:1521/ORCL')

cursor = connection.cursor()



def GameDataParser(path):
    #Output으로 받은 txt파일을 파싱하는 함수 
    #각 줄의 형식
    #게임 id | 100,aa,bb,cc|200,aa,bb,cc|win, loss
    f=open(path, 'r')
    line=f.readline()
    while (line):
        print(line)
        row1=[int(line.split('|')[0]),1,line.split('|')[3][0]]
        row2=[int(line.split('|')[0]),2,line.split('|')[3][1]]
        
        cursor.execute("""
                       INSERT INTO
                       MATCHDATA (GameId, Team, Result_)
                       VALUES(:1, :2, :3)
                       """, row1
                       )
        cursor.execute("""
                       INSERT INTO
                       MATCHDATA (GameId, Team, Result_)
                       VALUES(:1, :2, :3)
                       """, row2
                       )
        line=f.readline()
    return


GameDataParser("C:/Users/한동훈/Desktop/Github/League_of_Legend_4U/lolapi/gamedata0609.txt")

