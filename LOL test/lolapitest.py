# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:50:27 2020

@author: dhk13
"""
#from ApiLib import APIs
#from lolapi import APIs

from lolapi import APIs
import time
summoner="Antistan"
apikey="RGAPI-e82a3604-7d04-4baf-b659-11f0949b2f7e"
#APIs.GetSummonerInfo(summoner, apikey)

def GetId(json):
    Idlist=[]
    for i in json:
        Idlist.append(i['summonerId'])
    return Idlist

def GetName(json):
    Namelist=[]
    for i in json:
        Namelist.append(i['summonerName'])
    return Namelist

idlist=GetId(APIs.GetChallengerDiv(apikey))
MatchData=[]
#print(idlist)
f = open('test.txt', mode='wt', encoding='utf-8')
for i in idlist:
    time.sleep(0.01)
    print(i)
    for j in APIs.GetMachdata(i, apikey):
        f.write(j['platformId']+" "+str(j['gameId'])+" "+str(j['champion'])+" "+j['role']+" "+j['lane']+"\n")
    



f.close()