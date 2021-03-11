# 리스트 자료형
# C 나 Java 에서의 Array 와 비슷한 기능 수행.
a = [1, 2, 3, 4, 5]
print(a)

print(a[3]) # 네 번째 원소만 출력.

# 크기가  N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

a = [1, 2, 3, 4, 5, 6, 7] 
print(a[-1]) # 뒤에서 첫번째
print(a[-3]) # 뒤에서 세번째

# 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 Slicing을 이용한다.
# 대괄호 안에 콜론을 넣어서 시작인덱스와 끝 인덱스를 설정할 수 있다.
# 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정한다.
print(a[1 : 4]) # [2, 3, 4]

array = [i for i in range(10)]
print(array) # [0 ~ 9]

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
# 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]
print(array)

# insert(), append(), sort(), remove()
