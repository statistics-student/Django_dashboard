import pymysql
import datetime
import pandas as pd
def amt_last(db):
	date_start=datetime.date.today()
	date_end=str(date_start - datetime.timedelta(days=4))
	date_list=[]
	data_item = {}
	time_list=[]
	for i in range(1,5):
		date_list.append(date_start - datetime.timedelta(days=i))
	for i in range(8,24):
		time_list.append(str(datetime.time(i,0,0)))
	sql="SELECT pay_time,actual_amt FROM app_withdraw_appl WHERE pay_time <'"+str(date_start)+" 00:00:00' AND pay_time >='"+date_end+" 00:00:00'"
	db=pymysql.connect(host="106.14.64.233",user="daiyuanyuan",port=3306,passwd="ar*0J^dawkad",db=db)
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
	return data_item

def amt(db):
    time_list=[]
    amt_list=[]
    now_time=int(datetime.datetime.now().strftime('%H'))
    if now_time==8:
        time_list.append(str(datetime.time(8,0,0)))
    else:
        time_list=[]
        for i in range(8,now_time+1):
            time_list.append(str(datetime.time(i,0,0)))
    db=pymysql.connect(host="106.14.64.233",user="daiyuanyuan",port=3306,passwd="ar*0J^dawkad",db=db )
    sql_total1='select pay_time,actual_amt from app_withdraw_appl where pay_time REGEXP '
    sql_total2=repr(datetime.datetime.now().strftime('%Y-%m-%d'))
    sql_total3=' and pay_time<= '
    sql_total4=repr(datetime.datetime.now().strftime('%Y-%m-%d %H')+':00:00')
    sql_total=sql_total1+sql_total2+sql_total3+sql_total4
    cursor=db.cursor()
    cursor.execute(sql_total)
    data=list(cursor.fetchall())
    data1=pd.DataFrame(data,columns=['时间','放款'])
    data1['放款']=data1['放款'].astype('float')
    for i in time_list:
        amt_list.append(sum(data1.放款[data1.时间<=i]))
    return amt_list