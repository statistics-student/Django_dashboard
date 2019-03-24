from django.shortcuts import render,redirect,HttpResponse
from django.template import RequestContext
from django.http import HttpResponse
from .models import User
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
import json
from . import dataset
import datetime
import time
from . import task

# Create your views here.
def static(data_set,data_now):
    date_y = str(datetime.date.today()-datetime.timedelta(days=1))
    n_len=len(data_now)
    y_num=data_set[date_y]
    s_len=len(list(data_set.values()))
    y_len=len(y_num)
    #当前量
    n_num=data_now[-1]
    #同比
    tb=(n_num-y_num[n_len-1])/y_num[n_len-1]
    #近期总体平均
    t_p=0
    for i in list(data_set.values()):
        t_p=t_p+i[-1]
    total_p=t_p/s_len
    #近期实时平均
    n_p=0
    for i in list(data_set.values()):
        n_p=n_p+i[n_len-1]
    now_p=n_p/(s_len)
    #当前较平均
    n_t_p=(n_num-now_p)/now_p
    #保留几位小数
    tb=round(tb*100,3)
    total_p=round(total_p,3)
    now_p=round(now_p,3)
    n_t_p=round(n_t_p*100,3)
    return [n_num,tb,total_p,now_p,n_t_p]




def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return redirect('login')
    return inner

def login(request):
    # 如果是POST请求，则说明是点击登录按扭 FORM表单跳转到此的，那么就要验证密码，并进行保存session
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username,password=password)
        print(user)
        if user:
            #登录成功
            # 1，生成特殊字符串
            # 2，这个字符串当成key，此key在数据库的session表（在数据库存中一个表名是session的表）中对应一个value
            # 3，在响应中,用cookies保存这个key ,(即向浏览器写一个cookie,此cookies的值即是这个key特殊字符）
            request.session['is_login']='1'  # 这个session是用于后面访问每个页面（即调用每个视图函数时要用到，即判断是否已经登录，用此判断）
            # request.session['username']=username  # 这个要存储的session是用于后面，每个页面上要显示出来，登录状态的用户名用。
            # 说明：如果需要在页面上显示出来的用户信息太多（有时还有积分，姓名，年龄等信息），所以我们可以只用session保存user_id
            request.session['user_id']=user[0].id
            return redirect('mch')
        else:
            password_wrong=True
            return render(request,'login.html',{'password_wrong':password_wrong})
    # 如果是GET请求，就说明是用户刚开始登录，使用URL直接进入登录页面的
    return render(request, 'login.html')

def logout(request):
    del request.session["is_login"]
    return redirect("login")

def home(request):
    return render(request,'home.html')
def base(request):
    return render(request,'base.html')
@check_login
def mch(request):
    user_id1 = request.session.get('user_id')
    userobj = User.objects.filter(id=user_id1)
    print(userobj)
    data_loan_ifm_7=task.ifm_data[2][0]
    data_loan_ifm_today=task.ifm_data[2][1]
    data_amt_ifm_4=task.ifm_data[0][0]
    data_amt_ifm_today=task.ifm_data[0][1]
    data_amt_add_ifm_4=task.ifm_data[1][0]
    data_amt_add_ifm_today=task.ifm_data[1][1]
    data_loan_static=static(task.ifm_data[2][0],task.ifm_data[2][1])
    data_amt_static = static(task.ifm_data[0][0], task.ifm_data[0][1])
    data_amt_add_static = static(task.ifm_data[1][0], task.ifm_data[1][1])
    if userobj:
        return render(request, 'mch.html',
                      {
                          'data_loan_ifm_7': data_loan_ifm_7,
                          'data_loan_ifm_today': data_loan_ifm_today,
                          'data_amt_ifm_4': data_amt_ifm_4,
                          'data_amt_ifm_today': data_amt_ifm_today,
                          'data_amt_add_ifm_4': data_amt_add_ifm_4,
                          'data_amt_add_ifm_today': data_amt_add_ifm_today,
                          'data_loan_static':data_loan_static,
                          'data_amt_static':data_amt_static,
                          'data_amt_add_static':data_amt_add_static,
                          'productname': '莫愁花',
                          'user':userobj[0]
                      })
    else:
        return render(request, 'login.html')
@check_login
def xjs(request):
    user_id1 = request.session.get('user_id')
    userobj = User.objects.filter(id=user_id1)
    print(userobj)
    data_loan_qsh_7=task.qsh_data[2][0]
    data_loan_qsh_today=task.qsh_data[2][1]
    data_amt_qsh_4=task.qsh_data[0][0]
    data_amt_qsh_today=task.qsh_data[0][1]
    data_amt_add_qsh_4=task.qsh_data[1][0]
    data_amt_add_qsh_today=task.qsh_data[1][1]
    data_loan_static = static(task.qsh_data[2][0], task.qsh_data[2][1])
    data_amt_static = static(task.qsh_data[0][0], task.qsh_data[0][1])
    data_amt_add_static = static(task.qsh_data[1][0], task.qsh_data[1][1])
    if userobj:
        return render(request,'xjs.html',
                  {
                      'data_loan_qsh_7':data_loan_qsh_7,
                      'data_loan_qsh_today':data_loan_qsh_today,
                      'data_amt_qsh_4':data_amt_qsh_4,
                      'data_amt_qsh_today':data_amt_qsh_today,
                      'data_amt_add_qsh_4':data_amt_add_qsh_4,
                      'data_amt_add_qsh_today':data_amt_add_qsh_today,
                      'data_loan_static': data_loan_static,
                      'data_amt_static': data_amt_static,
                      'data_amt_add_static': data_amt_add_static,
                      'productname': '现金树',
                      'user': userobj[0]
                  })
    else:
        return render(request, 'login.html')
@check_login
def sxh(request):
    user_id1 = request.session.get('user_id')
    userobj = User.objects.filter(id=user_id1)
    print(userobj)
    data_loan_sxh_7=task.sxh_data[2][0]
    data_loan_sxh_today=task.sxh_data[2][1]
    data_amt_sxh_4=task.sxh_data[0][0]
    data_amt_sxh_today=task.sxh_data[0][1]
    data_amt_add_sxh_4=task.sxh_data[1][0]
    data_amt_add_sxh_today=task.sxh_data[1][1]
    data_loan_static = static(task.sxh_data[2][0], task.sxh_data[2][1])
    data_amt_static = static(task.sxh_data[0][0], task.sxh_data[0][1])
    data_amt_add_static = static(task.sxh_data[1][0], task.sxh_data[1][1])
    if userobj:
        return render(request,'sxh.html',
                  {
                      'data_loan_sxh_7':data_loan_sxh_7,
                      'data_loan_sxh_today':data_loan_sxh_today,
                      'data_amt_sxh_4':data_amt_sxh_4,
                      'data_amt_sxh_today':data_amt_sxh_today,
                      'data_amt_add_sxh_4':data_amt_add_sxh_4,
                      'data_amt_add_sxh_today':data_amt_add_sxh_today,
                      'data_loan_static': data_loan_static,
                      'data_amt_static': data_amt_static,
                      'data_amt_add_static': data_amt_add_static,
                      'productname': '随心花',
                      'user': userobj[0]
                  })
    else:
        return render(request, 'login.html')
@check_login
def tty(request):
    user_id1 = request.session.get('user_id')
    userobj = User.objects.filter(id=user_id1)
    print(userobj)
    data_loan_tty_7=task.tty_data[2][0]
    data_loan_tty_today=task.tty_data[2][1]
    data_amt_tty_4=task.tty_data[0][0]
    data_amt_tty_today=task.tty_data[0][1]
    data_amt_add_tty_4=task.tty_data[1][0]
    data_amt_add_tty_today=task.tty_data[1][1]
    data_loan_static = static(task.tty_data[2][0], task.tty_data[2][1])
    data_amt_static = static(task.tty_data[0][0], task.tty_data[0][1])
    data_amt_add_static = static(task.tty_data[1][0], task.tty_data[1][1])
    if userobj:
        return render(request,'tty.html',
                  {
                      'data_loan_tty_7':data_loan_tty_7,
                      'data_loan_tty_today':data_loan_tty_today,
                      'data_amt_tty_4':data_amt_tty_4,
                      'data_amt_tty_today':data_amt_tty_today,
                      'data_amt_add_tty_4':data_amt_add_tty_4,
                      'data_amt_add_tty_today':data_amt_add_tty_today,
                      'data_loan_static': data_loan_static,
                      'data_amt_static': data_amt_static,
                      'data_amt_add_static': data_amt_add_static,
                      'productname': '一万元',
                      'user': userobj[0]
                  })
    else:
        return render(request, 'login.html')