from  input import *
from  func import *
import numpy as np




if 1 :# #   param
     nmd="FJSPmodel"
     model = gp.Model(nmd)
     # model.setParam('TimeLimit', 5*60)
     # model.setParam('MIPGap', 0.9)
     # model.Params.LogToConsole = 1
     # model.params.NonConvex = 2
     pass
if 1 :# #  list

            ljobs = get_list(3,'j')
            loperations = get_list(7,'op')
            lmachines = namem
            lj=ljobs
            lo=loperations
            lm=lmachines
            NJ=len(ljobs)
            NO=len(loperations)
            NM=len(lmachines)

            
            
            # loperations_int = [1, 2, 3]
            # ljobs_int = [1, 2, 3, 4, 5, 6, 7]


# P = np.zeros((len(loperations_int) * len(ljobs_int), len(loperations_int) * len(ljobs_int)))

# P[1,1]= 1
# print(P)


def planning(PT,vCijk,vSijk,Xijk):


    plt=[]
    for i in range(len(loperations)):
        for j in range(len(ljobs)):
            for k in range(len(lmachines)):
                jk=3*j+k
                v_xj=Xijk[i][jk]
                if v_xj ==1 :
                    v_pt=PT[i][j][k]
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
        Cijk = model.addVars(loperations,ljobs,lmachines, vtype=gp.GRB.CONTINUOUS, name="Cijk")
        Yijijk = model.addVars(loperations,ljobs,loperations,ljobs,lmachines,vtype=gp.GRB.BINARY, name="Yijijk")
        # Ci = model.addVars(ljobs, vtype=gp.GRB.CONTINUOUS, name="Ci")
        

# print('P shape is', P.shape)    

# for i in range(P.shape[0]):
#     for j in range(P.shape[1]):
#         # access elements in the i-th row and j-th column
#         element = P[i, j]
#         print('P keys is ', element)
        

# for key in Yijijk.keys():
#     print(key)

# dims = len(Yijijk.keys())
# n = len(Yijijk.keys()[0])
# print(dims,n)

# print("Indices of Yijijk: ", Yijij.keys())

if 1 :# #  objective function
                #  cmax
        for i in loperations:
            for j in ljobs:
                # obj=model.setObjective( alpha * (Cmax) + beta * (Xijk[i,j,'H'] * dWj[i,j,'H']), sense=gp.GRB.MINIMIZE) # 
                obj=model.setObjective( gp.quicksum(Yijijk[i,j,ii,jj,k] for k in lm for i in lo for j in lj for ii in lo for jj in lj ), sense=gp.GRB.MINIMIZE) # 

                
if 1 :# #  constraint
            # !   Cmax   ;
        c1 = model.addConstrs(gp.quicksum(Xijk[i,j,k] for k in lmachines) ==1  for i in loperations for j in ljobs ) 
        c2 = model.addConstrs(Xijk[i,j,'Co'] >= Xijk[i,j,'H'] + (Xijk[i,j,'R'] -1) for i in loperations for j in ljobs)
        c3 = model.addConstrs(Xijk[i,j,'R'] + Xijk[i,j,'H'] <= (Xijk[i,j,'Co'] +1) for i in loperations for j in ljobs)
        c4 = model.addConstrs(Xijk[i,j,'Co'] <= Xijk[i,j,'R']  for i in loperations for j in ljobs)
        c5 = model.addConstrs(Xijk[i,j,'Co'] <= Xijk[i,j,'H']  for i in loperations for j in ljobs)

        Cindicator = model.addConstr((Xijk[i,j,'Co']==1) >> (Xijk[i,j,'H']==0))
        Cindicator2 = model.addConstr((Xijk[i,j,'Co']==1) >> (Xijk[i,j,'R']==0))
        Cindicator3 = model.addConstr((Xijk[i,j,'H']==1) >> (Xijk[i,j,'Co']==0))  
        Cindicator4 = model.addConstr((Xijk[i,j,'R']==1) >> (Xijk[i,j,'Co']==0))  
        
        c6 = model.addConstrs(Sijk[i,j,k] +Cijk[i,j,k]<=Xijk[i,j,k]*M for k in lmachines for i in loperations for j in ljobs ) 
        c7 = model.addConstrs(Cijk[i,j,k]>=Sijk[i,j,k]+dPT[i,j,k]-(1-Xijk[i,j,k])*M for k in lmachines for i in loperations for j in ljobs )
        c8 = model.addConstrs(Cmax >= Cijk[i,j,k] for k in lmachines for i in loperations for j in ljobs )
        c9 = model.addConstrs( gp.quicksum(Sijk[i,ljobs[j],k] for k in lmachines) >= gp.quicksum(Cijk[i,ljobs[j-1],k] for k in lmachines) for i in loperations for j in range(1,len(ljobs) ))   

        c10 = model.addConstrs( Sijk[loperations[i],j,k] >= Cijk[loperations[i-1],j,k] for k in lmachines for i in range(1,len(loperations) )for j in ljobs )    
        c11 = model.addConstrs( Sijk[i,j,lmachines[k]] >= Cijk[i,j,lmachines[k]] for k in range(1,len(lmachines) )for i in loperations for j in ljobs )    
        # c12 = model.addConstr((1 ==1 )for jj in range(0,4) )
        c12 = model.addConstrs((Yijijk[lo[i],lj[j],lo[ii],lj[jj],lm[k]] ==1 ) for i in range(NO) for j in range(NJ)for ii in range(i,NO) for jj in range(j,NJ) for k in range(NM))
    
        # c12 = model.addConstrs( Sijk[loperations[i],ljobs[j],k] >= Cijk[loperations[ii],ljobs[jj],k] -(Yijijk[loperations[i],ljobs[j],loperations[ii],ljobs[jj],k])*M for k in lmachines for ii in range(0,len(loperations) ) for jj in range(0,len(ljobs) ) for i in range(0,len(loperations) -1) for j in range(0,len(ljobs) -1) )
        # c13 = model.addConstrs(Sijk[loperations[ii],ljobs[jj],k] >= Cijk[loperations[i],ljobs[j],k] -(1-Yijijk[loperations[i],ljobs[j],loperations[ii],ljobs[jj],k])*M for k in lmachines for ii in range(0,len(loperations) ) for jj in range(0,len(ljobs) ) for i in range(0,len(loperations) -1) for j in range(0,len(ljobs) -1) )
        # c14 = model.addConstrs(Yijijk[i,j,ii,jj] == P[ii,jj] for k in lmachines for ii in range(len(loperations) ) for jj in range(len(ljobs) ) for i in range(len(loperations)) for j in range(len(ljobs)) )


        # for i in range(range(loperations_int)):
        #     for j in range(range(ljobs_int)):
        #         for ii in range(range(loperations_int)):
        #             for jj in range(range(ljobs_int)):
        #                 for k in range(range(lmachines)):
        #                     model.addConstr(Yijijk[i,j,ii,jj,k] == P[i*range(ljobs_int)+j][ii*range(ljobs_int)+jj])
                            
        # for i in range(loperations):
        #     for j in range(ljobs):
        #         for ii in range(loperations):
        #             for jj in range(ljobs):
        #                 for k in range(lmachines):
        #                     model.addConstr(Yijijk[i,j,ii,jj,k] == P[i][j][ii][jj])

        # try:
        #     for i in loperations:
        #         for j in ljobs:
        #             for ii in loperations:
        #                 for jj in ljobs:
        #                     for k in lmachines:
        #                         i_index = loperations.index(i)
        #                         j_index = ljobs.index(j)
        #                         ii_index = loperations.index(ii)
        #                         jj_index = ljobs.index(jj)
        #                         k_index = lmachines.index(k)
        #                         model.addConstr(Yijijk[i,j,ii,jj,k] == P[i_index][j_index][ii_index][jj_index][k_index], name='Equal_Yijijk_P')
        # except IndexError as e:
        #     print(f"IndexError: {e}")
        #     print(f"i_index: {i_index}, j_index: {j_index}, ii_index: {ii_index}, jj_index: {jj_index}, k_index: {k_index}")
        #     print(f"Size of list P: {len(P)}")
                            
        # c10 = model.addConstrs( Yijijk[[i][j][ii][jj][k]] == P for i in ljobs for j in loperations for ii in ljobs for jj in loperations for k in lmachines)

        # cadd = model.addConstrs( Yijijk[[i][j][ii][jj][k]] == Prec.keys() for i in loperations for j in ljobs for ii in range(0,len(loperations)) for jj in range(0,len(ljobs)) for k in lmachines)
        
        # c6 = model.addConstrs( Cmax==0  for j in ljobs) 
        # c7 = model.addConstrs( Xijk[loperations[0],ljobs[0],lmachines[1]]==1  for r in range(1)) 
        # c8 = model.addConstrs( Xijk[loperations[0],ljobs[1],lmachines[2]]==1  for r in range(1)) 

if 1 : #  optimize
    model.optimize()
    vCijk=var2list2d(Cijk,'Cijk')
    Xijk=var2list2d(Xijk,'Xijk')
    vSijk=var2list2d(Sijk,'Sijk') 
    lYijijk = [[key[0],key[1],key[2],key[3],key[4],value.X] for (key, value) in Yijijk.items()]
    s=' '
    for i in range(NO):
        # s=s+'['
        for j in range(NJ):
            # s=s+'['
            for ii in range(NO):
                # s=s+'['
                for jj in range(NJ):
                    s=s+'|'
                    for k in range(NM):
                        s=s+str(int(lYijijk[((NO+2*NJ+NM)*i)+((NO+NJ+NM)*j)+((NJ+NM)*ii)+(NM*jj)+k][5]))+','
                       
                    # s=s+'],'
                # s=s+'],'
            # s=s+'],'
            print(s)
            s=" "
        # s=s+'],'
    
    # Yijijk=var2list2d(Yijijk,'Yijijk')
    
    # print_lis2d(Xijk,'Xijk')
    # print_lis2d(Yijijk,'Yijijk')

    # print_lis3d(vCijk,'Cijk')
    # print_lis3d(vSijk,'Sijk')
    # print_lis3d(Yijijk,'Yijijk')


    # print(Cmax.X)
    
    # planning(PT,vCijk,vSijk,Xijk)

pass