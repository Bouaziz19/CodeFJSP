P =  [
    [[[0,0,1,1,0,0,0],[1,1,1,1,1,0,1],[1,1,1,1,1,0,0]],
     [[0,0,1,1,0,0,0],[1,1,1,1,1,0,1],[1,1,1,1,1,0,0]],
     [[0,0,0,1,0,0,0],[1,1,1,0,1,1,1],[1,1,1,1,1,0,0]],
     [[0,0,0,0,0,0,0],[1,1,1,0,1,0,1],[1,1,1,1,1,0,0]],
     [[0,0,1,1,0,0,0],[1,1,1,1,1,0,1],[1,1,1,1,1,0,0]],
     [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],
     [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],],
    [[[0,0,0,0,0,0,0],[0,1,1,0,1,0,0],[1,1,1,1,1,0,0]],
     [[0,0,0,0,0,0,0],[0,0,1,0,1,0,0],[1,1,1,1,1,0,0]],

     [[0,0,0,0,0,0,0],[0,0,0,0,1,1,0],
     [1,1,1,1,1,0,0]],

     [[0,0,0,1,0,0,0],[1,1,1,0,1,0,1],[1,1,1,1,1,0,0]],
     [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,1,1,1,0,0]],
     [[0,0,1,1,0,0,0],[1,1,1,1,1,0,1],[1,1,1,1,1,0,0]],
     [[0,0,0,0,0,0,0],[0,1,1,0,1,0,0],[1,1,1,1,1,0,0]],],
    [[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,1,1,0,0]],
     [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,1,1,0,0]],
     [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0]],
     [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],
     [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,0]],
     [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],
     [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]]]
s=''
for j in range(7):
    s=s+'['
    for i in range(3):
        s=s+'['
        for l in range(7):
            s=s+'['
            for k in range(3):
                s=s+str(P[k][l][i][j])+','
            s=s+'],'
        s=s+'],'
    s=s+'],'
print(s)
   