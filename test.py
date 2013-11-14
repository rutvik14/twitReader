#!/usr/bin/python

import datetime


str1="2013-01-12"
str2="14111987"
str3="2014-14-11" 
dt1=datetime.datetime.strptime(str1,'%Y-%d-%m')
dt2=datetime.datetime.strptime(str2,'%d%m%Y')
dt3=datetime.datetime.strptime(str3,'%Y-%d-%m') 

print dt2 <= dt1 <=dt3

# (dt2-dt1)
#if x > 0:
#print "yes" 
#print type(x) 
