from  input import *
from  func import *
import numpy as np
import pandas as pd



if 1 :# #   param
     nmd="mirna"
     model = gp.Model(nmd)
#      model.setParam("IntegralityFocus",1)
#      model.setParam("IntFeasTol",1e-9)
     # model.setParam('TimeLimit', 5*60)
#      model.setParam('MIPGap', 0.80)
     # model.Params.LogToConsole = 1
     # model.params.NonConvex = 2
#      model.params.InfUnbdInfo=0
      
     pass
if 1 :# #  list
            Ni=len(lsup)
            Nj=len(lDC)
            Nk=len(lret)
            Nl=Ni

            Li=lsup
            Lii=lsup

            Lj=lDC
            Lk=lret
            Ll=lcoal

if 1 :# #  dict
        qik=get_dic_2d(qik,Li,Lk)
        
        dZij=get_dic_2d(Zij,Li,Lj)

if 1 :# #  var
        Xijk = model.addVars( Li,Lj,Lk,vtype=gp.GRB.BINARY, name="Xijk") 
        Yil = model.addVars( Li,Ll, vtype=gp.GRB.BINARY, name="Yil")
        Wij = model.addVars( Li,Lj, vtype=gp.GRB.BINARY, name="Wij")
        ZZij = model.addVars( Li,Lj, vtype=gp.GRB.CONTINUOUS, name="ZZij")
        qij = model.addVars( Li,Lj, vtype=gp.GRB.BINARY, name="qij")
        qjk = model.addVars( Lj,Lk, vtype=gp.GRB.BINARY, name="qjk")
        qpjk = model.addVars( Lj,Lk, vtype=gp.GRB.BINARY, name="qjk")


if 1 :# #  objective function
                obj=model.setObjective( 
                     gp.quicksum(Wij[i,j] for j in Lj for i in Li  )
                    , sense=gp.GRB.MINIMIZE ) # 
                    # , sense=gp.GRB.MAXIMIZE) # 
# 
if 1 :# #  constraint
     c1 = model.addConstrs( Wij[i,j] >= gp.quicksum( Yil[i,l] * Yil[ii,l] * dZij[ii,j]  for ii in Li for l in Ll ) for j in Lj for i in Li ) 
     # c1 = model.addConstrs( Wij[i,j] <= ( Yil[i,l] * Yil[k,l] * dZij[k,j])  for k in Li for l in Ll  for j in Lj for i in Li ) 
     # c1 = model.addConstrs( Yil[i,l] + Yil[ii,l] + dZij[ii,j] -2 <= Wij[i,j]   for ii in Li for l in Ll  for j in Lj for i in Li ) 
     
     c2 = model.addConstrs( 1== gp.quicksum(Yil[i,l]  for l in Ll   )   for i in Li ) 
     c2 = model.addConstrs( 1== Yil["sup1","co1"] for a in range(1) ) 
     c2 = model.addConstrs( 1== Yil["sup2","co1"] for a in range(1) ) 
     c1 = model.addConstrs( Xijk[i,j,k] <= Wij[i,j] for k in Lk  for i in Li for j in Lj ) 
     c1 = model.addConstrs( gp.quicksum(Xijk[i,j,k]  for i in Li for j in Lj  ) ==1 for k in Lk ) 
     c1 = model.addConstrs( gp.quicksum(Xijk[i,j,k] *qik[i,k] for i in Li ) == qjk[j,k] for j in Lj for k in Lk ) 
     c1 = model.addConstrs( gp.quicksum(Xijk[i,j,k] * dZij[i,j] *qik[i,k] for i in Li ) == qpjk[j,k] for j in Lj for k in Lk ) 
     # c1 = model.addConstrs(  qjk[j,k]-qpjk[j,k] for j in Lj for k in Lk ) 

     c1 = model.addConstrs( gp.quicksum(Xijk[i,j,k] *qik[i,k] for k in Lk ) == qij[i,j] for j in Lj  for i in Li) 

if 1 : #  optimize
    model.write("model.lp")
    model.optimize()

if 1:
#     try:
        vXijk=var2list2dint(Xijk,'Xijk')

        s=""
        rec=0
        for xx in vXijk :
          print('------')

          for x in xx:

               if rec == Nk:
                    # print(s)
                    s=" "
                    rec=0
               else:  
                    s=s+' '+ str(x) 
                    rec=rec+1     
     #    vYil=var2list2dint(Yil,'Yil')
     #    print(vYil)
     #    vWij=var2list2dint(Wij,'Wij')
     #    print(vWij)
#     except:
#         pass
# Extract the solution values for decision variables
try:
     l1=[]
     l2=[]

     for v in model.getVars():
          l1.append(v.varName)
          l2.append(v.x)
     solution_df = pd.DataFrame({'Variable': l1, 'Value': l2})

     
except:
          pass
# Export the solution to an Excel file
with pd.ExcelWriter("solution.xlsx") as writer:
    solution_df.to_excel(writer, sheet_name="Solution", index=False)
