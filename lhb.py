 # -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:13:27 2016
@author:半个板渣
龙虎争霸选股器 资金+机构 V1.0
""" 
import csv,time,os,sys,getopt
type = sys.getfilesystemencoding()
import tushare as ts
from io import open
reload(sys)    
sys.setdefaultencoding('utf8')

#print("远端服务器选股处理中，请稍等.")
#print("远端服务器选股处理中，请稍等..")
#print("远端服务器选股处理中，请稍等...")

def lhb_zj(day):  #龙虎榜5日内最强资金 获取近5、10、30、60日个股上榜统计数据,包括上榜次数、累积购买额、累积卖出额、净额、买入席位数和卖出席位数。
    csvpath = ".资金.csv"
    a = ts.cap_tops(day)
    data=a[:day]
    data.to_csv(csvpath,columns=['code','name','net','bamount','samount','bcount','scount'])
    print("\n"+"  龙虎榜5日内最强资金"+"\n")
    with open(csvpath,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            code=row.get("code")
            name=row.get("name")
            net=row.get("net")
            #print name.decode('utf-8').encode(type)
            print code,("%11s"%(name)),net
    file.close()


def lhb_jg(day):   #龙虎榜day日内最强机构 获取机构近5、10、30、60日累积买卖次数和金额等情况。
    csvpath = ".机构.csv"
    a = ts.inst_tops(day)
    data=a[:day]
    data.to_csv(csvpath,columns=['code','name','net','bamount','samount','bcount','scount'])

    print("\n"+"  龙虎榜5日内最强机构"+"\n")
    with open(csvpath,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            code=row.get("code")
            name=row.get("name")
            net=row.get("net")
            #print(code,name,net).decode('utf-8').encode(type)
            print code,("%11s"%(name)),net

    file.close()

def lhb_yyb(day):     #获取营业部近5、10、30、60日上榜次数、累积买卖等情况。
    csvpath = ".营业部.csv"
    data = ts.broker_tops(day) 
    data.to_csv(csvpath,columns=['broker','count','bamount','bcount','samount','scount','top3'])

    print("\n"+"龙虎榜5日内最强机构"+"\n")
    with open(csvpath,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            broker=row.get("broker")
            count=row.get("count")
            bamount=row.get("bamount")
            bcount=row.get("bcount")
            samount=row.get("samount")
            scount=row.get("scount")
            top3=row.get("top3")		
            print broker,bamount,bcount,samount,scount,top3
			
    file.close()

def lhb_day():     #按日期获取历史当日上榜的个股数据，如果一个股票有多个上榜原因，则会出现该股票多条数据。
    csvpath = ".每日龙虎榜.csv"
    data = ts.broker_tops()
    data.to_csv(csvpath,columns=['code','name','pchange','amount','buy','bratio','sell','sratio','reason','date'])

    print("\n"+"龙虎榜5日内最强机构"+"\n")
    with open(csvpath,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            code=row.get("code")
            name=row.get("name")
            pchange=row.get("pchange")
            bcamountount=row.get("amount")
            samount=row.get("samount")
            buy=row.get("buy")
            bratio=row.get("bratio")
            sell=row.get("sell")
            sratio=row.get("sratio")
            reason=row.get("reason")
            date=row.get("date")		
            print code,name,bcount,buy,sell,reason
			 
    file.close()
def time_out():
	flage=int(time.strftime("%Y%m%d", time.localtime()))
	if flage > 20171125:
		print("_SYSERROR_：服务器端口已更换，请重新匹配端口"+"\n")
		quit()

def usage():
    print("半个板渣-龙虎榜数据查询"+"\n")

opts, args = getopt.getopt(sys.argv[1:], "hz,j,y,d,h",["help","zj","jg","yyb","day"])

for op,value in opts:
	if op in ("-z","-zj"):
		lhb_zj(5) #最强资金
		sys.exit()
	elif op in ("-j","--jg"):
		lhb_jg(5) #最强机构
		sys.exit()
	elif op in ("-y","--yyb"):
		lhb_yyb(5)#营业部
		sys.exit()
	elif op in ("-d","--day"):
		lhb_day() #每日龙虎榜
		sys.exit()
	elif op in ("-h","--help"):
		usage()
		sys.exit()

lhb_zj(5) #最强资金
lhb_jg(5) #最强机构

