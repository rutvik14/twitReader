#!/usr/bin/python

import json
import re
import sys
import itertools
import datetime
from collections import Counter
from collections import namedtuple


class DayAnalysis:
 def __init__(self, datestr):
  self.countDict={}
  self.topicDict={}
  self.idDict={}
  self.trendDict={}  
  self.date=datestr

 def appendToCountDict(key,value):
  return True 

 def appendToTopicDict(self,key,value):
  self.topicDict[key].append(value)
 def appendToTrendDict(key,value):
  return True
 


def checkDateRange(createDate,dateStart,dateEnd,dayChosen):
 date=createDate.split('T')[0]
 chosen=datetime.datetime.strptime(dayChosen,'%Y%m%d')
 start=datetime.datetime.strptime(dateStart,'%m%d%Y')
 date1=datetime.datetime.strptime(date,'%Y-%m-%d')
 end=datetime.datetime.strptime(dateEnd,'%m%d%Y')  
 if not (start <= chosen <= end):
  sys.exit("Pls enter a valid date wrt start and end date.")
 if (start <= date1 <= end):
  return True
 else:
  return False 

def dateFormatter(createDate):
 dayDate=createDate.split('T')[0]
 dayDate=datetime.datetime.strptime(dayDate,'%Y-%m-%d').strftime('%Y%m%d')
 return dayDate

def insertHash(symbol,topic,classObj):
 if symbol in classObj.topicDict:
  classObj.appendToTopicDict(symbol,topic)
 # classObj.topicDict[symbol].append(topic)
 else:
  classObj.topicDict[symbol]=[] 
  classObj.appendToTopicDict(symbol,topic)
 # classObj.topicDict[symbol].append(topic)
  
def insertCount(symbol,trend,classObj):
 if symbol in classObj.countDict:
    classObj.countDict[symbol]=classObj.countDict[symbol]+1
    classObj.trendDict[symbol]=trend
 else:
    classObj.countDict[symbol]=1
    classObj.trendDict[symbol]=trend
 
def dictFill(obj,classObj):
 body=obj['body']
 topic=re.findall(r"#[a-zA-Z]{1,10}",body.lower())
 
 if obj.has_key('symbols'):
  tickers=obj['symbols']
  for tick in tickers:
   symbol=tick['symbol']
   trend=tick['trending']
   insertCount(symbol,trend,classObj) 
   if topic:
    insertHash(symbol,topic,classObj)
      




try:
 dateStart=sys.argv[1]
 dateEnd=sys.argv[2]
 dayChosen=sys.argv[3]
except:
  print "Pls enter the date range you want to analyse the data for \n"+"./streamdata.py datestart(eg: mmddyyyy) dateend(mmddyyyy)"
  sys.exit()
 

print dateStart,dateEnd,dayChosen

mappingDict={}

f=open("data2.json",'r')

for jsonobject in f:
 obj=json.loads(jsonobject)
 #print type(obj)

# print trend
 createDate=obj['created_at'] 
 x=checkDateRange(createDate,dateStart,dateEnd,dayChosen)
 if x:
  dayDate=dateFormatter(createDate)
  if not mappingDict.has_key(dayDate):
   mappingDict[dayDate]=DayAnalysis(dayDate)
   print mappingDict[dayDate].date
   dictFill(obj,mappingDict[dayDate])
  else:
   dictFill(obj,mappingDict[dayDate])
 
  
 

for key,value in mappingDict['20131008'].topicDict.items():
 merged=list(itertools.chain(*value))
 merged=set(merged)
 print key+": "+ " ".join(merged)

for key,value in mappingDict.items():
 print value.trendDict['BBRY']


c=Counter(mappingDict[str(dayChosen)].countDict)
print "the most popular stocks for the chosen time period on this day:"+dayChosen
print c.most_common(3)
#for key,value in mappingDict:
# print key,value


for key,value in mappingDict.items():
 c1=Counter(value.countDict)
 print c1.most_common(3)
  
 
