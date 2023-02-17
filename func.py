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

# def planning(lPTE="",lEPT="",lAPT="" , lACPT="" , lACNPT="" , lDNA="" , lCj="" , lTj="" , lAprf="" , lACWT="" , lATA="" , lExpW="" , liprf="",cmax="",ns=""):
#     plt=[]
#     for m in range(Nws):
#         for j in range(Nprd):
#             if  int(lTj[j])!=0:
#                 color22=str(int(lTj[j]))
#                 Tâches="p"+str(j+1)
#                 Ressource="ws_"+str(m)
#                 D=lCj[j][m]-lEPT[j][m]
#                 v_pt=lEPT[j][m]
#                 F=D+v_pt
#                 plt.append(dict(Tâches=Tâches , Début=D, Fin= F, Ressource=Ressource, Aj=D,Pt=v_pt,Cj=F,color=color22,Time=v_pt))
          
#     for m in range(Nws):
#         v_pt=0
#         s=0
#         for j in range(Nprd):
#             if  int(lTj[j])!=0:
#                 vDNA=int(lDNA[j][m])
#                 Ressource="ws_"+str(m)
#                 if j==0:
#                     dlt=0
#                 else:
#                     dlt=lACPT[m]-lAPT[j-1][m]%lACPT[m]
#                     if dlt ==lACPT[m]:
#                         dlt=0
#                 D=lCj[j][m]-lEPT[j][m]+dlt
#                 v_abs=lACNPT[m]
#                 for ii in range(vDNA):
#                     F=D+v_abs
#                     plt.append(dict(Tâches="abs" , Début=D, Fin= F, Ressource=Ressource, Aj=D,Pt=v_abs,Cj=F,color="abs",Time=v_abs))
#                     D=F+lACPT[m]
    
        
          
#     df = pd.DataFrame(plt)
#     fo=' hjjhjh  '

#     afec=" : "
#     wws=0
#     for recc in lAprf:
#         afec+= ' ws_'+str(wws)+" : "+str(int(recc))
#         wws+=1
#     title="***   ***              Le planning d'mixprodonnancement  <br> "
#     title+="CMAX  = "+str(cmax)+" <br> "
#     title+= afec
#     fig = px.bar(df,base = "Aj",x = "Time",y = "Ressource", text="Tâches",color = "color", orientation = 'h', title=title)
#     fig.update_yaxes(autorange="reversed")
#     ns=ns+".html"
#     fig.write_html(ns)
#     fig.show() 
#     pass



pass