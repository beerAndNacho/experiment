# 이름궁합테스트

N, M = map(int, input().split())
A, B = input().split()

alp = [3,2,1,2,4,4,1,2,1,1,3,1,3,2,2,2,1,2,1,1,1,2,2,1]
AB =''
min_len=min(N,M)
for i in range(min_len):