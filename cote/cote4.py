# 백준 온라인 테스트 이름궁합 테스트
N, M = map(int, input().split())
A, B = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,
        1,2,2,2,1,2,1,1,1,2,2,1]

AB = ''
min_len = min(N,M)
for i in range(min_len):
    AB += A[i] + B[i]

# : 는 리스트의 끝 인덱스이다. ex [7,8] 리스트가 있다면 8 다음의 index를 가르킨다.
AB += A[min_len:] + B[min_len:]
lst = [alp[ord(i)-ord('A')] for i in AB]

# def f(lst):
#     ret = []
#     for i in range(lst-1):
#         ret.append(lst[i]+lst[i+1]%10)
#     return ret

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]
        
print("{}%".format(lst[0] % 10*10+lst[1]%10))

print((lst[0]%10)*10, lst[1]%10)

print(1%10)
