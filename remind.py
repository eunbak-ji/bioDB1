#import Bio
#print(Bio.__version__)
##############################################

#No.1
#w=int(input("몸무게를 입력하세요 (kg): "))
#h=float(input("신장을 입력하세요 (m): "))

#BMI=w/(h**2)
#print(f"당신의 BMI는 {BMI}입니다." )
#################################################

#No.2
# RNA_1="AUGGGGATTAAUGCAUAGCGUAG"
# RNA_2="AUGGCGTTTAAAUCGCCCUAG"
# RNA_3="AUGTTAAAAAAUGGGUAA"

# RNA=[RNA_1,RNA_2,RNA_3]
# print(RNA)

#print(f"RNA-1 : {RNA_1[-3:]},RNA-2 : {RNA_2[-3:]}, RNA-3 : {RNA_3[-3:]}")
##################################################

#No.3
#for i in [1:4]:
#    if "TTAA" in RNA_{i} 
#        print(f"RNA-{i} : True")
#    else print(f"RNA-{i} : False")

#a="TTAA" in RNA_1
#b="TTAA" in RNA_2
#c="TTAA" in RNA_3

#print(f'RNA-1 : {a}, RNA-2 : {b}, RNA-3 : {c}')
###################################################

#No.4
#l_RNA=[]
#for i in RNA:
#    rna=(len(i))  
#    l_RNA=+rna
#    print(l_RNA)
    
#R1=len(RNA_1)
#print(R1)
######################################################

#No.5
# print("life","is","too short",sep=",")

# seq_a="CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
# seq_b="CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
# seq_c="CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
# seq=[seq_a,seq_b,seq_c]
# # print(seq)


# def GC_content(seq):
#     gc=seq.count("G")+seq.count("C")
#     content=(gc/len(seq))*100
#     return(content)

# for i in seq:
#     GC_content(i)
###############################################################

#No.6
# dna_rna={'A':'U','T':'A','G':'C','C':'G'}
# dna=input("DNA sequence: ")

# RNA=[]
# if len(dna) >3 :
#     for rna in dna:
#         rna=dna_rna[rna]
#         RNA.append(rna)
#     print(f"RNA sequence:{''.join(RNA)}") 
# else:
#     print("error!")
###############################################################

# a=[1,2,3]
# def temp():
#     global a
#     a=[4,5,6]
    
# temp()
# print(a)

import math 
math.ceil(-3.14)
math.ceil(3.14)