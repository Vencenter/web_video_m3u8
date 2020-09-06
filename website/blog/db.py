# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from models import Member

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context,RequestContext
# Create your views here.
from django.models import HttpResponse
class db_use(object):
    def __init__(self):
        return True
    def insert_data(self,list=[]):
        if list!=[]:
                member=Member.object.get(id=list[0])
                member.Member_name=list[1]
                member.Member_age=list[2]
                member.Member_address=list[3]
                member.Member_int_time=list[4]
                member.Member_aera=list[5]
                
                
                
