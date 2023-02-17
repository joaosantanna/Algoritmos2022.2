#F = 1,1 ,2,3,5,8,13,21

print('F = 1,1',end=',')
contador = 2
T1 = 1
T2 = 1
while contador < 20 :
    T3 = T1 + T2
    print(T3,end=',')
    T1,T2 = T2,T3
    contador += 1

