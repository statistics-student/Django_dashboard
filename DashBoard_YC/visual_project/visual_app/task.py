from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
import datetime
import time
import pymysql
import pandas as pd

ifm_data=[[None,None],[None,None],[None,None]]
sxh_data=[[None,None],[None,None],[None,None]]
qsh_data=[[None,None],[None,None],[None,None]]
tty_data=[[None,None],[None,None],[None,None]]
'''
try:
    scheduler=BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(),'default')
    @register_job(scheduler,'interval',seconds=20)
    def test_job1():
        data.append(str(datetime.datetime.now()))
        print(len(data))
    register_events(scheduler)
    scheduler.start()
except Exception as e:
    print(e)
    scheduler.shutdown()
'''

#过去四天总体放款
def amt_last(db,dataset):
	date_start=datetime.date.today()
	date_end=str(date_start - datetime.timedelta(days=4))
	date_list=[]
	data_item = {}
	time_list=[]
	for i in range(1,5):
		date_list.append(date_start - datetime.timedelta(days=i))
	for i in range(8,24):
		for j in [0,15,30,45]:
			time_list.append(str(datetime.time(i,j,0)))
	sql="SELECT pay_time,actual_amt FROM app_withdraw_appl WHERE pay_time <'"+str(date_start)+" 00:00:00' AND pay_time >='"+date_end+" 00:00:00'"
	db=pymysql.connect(host="106.14.64.233",user="zhanglei",port=3306,passwd="2ISpoe3F!o8P",db=db)
	cursor=db.cursor()
	cursor.execute(sql)
	data=list(cursor.fetchall())
	data1=pd.DataFrame(data,columns=['时间','放款'])
	data1['放款']=data1['放款'].astype('float')
	for i in date_list:
		data_everyday=[]
		time_start=datetime.datetime.strptime(str(i)+' 00:00:00','%Y-%m-%d %H:%M:%S')
		start_to_end=i+datetime.timedelta(days=1)
		time_end=datetime.datetime.strptime(str(start_to_end)+' 00:00:00','%Y-%m-%d %H:%M:%S')
		data2=data1[data1.时间>=time_start][data1.时间<time_end]
		for j in time_list:
			j=datetime.datetime.strptime(str(i)+' '+j,'%Y-%m-%d %H:%M:%S')
			data_everyday.append(sum(data2.放款[data2.时间<=j]))
		data_item[str(i)]=data_everyday
	dataset[0][0]=data_item
#当天总体放款
def amt(db,dataset):
    time_list=[]
    amt_list=[]
    hour_list=[]
    minute_list=[]
    now_hour=int(datetime.datetime.now().strftime('%H'))
    now_minute=int(datetime.datetime.now().strftime('%M'))
    if now_hour==8:
        hour_list.append(8)
        if 0<=now_minute<15:
            minute_list.append(0)
        elif 15<=now_minute<30:
            minute_list.append(0)
            minute_list.append(15)
        elif 30<=now_minute<45:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
        elif 45<=now_minute<60:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
            minute_list.append(45)
        for i in hour_list:
            for j in minute_list:
                time_list.append(str(datetime.time(i,j,0)))
    elif now_hour>8:
        for i in range(8,now_hour):
            for j in [0,15,30,45]:
                time_list.append(str(datetime.time(i,j,0)))
        hour_list.append(now_hour)
        if 0<=now_minute<15:
            minute_list.append(0)
        elif 15<=now_minute<30:
            minute_list.append(0)
            minute_list.append(15)
        elif 30<=now_minute<45:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
        elif 45<=now_minute<60:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
            minute_list.append(45)
        for i in hour_list:
            for j in minute_list:
                time_list.append(str(datetime.time(i,j,0)))
    db=pymysql.connect(host="106.14.64.233",user="zhanglei",port=3306,passwd="2ISpoe3F!o8P",db=db)
    sql_total1='select pay_time,actual_amt from app_withdraw_appl where pay_time REGEXP '
    sql_total2=repr(datetime.datetime.now().strftime('%Y-%m-%d'))
    sql_total3=' and pay_time<= '
    sql_total4=repr(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sql_total=sql_total1+sql_total2+sql_total3+sql_total4
    cursor=db.cursor()
    cursor.execute(sql_total)
    data=list(cursor.fetchall())
    data1=pd.DataFrame(data,columns=['时间','放款'])
    data1['放款']=data1['放款'].astype('float')
    for i in time_list:
        amt_list.append(sum(data1.放款[data1.时间<=i]))
    dataset[0][1] = amt_list

#过去四天新增
def amt_last_add(db,dataset):
	date_start=datetime.date.today()
	date_end=str(date_start - datetime.timedelta(days=4))
	date_list=[]
	data_item = {}
	time_list=[]
	for i in range(1,5):
		date_list.append(date_start - datetime.timedelta(days=i))
	for i in range(8,24):
		for j in [0,15,30,45]:
			time_list.append(str(datetime.time(i,j,0)))
	sql="SELECT e.c,e.d FROM (SELECT t.appr_id a,MIN(t1.id) b,t.pay_time c,\
	t.actual_amt d FROM app_withdraw_appl t JOIN app_repay_plan t1 ON t1.withdraw_id \
	= t.id WHERE t.pay_time >= '2017-12-25' GROUP BY t.appr_id) e WHERE e.c>='"+date_end+\
	" 00:00:00' and e.c < '"+str(date_start)+" 00:00:00'"
	db=pymysql.connect(host="106.14.64.233",user="zhanglei",port=3306,passwd="2ISpoe3F!o8P",db=db)
	cursor=db.cursor()
	cursor.execute(sql)
	data=list(cursor.fetchall())
	data1=pd.DataFrame(data,columns=['时间','放款'])
	data1['放款']=data1['放款'].astype('float')
	for i in date_list:
		data_everyday=[]
		time_start=datetime.datetime.strptime(str(i)+' 00:00:00','%Y-%m-%d %H:%M:%S')
		start_to_end=i+datetime.timedelta(days=1)
		time_end=datetime.datetime.strptime(str(start_to_end)+' 00:00:00','%Y-%m-%d %H:%M:%S')
		data2=data1[data1.时间>=time_start][data1.时间<time_end]
		for j in time_list:
			j=datetime.datetime.strptime(str(i)+' '+j,'%Y-%m-%d %H:%M:%S')
			data_everyday.append(sum(data2.放款[data2.时间<=j]))
		data_item[str(i)]=data_everyday
	dataset[1][0]=data_item
#当天新增
def amt_add(db,dataset):
    time_list=[]
    amt_list=[]
    hour_list=[]
    minute_list=[]
    now_hour=int(datetime.datetime.now().strftime('%H'))
    now_minute=int(datetime.datetime.now().strftime('%M'))
    if now_hour==8:
        hour_list.append(8)
        if 0<=now_minute<15:
            minute_list.append(0)
        elif 15<=now_minute<30:
            minute_list.append(0)
            minute_list.append(15)
        elif 30<=now_minute<45:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
        elif 45<=now_minute<60:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
            minute_list.append(45)
        for i in hour_list:
            for j in minute_list:
                time_list.append(str(datetime.time(i,j,0)))
    elif now_hour>8:
        for i in range(8,now_hour):
            for j in [0,15,30,45]:
                time_list.append(str(datetime.time(i,j,0)))
        hour_list.append(now_hour)
        if 0<=now_minute<15:
            minute_list.append(0)
        elif 15<=now_minute<30:
            minute_list.append(0)
            minute_list.append(15)
        elif 30<=now_minute<45:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
        elif 45<=now_minute<60:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
            minute_list.append(45)
        for i in hour_list:
            for j in minute_list:
                time_list.append(str(datetime.time(i,j,0)))
    db=pymysql.connect(host="106.14.64.233",user="zhanglei",port=3306,passwd="2ISpoe3F!o8P",db=db)
    date_start=datetime.date.today()
    date_now=repr(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sql="SELECT e.c,e.d FROM (SELECT t.appr_id a,MIN(t1.id) b,t.pay_time c,\
    t.actual_amt d FROM app_withdraw_appl t JOIN app_repay_plan t1 ON t1.withdraw_id \
    = t.id WHERE t.pay_time >= '2017-12-25' GROUP BY t.appr_id) e WHERE e.c>='"+str(date_start)+\
    " 00:00:00' and e.c < "+date_now
    cursor=db.cursor()
    cursor.execute(sql)
    data=list(cursor.fetchall())
    data1=pd.DataFrame(data,columns=['时间','放款'])
    data1['放款']=data1['放款'].astype('float')
    for i in time_list:
        amt_list.append(sum(data1.放款[data1.时间<=i]))
    dataset[1][1] = amt_list
#过去七天注册量
def loan_last(db,dataset):
	date_start=datetime.date.today()
	date_end=str(date_start - datetime.timedelta(days=7))
	date_list=[]
	data_item = {}
	time_list=[]
	for i in range(1,8):
		date_list.append(date_start - datetime.timedelta(days=i))
	for i in range(0,24):
		for j in [0,15,30,45]:
			time_list.append(str(datetime.time(i,j,0)))
	time_list.append('23:59:59')
	sql="SELECT create_date FROM app_loan_appl WHERE create_date >='"+date_end+" 00:00:00' AND create_date <"+repr(str(date_start))
	db=pymysql.connect(host="106.14.64.233",user="zhanglei",port=3306,passwd="2ISpoe3F!o8P",db=db)
	cursor=db.cursor()
	cursor.execute(sql)
	data=list(cursor.fetchall())
	data1=pd.DataFrame(data,columns=['时间'])
	for i in date_list:
		data_everyday=[]
		time_start=datetime.datetime.strptime(str(i)+' 00:00:00','%Y-%m-%d %H:%M:%S')
		start_to_end=i+datetime.timedelta(days=1)
		time_end=datetime.datetime.strptime(str(start_to_end)+' 00:00:00','%Y-%m-%d %H:%M:%S')
		data2=data1[data1.时间>=time_start][data1.时间<time_end]
		for j in time_list:
			j=datetime.datetime.strptime(str(i)+' '+j,'%Y-%m-%d %H:%M:%S')
			data_everyday.append(len(data2[data2.时间<=j]))
		data_item[str(i)]=data_everyday
	dataset[2][0]=data_item

#当天注册量
def loan_today(db,dataset):
    time_list=[]
    amt_list=[]
    hour_list=[]
    minute_list=[]
    now_hour=int(datetime.datetime.now().strftime('%H'))
    now_minute=int(datetime.datetime.now().strftime('%M'))
    if now_hour==0:
        hour_list.append(0)
        if 0<=now_minute<15:
            minute_list.append(0)
        elif 15<=now_minute<30:
            minute_list.append(0)
            minute_list.append(15)
        elif 30<=now_minute<45:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
        elif 45<=now_minute<60:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
            minute_list.append(45)
        for i in hour_list:
            for j in minute_list:
                time_list.append(str(datetime.time(i,j,0)))
    elif now_hour>0:
        for i in range(0,now_hour):
            for j in [0,15,30,45]:
                time_list.append(str(datetime.time(i,j,0)))
        hour_list.append(now_hour)
        if 0<=now_minute<15:
            minute_list.append(0)
        elif 15<=now_minute<30:
            minute_list.append(0)
            minute_list.append(15)
        elif 30<=now_minute<45:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
        elif 45<=now_minute<60:
            minute_list.append(0)
            minute_list.append(15)
            minute_list.append(30)
            minute_list.append(45)
        for i in hour_list:
            for j in minute_list:
                time_list.append(str(datetime.time(i,j,0)))
    db=pymysql.connect(host="106.14.64.233",user="zhanglei",port=3306,passwd="2ISpoe3F!o8P",db=db)
    date_start=datetime.date.today()
    date_now=repr(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sql="SELECT create_date FROM app_loan_appl WHERE create_date >='"+str(date_start)+" 00:00:00' AND create_date <="+date_now
    cursor=db.cursor()
    cursor.execute(sql)
    data=list(cursor.fetchall())
    data1=pd.DataFrame(data,columns=['时间'])
    for i in time_list:
        amt_list.append(len(data1[data1.时间<=i]))
    dataset[2][1] = amt_list


try:
    scheduler=BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(),'default')
    @register_job(scheduler,'interval',minutes=3,next_run_time=datetime.datetime.now())
    def do_someting():
        start1=time.time()
        #总体放款
        amt('qsh', qsh_data)
        amt('sxh', sxh_data)
        amt('tty', tty_data)
        amt('ifm', ifm_data)
        amt_last('qsh', qsh_data)
        amt_last('sxh', sxh_data)
        amt_last('tty', tty_data)
        amt_last('ifm',ifm_data)
        start2=time.time()
        #新增放款
        amt_add('qsh', qsh_data)
        amt_add('sxh', sxh_data)
        amt_add('tty', tty_data)
        amt_add('ifm', ifm_data)
        amt_last_add('qsh', qsh_data)
        amt_last_add('sxh', sxh_data)
        amt_last_add('tty', tty_data)
        amt_last_add('ifm', ifm_data)
        start3=time.time()
        #注册量
        loan_today('qsh', qsh_data)
        loan_today('sxh', sxh_data)
        loan_today('tty', tty_data)
        loan_today('ifm', ifm_data)
        loan_last('qsh', qsh_data)
        loan_last('sxh', sxh_data)
        loan_last('tty', tty_data)
        loan_last('ifm', ifm_data)
        print(str(datetime.datetime.now()))
        end=time.time()
        print(end-start3)
        print(end-start2)
        print(end-start1)
    register_events(scheduler)
    scheduler.start()
except Exception as e:
    print(e)
    scheduler.shutdown()