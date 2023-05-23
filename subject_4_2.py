# 저보다 더 잘푸신 분들의 코드를 공유드립니다.

n = int(input("숫자를 입력해주세요 : "))
a = n
if 0 <= n <= 99: 
    cycle = 0
    while True:
        n1 = n % 10
        n10 = n // 10
        n1_n10 = n1 + n10
        if n1_n10 < 10:
            n = (n1 * 10) + n1_n10
            new = n
        else:
            n = (n1 * 10) + (n1_n10 % 10)
            new = n
        cycle += 1
        if new == a:
            print(f"cycle : {cycle}")
            print("코드종료")
            break
else: 
    print("0이상 99이하의 숫자를 입력해주세요.")
