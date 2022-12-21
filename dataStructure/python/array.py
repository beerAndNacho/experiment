### 배열

# 데이터를 나열하고 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
# 파이썬에서는 리스트 타입이 배열 기능 제공함

### 배열의 필요성

# 같은 종류의 데이터를 효율적으로 관리하기 위해 사용한다.
# 같은 종류의 데이터를 순차적으로 저장
# 장점
#  - 빠른 접근 가능 
#    - 첫 데이터의 위치에서 상대적인 위치로 데이터 접근 (인덱스 번호로 접근)
# 단점
#  - 데이터 추가/삭제가 어려움
#   - 자바나 C언어의 경우는 최대 길이를 지정해야하는 어려움이 있음

### point 조회가 편하나 추가 삭제는 어렵다. 따라서 전체적인 사이즈가 겨의 변하지 않는 데이터 구조에서
### 유리하지만 전체 사이즈를 자주 변경하는 경우에는 유지보수가 어려울 수 있다.

data_list = [1,2,3,4,5]

print(data_list)

data_list = [[1,2,3],[4,5,6],[7,8,9]]

print(data_list)

print(data_list[0])

print(data_list[2][2])

dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']

m_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            m_count += 1
print(m_count)            

print(range(5))

# 패스트캠퍼스 알고리즘 / 기술면접 완전 정복 올인원 패키지 참고