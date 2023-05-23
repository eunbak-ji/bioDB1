print('3-1')
num={'ESTJ' : '010-1234-5678' , 'INFJ' : '010-3456-7654', 'ENFP' : '010-3535-7575'}
print (num)
print('--------------------------------------')
print('3-2')
print(num['ESTJ'][4:8])
print(num['ESTJ'][9:13])
print('--------------------------------------')
print('3-3')
a=int(num['ESTJ'][4:8])
b=int(num['ESTJ'][9:13])
print(a+b)
print('----------------------------------------')
print('3-4')
list=['010-1234-5678', '010-3456-7654', '010-3535-7575' ]
print(list[0])
list_1=[ num['ESTJ'], num['INFJ'], num['ENFP'] ]
print(list_1)
print(list_1[0])       
