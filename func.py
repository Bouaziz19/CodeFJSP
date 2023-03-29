import gurobipy as gp
import os
from pprint import pprint
import pandas as pd
import plotly.express as px
import numpy as np
import numpy
from tupledict import TupleDict
from urllib.request import urlopen
import webbrowser

import time


def get_list(Nval=0,st="val"):
    lval = list()
    for i in range(Nval):
        lval.append(st+"_{}".format(i + 1))
    return lval
def get_dic_1d(dval,lval):
    dic_val = dict()
    for i, val in enumerate(dval):
        kval = lval[i]
        dic_val[kval] = val
    return dic_val
def get_dic_2d(dval,lval1,lval2):
    dic_val = dict()
    li=len(lval1)
    lj=len(lval2)
    for i in range(li):
        kval1 = lval1[i]
        for j in range(lj):
            kval2 = lval2[j]
            dic_val[kval1,kval2] = dval[i][j]
    return dic_val
def get_dic_3d(dval,lval1,lval2,lval3):
    dic_val = dict()
    li=len(lval1)
    lj=len(lval2)
    lk=len(lval3)
    print(li)
    print(lj)
    print(lk)

    for i in range(li):
        kval1 = lval1[i]
        for j in range(lj):
            kval2 = lval2[j]
            for k in range(lk):
                kval3 = lval3[k]
                dic_val[kval1,kval2,kval3] = dval[i][j][k]
    return dic_val
def get_dic_4d(dval,lval1,lval2,lval3,lval4):
    dic_val = dict()
    li=len(lval1)
    lj=len(lval2)
    lk=len(lval3)
    ll=len(lval4)
    for i in range(li):
        kval1 = lval1[i]
        for j in range(lj):
            kval2 = lval2[j]
            for k in range(lk):
                kval3 = lval3[k]
                for l in range(ll):
                    kval4 = lval4[l]
                    print(i,' ',j,' ',k,' ',l,' ',)
                    dic_val[kval1,kval2,kval3,kval4] = dval[i][j][k][l]
    return dic_val
def get_dic_5d(dval,lval1,lval2,lval3,lval4,lval5):
    dic_val = dict()
    li=len(lval1)
    lj=len(lval2)
    lk=len(lval3)
    ll=len(lval4)
    lm=len(lval5)
    for i in range(li):
        kval1 = lval1[i]
        for j in range(lj):
            kval2 = lval2[j]
            for k in range(lk):
                kval3 = lval3[k]
                for l in range(ll):
                    kval4 = lval4[l]
                    for m in range(lm):
                        kval5 = lval5[m]
                dic_val[kval1,kval2,kval3,kval4,kval5] = dval[i][j][k][l][m]
    return dic_val
def print_lis2d(l,st=''):
    print('_______      ',st,'      _______')
    for rec in l:
        print(rec)
def print_lis3d(l,st=''):
    print('_______      ',st,'      _______')
    for rec in l:
        print(rec)
def var2list2d(var,st_var):
    l1 = []
    l2 = []
    s=''

    for rec in var.select():
        m=rec.getAttr("VarName").replace(st_var, "").replace("[", "").replace("]", "")
        val=rec.getAttr("x")
        m=m.split(',')
        if s==m[0]:
            l2.append(val)
            
        else:
            if s!='':
                l1.append(l2)

            s=m[0]
            l2=[]
            l2.append(val)
    l1.append(l2)
    return(l1)
def var2list2dint(var,st_var):
    l1 = []
    l2 = []
    s=''

    for rec in var.select():
        m=rec.getAttr("VarName").replace(st_var, "").replace("[", "").replace("]", "")
        val=int(rec.getAttr("x"))
        m=m.split(',')
        if s==m[0]:
            l2.append(val)
            
        else:
            if s!='':
                l1.append(l2)

            s=m[0]
            l2=[]
            l2.append(val)
    l1.append(l2)
    return(l1)
def var2list5d(var,st_var):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    s=''

    for rec in var.select():
        m=rec.getAttr("VarName").replace(st_var, "").replace("[", "").replace("]", "")
        val=rec.getAttr("x")
        m=m.split(',')
        if s==m[0]:
            l2.append(val)
            
        else:
            if s!='':
                l1.append(l2)

            s=m[0]
            l2=[]
            l2.append(val)
    l1.append(l2)
    return(l1)
def var2list3d(var,st_var):
    l0 = []
    l1 = []
    l2 = []

    s0=''
    s=''
    
    for rec in var.select():
        
        m=rec.getAttr("VarName").replace(st_var, "").replace("[", "").replace("]", "")
        val=rec.getAttr("x")
        m=m.split(',')
        print(m)
        if s0==m[0] and s==m[1] :
            l2.append(val)
        else:
            if s!='':
                l1.append(l2)

            s0=m[0]
            s1=m[1]
            l2=[]
            l1=[]
            l2.append(val)
    l1.append(l2)
    return(l1) 
def var2list3dint(var,st_var):
    l0 = []
    l1 = []
    l2 = []

    s0=''
    s=''
    
    for rec in var.select():
        
        m=rec.getAttr("VarName").replace(st_var, "").replace("[", "").replace("]", "")
        val=rec.getAttr("x")
        m=m.split(',')
        print(m)
        if s0==m[0] and s==m[1] :
            l2.append(val)
        else:
            if s!='':
                l1.append(l2)

            s0=m[0]
            s1=m[1]
            l2=[]
            l1=[]
            l2.append(val)
    l1.append(l2)
    return(l1) 

pass