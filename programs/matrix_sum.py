x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
z=[[x[i][j]+y[i][j] for j in range(len(y)) ] for i in range(len(x))]
print(z)