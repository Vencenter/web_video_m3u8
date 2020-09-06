# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,Context,RequestContext
# Create your views here.
import datetime
import os,random
from models import Member,Mitao
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

pic_root=os.path.dirname(os.path.abspath(__file__))+"/static/pic"

def index(request):
    return HttpResponse("<h1>これは例が一つだよ！<h1>")

def file(request):
    return HttpResponse("<h1>信じられない事はあなたはそんな人ですが、何も言わないで別れよう！！<h1>")

def bing(request):
    template=loader.get_template("bin2.html")

    #*******************1******************************
    #c=Context({})
    #context={"title":"日本語の世界に入ってくだい！","time":datetime.datetime.now()}
    #*******************1******************************

    #*******************2******************************
    #title="日本語の世界に入ってくだい！"
    #time=datetime.datetime.now()
    #context={}
    #*******************2******************************

    pic_root="J:/flod/傳說".decode("utf-8")
    
    root = os.listdir(pic_root)
  
    list_root=[]
    for r in root:
        list_root.append(r)
        
 

    
    data=["相澤南","波多野ゆい","あやみ旬果","小沢まりあ","鈴村愛理","蒼い空","明日花キラ","蒼い空","七海奈々","葵司","天海翼","asuka","......"]
    #data=["相澤","ゆい","あやみ","まりあ","鈴村","遥か","飛鳥","小野泰明", "七海奈々", "葵司","山田","asuka","......"]

    context={"title":"日本語の世界に入ってくだい！","time":datetime.datetime.now(),"person":["傳說",24,"mikami@gmail.com"],"jyoyu":data,"pic":list_root,"num":len(root)}
    request_context = RequestContext(request, context)
    request_context.push(locals())
    html=template.render(context=locals(), request=request)
    return HttpResponse(html)
def fc2(request):
    template=loader.get_template("bin3.html")
    pic_root="J:/flod/pic_image/FC-2/fc2/vedio/"
    root = os.listdir(pic_root)
    list_root=[]
    for r in root:
        list_root.append(r)

    context={"title":"日本語の世界に入ってくだい！","time":datetime.datetime.now(),"person":["Tory",21,"東京"],"pic":list_root,"num":len(list_root)}
    request_context = RequestContext(request, context)
    request_context.push(locals())
    html=template.render(context=locals(), request=request)
    return HttpResponse(html)
def params(request):
    print (0)
    template=loader.get_template("bing.html")
    id=request.GET.get("id")
    name=request.GET.get("name")
    url_data=[id,name]
    context={"url":url_data,"title":"日本語の世界に入ってくだい！","time":datetime.datetime.now(),"person":["三上優弥",24,"mikami@gmail.com"],"jyoyu":url_data}
    request_context = RequestContext(request, context)
    request_context.push(locals())
    html=template.render(context=locals(), request=request)
    return HttpResponse(html)
def params1(request,id,name):
    print (1)
    template=loader.get_template("bing.html")
    url_data=[id,name]
    context={"title":"日本語の世界に入ってくだい！","time":datetime.datetime.now(),"person":["三上優弥",24,"mikami@gmail.com"],"jyoyu":url_data}
    request_context = RequestContext(request, context)
    request_context.push(locals())
    html=template.render(context=locals(), request=request)
    return HttpResponse(html)


def data(request):
    template=loader.get_template("db.html")
    pic_root="J:/flod/傳說".decode("utf-8")
    place_data=["东京","千叶","神户","横滨","大阪","北海道"]
    person_data=["相澤南","波多野ゆい","あやみ旬果","小沢まりあ","鈴村愛理","蒼い空","明日花キラ","蒼い空","七海奈々","葵司","天海翼","asuka","......"]
    root = os.listdir(pic_root)

    
    #增添
    #在数据库表批量加入数据
    #for i in root:
    #member_list.append( [member_data[i],random.randint(10,45),root[i],"2020-09-04","Japan"])
    #db=Member(name=random.choice(person_data),age=random.randint(10,48),address=i,inttime="2020-09-05",area=random.choice(place_data))
    #db.save()
    
    #查找
    #获取数据库表所有信息
    member_list=Member.objects.all()
    #信息排序
    #member_list=Member.objects.all().order_by("age")#升序member_list=Member.objects.order_by("age")
    #member_list=Member.objects.all().order_by("-age")#降序
    #过滤
    #member_list=Member.objects.filter(age = 16)    #age=16
    #member_list=Member.objects.filter(age__gt = 16)#age>16
    #member_list=Member.objects.filter(age__gte 16)#age>=16
    #member_list=Member.objects.filter(name__contains = "张")#筛选姓张的人


    #修改
    #member_data=Member.objects.get(id=1)
    #member_data.age=25
    #member_data.area="中国"
    #member_data.save()

    #删除
    #Member.objects.all().delete()
    #Member.objects.filter(id=1)
    


    
    

    context={"title":"日本語の世界に入ってくだい！","time":datetime.datetime.now(),"member_list":member_list,"num":len(member_list)}
    request_context = RequestContext(request, context)
    request_context.push(locals())
    html=template.render(context=locals(), request=request)
    return HttpResponse(html)

def mitao(request,page=1):
    
    #from mitao import *
    #dlist=data()
    #for li in dlist:
    #db=Mitao(title=li[0].decode("utf-8"),pic=li[1],address=li[2])
    #db.save()
    set_video_num=15

    data_list=[]

    template=loader.get_template("mitao.html")
    all_list=Mitao.objects.all()

    for i in range((page-1)*set_video_num,page*set_video_num):
        data_list.append(all_list[i])

    data_list=[]
    for i in range((page-1)*set_video_num,page*set_video_num):
        data_list.append(all_list[i])

    if(len(data_list)%set_video_num==0):
        pages=len(all_list)/set_video_num
    else:
        pages=len(all_list)/set_video_num + 1



    context={"title":"Player！","time":datetime.datetime.now(),"data":data_list,"num":len(all_list),"pages":pages,"current_page":page,"page_list":list(range(1,pages+1))}
    request_context = RequestContext(request, context)
    request_context.push(locals())
    html=template.render(context=locals(), request=request)
    return HttpResponse(html)

def mitao_pages(request,page=1):
    page=int(page)

    #return HttpResponse(page)
    
    #from mitao import *
    #dlist=data()
    #for li in dlist:
    #db=Mitao(title=li[0].decode("utf-8"),pic=li[1],address=li[2])
    #db.save()
    set_video_num=15

    

    template=loader.get_template("mitao.html")
    all_list=Mitao.objects.all()

    if (page<=0):
        url="http://127.0.0.1:8000/mitao/"
        return HttpResponseRedirect(url)
        #return HttpResponse("<h2 align=\"center\">当前网址错误！<h2>")


    if(len(all_list)<(page-1)*set_video_num+1):
        url="http://127.0.0.1:8000/mitao/"
        return HttpResponseRedirect(url)
        #return HttpResponse("<h2 align=\"center\">当前资源已加载完毕！<h2>")
        

    data_list=[]
    for i in range((page-1)*set_video_num,page*set_video_num):
        data_list.append(all_list[i])

    if(len(data_list)%set_video_num==0):
        pages=len(all_list)/set_video_num
    else:
        pages=len(all_list)/set_video_num + 1

    context={"title":"Player！","time":datetime.datetime.now(),"data":data_list,"num":len(all_list),"pages":pages,"current_page":page,"page_list":list(range(1,pages+1))}
    request_context = RequestContext(request, context)
    request_context.push(locals())
    html=template.render(context=locals(), request=request)
    return HttpResponse(html)
    
    
