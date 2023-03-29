import numpy as np


lsup=["sup1","sup2","sup3","sup4"] # suppliers i  Index 
lDC=["dc1","dc2","dc3","dc4","dc5","dc6","dc7"] # DC j  Index 
lret=["RT1","RT2","RT3","RT4","RT5","RT6","RT7","RT8","RT9","RT10","RT11","RT12"] # retailer k  Index 

lcoal=["co1","co2","co3","co4"] # coalition l  Index 
M =999999
# qki Demand of retailer k from supplier i
qik=[      
    [10,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    ]
Zij=[
[1,0,0,0,1,1,0],
[0,1,0,0,0,0,1],
[0,0,1,0,0,0,0],
[0,0,0,1,0,0,0],
 ]












# Uij 1 if DC j is operated by supplier i
# Yik 1 if retailer k is a customer of supplier i
# Rij Number of trucks sent from supplier i to DC j
# Vkj Number of vehicles sent from DC j to retailer k
# Cij Renting cost for unit space at DC j paid by i
# F Rj Fixed cost associated with renting space at DC j
# V Cjk Cost paid to i for using fleet of its DC j
# T Ci Total cost per supplier operating as singleton
# T Ci(S) Total cost per supplier in coalition S
# Mij proportion of DC’s j capacity rented by i


# Cap(i) Capacity of supplier
# Cap(j) Capacity of DC
# Capt Fixed capacity of truck
# Capv Fixed capacity of vehicle
# λij Distance separating supplier i from DC j
# λjk Distance separating DC j from retailer k
# aij Transshipment cost per unit for a DC j
# ft0 Fixed cost per truck
# ft1 Fixed unit cost per distance for truck
# fv0 Fixed cost per vehicle
# fv1 Fixed unit cost per distance for vehicle













# N Set of suppliers (firms)
# J Set of DCs
# K Set of retailers
# O Set of objective functions
# i ∈ N Index of each supplier
# j ∈ J Index of each DC
# k ∈ K Index of each retailer
# o ∈ O Index of each objective function
# S A coalition of suppliers i
# NS Set of suppliers in a coalition S
# JS Set of DCs in a coalition S
# KS Set of retailers in a coalition S
# J(i) Set of DCs operated by i in a coalition S
# qki Demand of retailer k from supplier i
# aij Transshipment cost per unit for a DC j
# ft0 Fixed cost per truck
# ft1 Fixed unit cost per distance for truck
# fv0 Fixed cost per vehicle
# fv1 Fixed unit cost per distance for vehicle
# λij Distance separating supplier i from DC j
# λjk Distance separating DC j from retailer k
# Cap(i) Capacity of supplier
# Cap(j) Capacity of DC
# Capt Fixed capacity of truck
# Capv Fixed capacity of vehicle
# Uij 1 if DC j is operated by supplier i
# Yik 1 if retailer k is a customer of supplier i
# Rij Number of trucks sent from supplier i to DC j
# Vkj Number of vehicles sent from DC j to retailer k
# Cij Renting cost for unit space at DC j paid by i
# F Rj Fixed cost associated with renting space at DC j
# V Cjk Cost paid to i for using fleet of its DC j
# T Ci Total cost per supplier operating as singleton
# T Ci(S) Total cost per supplier in coalition S
# Mij proportion of DC’s j capacity rented by i
# Xij Quantity of product sent from supplier i to DC j
# Wijk 1 if retailer k assigned to DC j ∈ i, 0 otherwise
