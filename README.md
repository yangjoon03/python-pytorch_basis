## pytorch기반 python코드
  * 기초는 .py 확장자로 출력이 되지 않음.
  * .py , .ipynb 확장자 ✔확인
  * pytorch 모듈
    <br>
    
## 1.list_indexing
  ``` python
  list.append()
  list.extend()  #list+list
  list.insert()  #index
  list.remove()  #particular value
  list.pop()     
  list.index()   #value_index_search
  list.count()   #특정 값 개수 세기
  list.sort()
  list.reverse()
  ```
<br>

## slicing
## for
## numpy
<br>

## A.Importing Data pytorch(데이터 불러오기)
 * 데이터 경로
 ```python
 #절대경로
 dataset_path = "C:/Users/양준영/project/data/folder/train"
 #상대경로
 dataset_path = "data/folder/train"
 ```
<br>

## B.Compose 이미지 전처리
 * 이미지 자르기,회전,반전,크롭 등을 지원함.
 * 추가로 이미지 특정개수로 나누기 등도 있음.
```python
transform = transforms.Compose([
transforms.resize()
])
```
<br>

## C.CV2 이미지 전처리
<br>

## D.데이터 분할
 * 훈련 , 검증 , 테스트

## Ⅰ VGG16(전이 학습)
 * 각 클래스당 20장의 이미지로 마지막 층에 대한 전이학습.
 * ✨배치 사이즈가 무조건 크다고 좋은게 아니다.
