# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 01:53:30 2020

@author: dhk1349
"""

#필요한 함수
"""
API로 가져온 데이터를 revise하는 함수가 필요.
-경기 결과를 집계하는 함수
"""

def GameDataParser(path):
    #Output으로 받은 txt파일을 파싱하는 함수 
    #각 줄의 형식
    #게임 id | 100,aa,bb,cc|200,aa,bb,cc|win, loss
    f=open(path, 'r')
    line=f.readline()
    while (line):
        for i in line.split('|'):
            print(i.split(','), end="")
        print()
        line=f.readline()
    return


GameDataParser("C:/Users/한동훈/Desktop/Github/League_of_Legend_4U/lolapi/gamedata0609.txt")