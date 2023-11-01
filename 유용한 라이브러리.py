# python은 1초에 2~5천만 정도의 연산을 가짐 그래서 N3승의 알고리즘 같은 경우 N = 5000이면 2500초가 걸린다
# 시간제한이 1초인 문제를 만났을 때, 일반적인 기준
# N의 범위가 500이면 O(N3) 가능
# N의 범위가 2000이면 O(N2) 가능
# N의 범위가 100,0000이면 O(NlogN) 가능
# N의 범위가 10,000,000이면 O(N) 가능

# 아래와 같은 코드로 수행시간 측정가능

from bisect import bisect_left, bisect_right
import math
from collections import Counter
from itertools import *
from itertools import permutations
import sys
import time
start_time = time.time()

# 프로그램 소스코드
end_time = time.time()
print("time:", end_time - start_time)

# 아래와 같이 조건문 추가 가능
array = [i for i in range(20)if i % 2 == 1]
print(array)

# 2차원 deep copy and shallow copy
array = [[0] * 5 for _ in range(5)]  # deep copy(5*5)
array[1][1] = 1
print(array)
array = [[0]*5] * 5  # shallow copy(5*5) => 전체 리스트 안에 포함된 각 리스트가 같은 객체로 인식
array[1][1] = 1
print(array)

# list method
# 1. append()
# 2. sort() 오름차순 + sort(reverse = True) 내림차순 O(NlogN)복잡도
# 3. reverse()
# 4. insert(삽입할 위치 인덱스, 삽일 할 값)
# 5. count(특정 값)
# 6. remove(특정 값) => 하나만 제거
# 모두 제거하기 위해선

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]  # 즉 리스트를 다시 만드는 법
print(result)

# 튜플이 사용되는 경우 => 변경 불가 이에 반해 리스트는 변경 가능
# 1. 서로 다른 성질의 데이터를 묶어서 관리해야 할 때 => 최단 경로 알고리즘에서는(비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용
# 2. 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때 => 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있다.
# 3. 리스트보다 메모리를 효율적으로 사용해야 할 때

# 딕셔너리는
# 1. 키와 값의 쌍을 데이터로 가지는 자료형이며, 리스트와 튜플과는 다르게 값을 순차적으로 저장하는 것과는 대비된다.
# 2. 해쉬 테이블을 이용하므로 데이터 조회 및 수정은 O(1)시간이 걸린다
# 3. 변경 불가능한 자료형을 키로 사용할 수 있다.

# diction method
# 1. keys() 키만 출력
# 2. values() 값만 출력

data = dict()
# 딕셔너리 키, 값이라는 하나의 객체로 반환하기 떄문에 list로 바꿔주거나 for문으로 하나씩 출력하는 것이 가능하다.
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)
for key in key_list:
    print(data[key])

# 집합 자료형
# 초기화 방법 1 & 2
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 자료형의 연산에선 합칩합, 교집합, 차집합을 제공한다.

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
print(a | b)
print(a & b)
print(a - b)

# add, update, remove함수를 이용할 수 있다.
a.add(6)
print(data)  # 새로운 원소 추가

data.update([10, 11])  # 여러 데이터 넣기
print(data)

data.remove(3)
print(data)  # 특정한 값을 갖는 원소 삭제

# 딕셔너리 + 집합 자료형 특징은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다.
# 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
# 사전의 키 혹은 집합은 원소를 이용해 O(1)시간 복잡도로 조회가능

# 입력받는 방법
# 1. 보통은 input()
# 2. 입력을 최대한 빠르게 받는 경우 sys.stdin.readline() 단, 엔터가 줄 바꿈 기호로 입력되므로 rstrip() method 함께 사용
data = list(map(int, sys.stdin.readline().rstrip()))
print(data)

# pass는 조건문 반복문에서 디버깅을 위해 아무 것도 안하고 가는 경우

# 람다 표현식 => 특정한 기능을 수행하는 함수를 한 줄에 작성 가능
print((lambda a, b: a+b)(3, 7))

# 자주 사용되는 람다 함수 방식
# 제일 점수가 높은 사람 순으로 정렬하는 경우
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))  # 오름차순
print(sorted(array, key=lambda x: x[1], reverse=True))  # 내림차순
# --------------2번째

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)
print(list(result))

# 꼭 기억해야할 표준 라이브러리
# 1. itertools => 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공(특히 순열과 조합에서)
# 2. heapq => 우선순위 큐 기능 구현을 위해
# 3. bisect => 이진 탐색 기능 제공
# 4. collections => deque, Counter등
# 5. math => 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수, 파이 상수 포함

# 내장 라이브러리
# 1. sum, min, max
# 2. eval => 사람 입장에서 수식으로 표현된 String을 값으로 반환
# 3. sorted() / sorted(reverse = True)

# 순열 => 서로 다른 n개에서 서로 다른 r개를 선택하여 잉렬로 나열하는 것(순서 상관함) => nPr
# 조합 => 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것(순서 상관안함) => nCr
# from itertools import permutations 라이브러리 사용
# from itertools import combinations 라이브러리 사용
# from itertools import product 라이브러리 사용
# from itertools import combinations_with_replacement
data = ['A', 'B', 'C']

result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)
result = list(combinations(data, 2))  # 조합 구하기
print(result)
result = list(product(data, repeat=2))  # 2개를 뽀는 모든 순열 구하기(중복 허용)
print(result)
result = list(combinations_with_replacement(
    data, 2))  # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)

# from collections import Counter => 등장 횟수를 세는 기능 제공 즉, 리스트와 같은 반복 가능한(iterable)객체가 주어졌을 때 내부의 원소가 몇 번씩 등장하는지 알려준다.

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))  # 사전 자료형으로 반환

# math라이브러리


def lcm(a, b):
    return a*b // math.gcd(a, b)


a = 21
b = 14
print(math.gcd(21, 14))  # 최대 공약수(GCD) 계산 => 최대 공약수는 공통된 약수 중 가장 큰 값
print(lcm(21, 14))  # 최소 공배수(LCM)계산 => 최소 공배수는 공통된 약수 중 가장 작은 값

print((2//3)*3)

# 아스키코드
print(ord("A"))
print(ord("B"))
print(ord("C"))

# 65
# 66
# 67

print(chr(65))
print(chr(66))
print(chr(67))

# A
# B
# C

# isalpha()라는 함수로 알파벳인 경우 확인 가능
# ascii code => 65부터 90까진 대문자 알파벳 97부터 122까진 소문자 알파벳


a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))  # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
print(bisect_right(a, x))  # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
