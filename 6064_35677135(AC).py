a, b, c = map(int, input().split())

# 가장 작은 값을 찾기 위한 3항 연산자 사용
d = (a if a < b else b) if ((a if a < b else b) < c) else c

print(d)
