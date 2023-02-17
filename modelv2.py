from  input23 import *
from  func import *
import numpy as np




if 1 :# #   param
     nmd="FJSPmodel"
     model = gp.Model(nmd)
     model.setParam("IntegralityFocus",1)
     model.setParam("IntFeasTol",1e-9)
     # model.setParam('TimeLimit', 5*60)
    #  model.setParam('MIPGap', 0.90)
     # model.Params.LogToConsole = 1
     # model.params.NonConvex = 2
     pass
if 1 :# #  list
            NJ=len(namej)
            NO=len(nameop)
            NM=len(namem)
            ljobs = get_list(NJ,'j')
            loperations = get_list(NO,'op')
            lmachines = namem
            lj=ljobs
            lo=loperations
            lm=lmachines
            

            def planning(vPTE,vCijk,vSijk,Xijk):


                plt=[]
                for i in range(len(loperations)):
                    for j in range(len(ljobs)):
                        for k in range(len(lmachines)):
                            jk=3*j+k
                            v_xj=Xijk[i][jk]
                            if v_xj ==1 :
                                v_pt=vPTE[i][jk]
                                v_cj=vCijk[i][jk]
                                v_sj=vSijk[i][jk]
                                Tâches='t'+str(loperations[i])+' '+str(ljobs[j])
                                D=v_sj
                                F=v_cj
                                Ressource=lmachines[k]
                                # color22=str(ljobs[j])
                                color22=Tâches

                                plt.append(dict(Tâches=Tâches , Début=D, Fin= F, Ressource=Ressource, Aj=D,Pt=v_pt,Cj=F,color=color22,Time=v_pt))
                df = pd.DataFrame(plt)
                title="***   ***             Le planning d'ordonnancement  <br> "
                fig = px.bar(df,base = "Aj",x = "Time",y = "Ressource", text="Tâches",color = "color", orientation = 'h', title=title)
                fig.update_yaxes(autorange="reversed")
                fig.show() 

if 1 :# #  dict
        dPT=get_dic_3d(PT,loperations,ljobs,lmachines)
        dWj=get_dic_3d(Wj,loperations,ljobs,lmachines)
        dP=get_dic_4d(P,loperations,ljobs,loperations,ljobs)
        pass

if 1 :# #  var
        Cmax = model.addVar(0 , name="Cmax", vtype=gp.GRB.CONTINUOUS)
        # INTEGER
        Xijk =model.addVars(loperations,ljobs,lmachines,vtype=gp.GRB.BINARY, name="Xijk") 
        Sijk = model.addVars( loperations,ljobs,lmachines, vtype=gp.GRB.CONTINUOUS, name="Sijk")
        PTE = model.addVars( loperations,ljobs,lmachines, vtype=gp.GRB.CONTINUOUS, name="PTE")
        Cijk = model.addVars(loperations,ljobs,lmachines, vtype=gp.GRB.CONTINUOUS, name="Cijk")
        Yijijk = model.addVars(loperations,ljobs,loperations,ljobs,lmachines,vtype=gp.GRB.BINARY, name="Yijijk")
        Ci = model.addVars(ljobs, vtype=gp.GRB.CONTINUOUS, name="Ci")
        


if 1 :# #  objective function
                obj=model.setObjective( gp.quicksum(Cijk[i,j,k] for k in lm for i in lo for j in lj  ), sense=gp.GRB.MINIMIZE) # 
                # obj=model.setObjective( alpha * (Cmax) + beta * (Xijk[i,j,'H'] * dWj[i,j,'H']), sense=gp.GRB.MINIMIZE) # 
                # obj=model.setObjective( gp.quicksum(Yijijk[i,j,ii,jj,k] for k in lm for i in lo for j in lj for ii in lo for jj in lj ), sense=gp.GRB.MINIMIZE) # 

                
if 1 :# #  constraint
            # !   Cmax   ;
        c1 = model.addConstrs(gp.quicksum(Xijk[i,j,k] for k in lmachines) >= 1  for i in loperations for j in ljobs ) 
        c12 = model.addConstrs(Xijk[i,j,k] >= Xijk[i,j,"Co"]  for k in lmachines  for i in loperations for j in ljobs ) 
        c13 = model.addConstrs(PTE[i,j,k] == dPT[i,j,k]*(1-Xijk[i,j,"Co"])+dPT[i,j,"Co"]*(Xijk[i,j,"Co"]) for k in lmachines for i in loperations for j in ljobs )
        c14 = model.addConstrs(Sijk[i,j,k] == Sijk[i,j,"Co"]*(Xijk[i,j,"Co"]) +Sijk[i,j,k]*(1-Xijk[i,j,"Co"])  for k in lmachines for i in loperations for j in ljobs ) 
        # c14 = model.addConstrs(Cijk[i,j,k] <= Cijk[i,j,"Co"]*(Xijk[i,j,"Co"]) +(1-Xijk[i,j,"Co"])*M   for k in lmachines for i in loperations for j in ljobs ) 

        c2 = model.addConstrs(Sijk[i,j,k] +Cijk[i,j,k]<=Xijk[i,j,k]*M for k in lmachines for i in loperations for j in ljobs ) 
        c3 = model.addConstrs(Cijk[i,j,k]>=Sijk[i,j,k]+PTE[i,j,k]-(1-Xijk[i,j,k])*M for k in lmachines for i in loperations for j in ljobs )
        # c6 = model.addConstrs(gp.quicksum(Sijk[loperations[i],j,k]  for k in lmachines)  >= gp.quicksum(Cijk[loperations[i-1],j,k]for k in lmachines)   for i in range(1,len(loperations) )for j in ljobs )    
        c8 = model.addConstrs(Cmax >= Cijk[i,j,k] for k in lmachines for i in loperations for j in ljobs )
        c7 = model.addConstrs( Ci[j]>= Cijk[i,j,k] for k in lmachines for i in loperations for j in ljobs)  
        
        c91 = model.addConstrs( Sijk[i,j,k]*Yijijk[i,j,ii,jj,k]+M*(1-Xijk[i,j,k])+ M*(1-Xijk[ii,jj,k])  >=Cijk[ii,jj,k]*Yijijk[i,j,ii,jj,k]  for k in ["H","R","Co"] for ii in loperations for jj in ljobs  for i in loperations for j in ljobs)   
        # c92 = model.addConstrs( Sijk[i,j,"Co"]*Yijijk[i,j,ii,jj,"Co"]+M*(1-Xijk[i,j,"Co"])+ M*(1-Xijk[ii,jj,"Co"]) >=Cijk[ii,jj,"Co"]*Yijijk[i,j,ii,jj,"Co"]for ii in loperations for jj in ljobs  for i in loperations for j in ljobs)   
        # c93 = model.addConstrs( Sijk[i,j,"Co"]*Yijijk[i,j,ii,jj,"Co"] >=Cijk[ii,jj,"R"]*Yijijk[i,j,ii,jj,"Co"] for ii in loperations for jj in ljobs  for i in loperations for j in ljobs)   
        # c94 = model.addConstrs( Sijk[i,j,"Co"]*Yijijk[i,j,ii,jj,"Co"] >=Cijk[ii,jj,"H"]*Yijijk[i,j,ii,jj,"Co"]  for ii in loperations for jj in ljobs  for i in loperations for j in ljobs)   
        
        # c9 = model.addConstrs( Sijk[i,j,k]*Yijijk[i,j,ii,jj,k] >=Cijk[ii,jj,k]*Yijijk[i,j,ii,jj,k]  for k in lmachines for ii in loperations for jj in ljobs  for i in loperations for j in ljobs)   
        
        c11 = model.addConstrs( gp.quicksum(Sijk[i,j,k]for k in lmachines)*dP[i,j,ii,jj] >=gp.quicksum(Cijk[ii,jj,k] for k in lmachines)*dP[i,j,ii,jj]  for ii in loperations for jj in ljobs  for i in loperations for j in ljobs)   


        
        # c9 = model.addConstrs( Sijk[i,j,k]*Yijijk[i,j,ii,jj,k] +(1-Xijk[i,j,k])*M+ M*(1-Xijk[ii,jj,k])>=Cijk[ii,jj,k]*Yijijk[i,j,ii,jj,k]  for k in lmachines for ii in loperations for jj in ljobs  for i in loperations for j in ljobs)   
        # Sijk[i,j,k]*Yijijk[i,j,ii,jj,k]*Xijk[i,j,k]*Xijk[ii,jj,k] >= Cijk[ii,jj,k]*Yijijk[i,j,ii,jj,k]*Xijk[i,j,k]*Xijk[ii,jj,k]

        for vi in range(NO):
            for vj in range(NJ):
                for vii in range(NO):
                    for vjj in range(NJ):
                        for vk in range(NM):
                            i=lo[vi]
                            ii=lo[vii]
                            j=lj[vj]
                            jj=lj[vjj]
                            k=lm[vk]
                            # c4 = model.addConstrs(Sijk[i,j,k]*Yijijk[i,j,ii,jj,k]*Xijk[i,j,k]*Xijk[ii,jj,k] >= Cijk[ii,jj,k]*Yijijk[i,j,ii,jj,k]*Xijk[i,j,k]*Xijk[ii,jj,k]   for ll in range(1) )

                            if vi*NJ+vj<vii*NJ+vjj:
                                c8 = model.addConstrs( Yijijk[i,j,ii,jj,k]+Yijijk[ii,jj,i,j,k] ==1 for ll in range(1)) 
                                # c9 = model.addConstrs(Yijijk[ii,jj,i,j,k] ==1 for ll in range(1))   


                                pass
                                #     i=lo[vi]
                                #     ii=lo[vii]
                                #     j=lj[vj]
                                #     jj=lj[vjj]
                                #     k=lm[vk]
                                # c44 = model.addConstrs( Yijijk[i,j,ii,jj,k]==0 for ll in range(1) )
                                    # c4 = model.addConstrs(Sijk[i,j,k]>= Cijk[ii,jj,k] - (M*(Yijijk[i,j,ii,jj,k]) ) for ll in range(1) )
                                    # c5 = model.addConstrs(Sijk[ii,jj,k]>= Cijk[i,j,k] - (M*(1-Yijijk[i,j,ii,jj,k] )) for ll in range(1) )
                                    # s5*Y54h*X4h*X5h	>=	C4*Y54h*X4h*X5h



if 1 : #  optimize
    model.optimize()
    vCijk=var2list2d(Cijk,'Cijk')    
    Xijk=var2list2d(Xijk,'Xijk')
    vSijk=var2list2d(Sijk,'Sijk')
    vPTE=var2list2d(PTE,'PTE')

    vCi=var2list2d(Ci,'Ci')

    lYijijk = [[key[0],key[1],key[2],key[3],key[4],value.X] for (key, value) in Yijijk.items()]
    # lvYijijk = [int(value.X) for (key, value) in Yijijk.items()]
    lvYijijk = [(value.X) for (key, value) in Yijijk.items()]

    s=' '
    import os

    os.system('cls')
    # print(lvYijijk)
    for i in range(NO):
        # s=s+'['
        for j in range(NJ):
            # s=s+'['
            for ii in range(NO):
                # s=s+'['
                for jj in range(NJ):
                    s=s+'|'
                    # for k in range(NM):
                        # s=s+str(int(lYijijk[((NO*2*NJ*NM)*i)+((NO*NJ*NM)*j)+((NJ*NM)*ii)+(NM*jj)+k][5]))+','
                        # s=s+str(int(lYijijk[((NO*NJ*NJ*NM)*i)+((NO*NJ*NM)*j)+((NJ*NM)*ii)+(NM*jj)+k][5]))
                        # s=s+str(lYijijk[((NO*NJ*NJ*NM)*i)+((NO*NJ*NM)*j)+((NJ*NM)*ii)+(NM*jj)+k][5])
                    s=s+str(int(lYijijk[((NO*NJ*NJ*NM)*i)+((NO*NJ*NM)*j)+((NJ*NM)*ii)+(NM*jj)+0][5]))

                       
                    # s=s+'],'
                # s=s+'],'
            # s=s+'],'
            print(s)
            s=" "
        # s=s+'],'
    
    # Yijijk=var2list2d(Yijijk,'Yijijk')
    
    print_lis2d(Xijk,'Xijk')
    print_lis2d(var2list2d(PTE,'PTE'))

    # print(vCi)

    
    # print_lis2d(Yijijk,'Yijijk')

    # print_lis3d(vCijk,'Cijk')
    # print_lis3d(vSijk,'Sijk')
    # print_lis3d(Yijijk,'Yijijk')


    print(Cmax.X)
    
    planning(vPTE,vCijk,vSijk,Xijk)

pass