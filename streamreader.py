#!/usr/bin/python
#import ijson
import json
import re
import sys
import itertools
from collections import Counter
countdict={}
topicdict={}
iddict={}









#def checkDaterange(dateStart,dateEnd):











def insertCount(symbol):
 if symbol in countdict:
  countdict[symbol]=countdict[symbol]+1 
 else:
  countdict[symbol]=1
# print "countdict referred

def insertHash(symbol,topic):
  if symbol in topicdict:
   topicdict[symbol].append(topic)
  else:
   topicdict[symbol]=[]
   topicdict[symbol].append(topic)
def dictFill(obj):
 topic=""
 if obj.has_key('symbols'):
  body=obj['body']
  topic=re.findall(r"#[a-zA-Z]{1,10}", body)   
  tickers=obj['symbols']
  for tick in tickers:
   insertCount(tick['symbol'])
   if topic:
    insertHash(tick['symbol'],topic)
 #  insertHash(body)  
 #  if obj.has_key('body'):
#   body=obj['body']
#   topic=re.findall(r"#[a-zA-Z]{1,10}", body)  
#   insertHash(topic)




try:
 dateStart=sys.argv[1]
 dateEnd=sys.argv[2]
except:
  print "Pls enter the date range you want to analyse the data for \n"+"./streamdata.py datestart(in utc format) dateend(utc format)"
  sys.exit()

print dateStart,dateEnd
f=open('data2.json','r')


for object in f:
 obj=json.loads(object)
#checkDateRange()
 dictFill(obj)




#for key,value in countdict.items():
# print key +" " + str(value)
  
for key,value in topicdict.items():
 #print topicdict[key]
 merged=list(itertools.chain(*value))
 print key+": "+ ",".join(merged)
c=Counter(countdict)
print c.most_common(3)
