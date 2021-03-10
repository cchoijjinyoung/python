# 기본 입출력

# 프로그램 동작의 첫번째 단계는 데이터를 입력 받거나 생성하는 것.
# ex) 학생의 성적 데이터가 주어지고, 이를 내림차순으로 정렬한 결과를 출력하는 프로그램.

## input(), map() 
n = int(input())
# data = input().split() = ['10', '20', '30', '40', '50']
data = list(map(int, input().split()))
# [10, 20, 30, 40, 50]
print(n)
print(data)

a, b, c = map(int, input().split())
print(a, b, c)
# 3개만 입력 받을 수 있다. 4개 이상 입력 시 오류.

## f-string