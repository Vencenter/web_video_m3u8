#-*- coding:utf-8 -*-
import urllib2
import re,sys,os
import json
import ssl

reload(sys)
sys.setdefaultencoding("utf-8")
context = ssl._create_unverified_context()

def get_data(url):
    header = {    
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Referer': 'https://qcfem364cngtx9jq66.amitaoapps.com',
        }
    print "get_data!\n"

    try:
        req = urllib2.Request(url, headers = header)
        response = urllib2.urlopen(req,context=context,timeout=20)
        html = json.loads(response.read())
    except:
        req = urllib2.Request(url, headers = header)
        response = urllib2.urlopen(req,context=context,timeout=20)
        html = json.loads(response.read())
    return html
        
def get_content(text):
    print "get_content!\n"
    content=[]
    for li in text["data"]:
        get_id=li['id']
        get_title=li['title']
        get_pic=li['thumb']
        data=[get_id,get_title,get_pic]
        content.append(data)
    return content
def get_m3u8(content,root):
    header = {    
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Referer': 'https://qcfem364cngtx9jq66.amitaoapps.com',
        }
    print ("get_m3u8! %d\n"% len(content))
 
    m3u8=[]
    per=0
    for txt in content:
        base_url="https://qcfem364cngtx9jq66.amitaoapps.com/api/v3/node/detail?id="
        all_url=base_url+str(txt[0])
        
        while True:
            try:
                req = urllib2.Request(all_url, headers = header)
                response = urllib2.urlopen(req,context=context,timeout=5)
                text = json.loads(response.read())
                break
            except:
                print "re_get_data!"
        per+=1
        print all_url+ " percent=" +str((float(per)/len(content))*100)+"%"
        get_title=text["data"]['title']
        get_pic="https://qcfem364cngtx9jq66.amitaoapps.com/"+text["data"]['cover']
        get_url="https://cdn.first0351.com/"+text["data"]["play"][0]["url"]
     
        data=[get_title,get_pic,get_url]
        m3u8.append(data)

        
    return m3u8


    
    
        
        
        
"""try:           
    page=input(u"请输入下载的页面：\n".encode(sys.getfilesystemencoding()))
    num=input(u"请输入该页面显示的数量：\n".encode(sys.getfilesystemencoding()))
except:
    page=input(u"请输入下载的页面：\n")
    num=input(u"请输入该页面显示的数量：\n")
    
"""

def data(page=1,num=2):
    try:  
        page=input(u"请输入下载的页面：\n".encode(sys.getfilesystemencoding()))
        num=input(u"请输入该页面显示的数量：\n".encode(sys.getfilesystemencoding()))
    except:
        page=input(u"请输入下载的页面：\n")
        num=input(u"请输入该页面显示的数量：\n")

    url="https://qcfem364cngtx9jq66.amitaoapps.com/api/v3/node/index?key=&tag_id=&actress_id=&filter=recommend&category_id=550&page="+str(page)+"&user_search_keys=&limit="+str(num)

    root="mitao"
    text=get_data(url)

    content=get_content(text)

    name="mitao/"+str(page)+"_"+str(num)+".m3u8"
    m3u8=get_m3u8(content,name)

    return m3u8

