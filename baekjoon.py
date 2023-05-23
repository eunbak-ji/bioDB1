# A,B=int(input().split())

# if A > B:
#     print(">")
# elif A < B:
#     print("<")
# else:
#     print("==")

# A,B=input().split()
# if int(A) > int(B):
#     print(">")
# elif int(A) < int(B):
#     print("<")
# else:
#     print("==")

# n=int(input(""))
# if 100>=n>=90:
#     print("A")
# elif 89>=n>=80:
#     print("B")
# elif 79>=n>=70:
#     print("C")
# elif 69>=n>=60:
#     print("D")
# else:
#     print("F")

##############################################################################
#완전제곱수_1977
#1 m과n을 input으로
#2 n<x<m의 x 값들 중 완전제곱수 구하기 -> 완전제곱수=i**2=x
#3 x들 중에서 완전 제곱수가 몇개든 최소는 splicing [1],합은 sum 함수 쓰기

# m=int(input(""))
# n=int(input(""))
# sqare_number=[]
# i=1
# while i **2 <=n:
#     if m <= i**2 <=n:
#         sqare_number.append(i**2)
#     i += 1
# if sqare_number==[]:
#     print(-1)
# else:
#     print(sum(sqare_number))
#     print(sqare_number[0])    
    
################################################################################
#손익분기점_1712
#A=임대료+재산세+보험료+급여, B=가변비용 (노트북을 생산하는 데에 드는 비용),C=판매비용
#C*I>A+B*I ~ 손익 분기점(BREAK-EVEN POINT)

# A,B,C=map(int,input("").split())
# if B>=C:
#     print(-1)
# else:
#     print(A//(C-B)+1)

############################################################3
#벌집_2292
#벌집이 1을 중심으로 6개씩 증가한다. 
#벌집이 증가할 수록 이동해야할 칸이 1개씩 증가

# n=int(input())
# bee=1
# c=1
# while n>bee:
#     bee+=c*6
#     c+=1
    
# print(c)

###########################################################
#분수찾기_1193
#분수 지그재그순 1/1-1/2-2/1-3/1-2/2-1/3-1/4-2/3-3/3-... 분수가 위로 아래로,,,,
#
