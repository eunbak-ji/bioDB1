# counting DNA nucleotides
# A,T,G,C의 갯수 구하기
# 1. INPUT에 염기서열 넣기
# 2. 만약 INPUT 안에 A(T,G,C)가 있다면 갯수를 세라
# 3. 갯수를 셀 떄마다 리스트 안에 저장 
# 4.OUTPUT으로 리스트가 나오게 설정한다.

nucleotide=input("")
count_N=[]
if A in nucleotide:
    CA=nucleotide.count("A")
    count_N+=CA
elif T in nucleotide:
    CT=nucleotide.count("T")
    count_N+=CT
elif G in nucleotide:
    CG=nucleotide.count("G")
    count_N+=CG    
elif C in nucleotide:
    CC=nucleotide.count("C")
    count_N+=CC
print(count_N)    

sequence=input("")
A=0
T=0
G=0
C=0

for nt in sequence:
    if "A" in nt:
        A+=1
    elif "T" in nt:
        T+=1
    elif "G" in nt:
        G+=1            
    else:
        C+=1
print(A,C,G,T) 


# Transcribing DNA into RNA
# dna를 rna식으로 바꾸기
# input으로 rna식 받기
# t를 u로만 바꾸기->함수 하나만 써도 되는 골까..?

DNA=input("")
RNA=DNA.replace("T","U")
print(RNA)

# Complementing a strand of DNA
# input dna와 맞는 염기 서열을 찾는다.
# 맞는 염기서열을 찾은 뒤 거꾸로 나오게 설정

com_dna=''
seq=input("")

for nt in seq:
    if "A" in nt:
        com_dna+="T"
    elif "T" in nt:
        com_dna+="A"
    elif "G" in nt:
        com_dna+="C"
    elif "C" in nt:
        com_dna+="G"
    else:
        print("ERROR!")

print(com_dna[::-1])
    
    
# Computing GC content
# GC의 비율 구하기
# g와 c를 카운팅
# 전체 길이 구하기
# (g카운팅+c카운팅)/전체 *100 해서 구하기

seq=input("")
gc=seq.count("G")+seq.count("C")
content=(gc/len(seq))*100
print(content)





