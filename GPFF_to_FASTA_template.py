def Take_Region_name(lines_list):
    name=[]#region_name이 여러개일 경우 커다란 그릇 만들어주기
    for line in lines_list:
        if '/region_name=' in line:
            region_name=line.split('"')[1]
            name.append(region_name)#name이라는 그릇에 하나씩 담는 중
    return name #return이 for문 안에 있을 경우 한번 돌고 끝나는 것에 주의하기/ name이라는 그릇에 다 담아서 출력하기



def Take_Version(lines_list):
    for line in lines_list:
        if ' VERSION ' in line:
            return line.strip().split(" ")[1]


def Take_Definition(lines_list):
    for line in lines_list:
        if 'DEFINITION  ' in line:
            return line.strip.split(" ")[2:] 


def Take_Protein_Region_Sequence():
    return 0


def Write_FASTA(output_path,result): #변수는 여러개 받을 수 있다, 다만 순서주의
                                     #변수로 설정한 것이 아닌 것을 사용하면 컴퓨터 못알아먹어요
    f=open(output_path,'w')
    for i in result: #넣고 싶은 내용이 여러개일 경우 for문 이용하여 i라는 그릇에 하나씩 넣어서 출력
        f.write(i)

    return 0 # return의 의미, 말그대로 출력 return은 함수당 한번만 쓸 수 있으며 return선언을 해버리면 함수는 더이상 작동 안함.


def main():
    GPFF = open("/home/Bio_Genome_Coding/assistant/python/b11_GPFF/ref_file/pilot.gpff", 'r')
    lines_list = [line for line in GPFF.readlines()]
    region_name = Take_Region_name(lines_list)  # 1번 정보/밖에 있는 변수를 가지고 오고 싶을 때에 함수에 변수 선언하기
    version = Take_Version(lines_list) # 2번 정보
    print(version)
    definition = Take_Definition(lines_list)  # 3번 정보
    print(definition)
    protein_region_sequence = Take_Protein_Region_Sequence()  # 4번 정보
    protein_length = -999  # 5번 정보

    info = [region_name, version, protein_length, definition, protein_region_sequence]

    output_path = "/home/Bio_Genome_Coding/202114027/python/PeptidaseM60.fasta"
    Write_FASTA(output_path,info[0])#함수에 변수 2개 설정한 것 따라서 해주기


main()
