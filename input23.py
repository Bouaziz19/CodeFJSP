import numpy as np

M = 10000000
alpha = 0.5
beta = 0.5

dataT= [1 , 1 , 1 , 2 , 2 , 2]
dataTid= [1 ,2 ,3 ,1 ,2 ,3]
namej=["j1","j2"]
nameop=["op1","op2","op3"]
namem=["H","R","Co"]



PT=[ # " j1 "       " j2 "     
    [[1,100,100],[1,100,100]],# "op1"         
    [[100,1,100],[100,1,100]],# "op2"       
    [[100,100,1],[100,100,1]],# "op3"       
    ]


Wj=[ #  " j1 "      " j2 "   
    [[2 , 6 , 4],[6 , 3 , 4]],# "op1"         
    [[4 , 4 , 4],[4 , 5 , 3]],# "op2"       
    [[3 , 6 , 5],[4 , 6 , 3]],# "op3"       
  
    ]


                                                                                                                                                                                                 
   #     op1   op2  op3             op1  op2   op3   
P =  [[[[0,0],[0,0],[0,0]],      [[0,0],[0,0],[0,0]]],  #op1
      [[[0,0],[0,0],[0,0]],      [[0,0],[0,0],[0,0]]],  #op2
      [[[0,0],[0,0],[0,0]],      [[0,0],[1,1],[0,0]]],  #op3
      ]  
#op3,j1>OP2j1
#op3,j1>OP2j2
#op3,j2>OP1j1
#op3,j2>OP2j1