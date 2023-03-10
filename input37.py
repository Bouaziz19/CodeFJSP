import numpy as np

M = 10000000
alpha = 0.5
beta = 0.5

dataT= [1 , 1 , 1 , 1 , 1 , 2 , 2 , 2 , 2 , 2 , 2 , 2 , 3 , 3 , 3 , 3 , 3 ]
dataTid= [1 , 2 , 3 , 4 , 5 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 1 , 2 , 3 , 4 , 5]
namej=["j1","j2","j3"]
nameop=["op1","op2","op3","op4","op5","op6","op7",]
namem=["H","R","Co"]

# PT=[#     " j1 "            " j2 "            " j3 " 
#     [[145 , 217, 181],[114 , 171 , 142],[11  , 16  , 13 ]],# "op1"         
#     [[12  , 18 , 15 ],[16  , 24  , 52 ],[20  , 30  , 25 ]],# "op2"       
#     [[14  , 21  , 17 ],[11  , 16  , 13 ],[180 , 270 , 225]],# "op3"       
#     [[11  , 16  , 13 ],[12  , 18  , 15 ],[145 , 271 , 181]],# "op4"      
#     [[130 , 195 , 162],[720 , 1080, 900],[145 , 271 , 181]],# "op5"       
#     [[0   , 0   , 0  ],[10  , 15  , 12 ],[0   , 0   , 0  ]],# "op6"       
#     [[0   , 0   , 0  ],[21  , 31  , 26 ],[0   , 0   , 0  ]] # "op7"
#     ]

# PT=[#     " j1 "            " j2 "            " j3 " 
#     [[1,100,100],[1,100,100],[1,100,100]],# "op1"         
#     [[1,100,100],[1,100,100],[1,100,100]],# "op2"       
#     [[1,100,100],[1,100,100],[1,100,100]],# "op3"       
#     [[1,100,100],[1,100,100],[1,100,100]],# "op4"      
#     [[1,100,100],[1,100,100],[1,100,100]],# "op5"       
#     [[1,100,100],[1,100,100],[1,100,100]],# "op6"       
#     [[1,100,100],[1,100,100],[1,100,100]] # "op7"
#     ]

PT=[#     " j1 "            " j2 "            " j3 " 
    [[1,100,100],[100,1,100],[100,100,1]],# "op1"         
    [[1,100,100],[1,100,100],[100,100,1]],# "op2"       
    [[1,100,100],[100,1,100],[100,100,1]],# "op3"       
    [[1,100,100],[100,1,100],[100,100,1]],# "op4"      
    [[1,100,100],[100,1,100],[100,100,1]],# "op5"       
    [[1,100,100],[100,1,100],[100,100,1]],# "op6"       
    [[1,100,100],[100,1,100],[100,100,1]] # "op7"
    ]


Wj=[ #  " j1 "      " j2 "     " j3 " 
    [[2 , 6 , 4],[6 , 3 , 4],[4 , 6 , 3]],# "op1"         
    [[4 , 4 , 4],[4 , 5 , 3],[4 , 8 , 5]],# "op2"       
    [[3 , 6 , 5],[4 , 6 , 3],[4 , 5 , 5]],# "op3"       
    [[4 , 5 , 3],[2 , 8 , 4],[2 , 6 , 4]],# "op4"      
    [[2 , 6 , 4],[6 , 2 , 4],[2 , 6 , 4]],# "op5"       
    [[0 , 0 , 0],[2 , 6 , 4],[0 , 0 , 0]],# "op6"       
    [[0 , 0 , 0],[4 , 8 , 6],[0 , 0 , 0]],# "op7"
    ]


   #                          j1                                                             j2                                                                   j3                                       
#        j1j2j3 j1j2j3                                                                                                                                                                                                        
   #       op1     op2    op3     op4     op5     op6     op7
P =  [[[[0,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]],      [[0,0,1],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]],  #op1
      [[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]],  #op2
      [[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]],  #op3
      [[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]],  #op4
      [[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]],  #op5
      [[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]],  #op6
      [[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],      [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]]]  #op7
