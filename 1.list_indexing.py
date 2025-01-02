list_a = [1,2,3,4,5,6,7,8,9,10]
list_b = [12]

list_a.append(11)
list_a.extend(list_b)  #list_a+list_b
list_a.insert(0,1)  #index
list_a.remove(1)  #particular value
list_a.pop(1)     
list_a.index(1)   #value_index_search
list_a.count(12)   #특정 값 개수 세기
list_a.sort()
list_a.reverse()

#아직 수정해야함.
