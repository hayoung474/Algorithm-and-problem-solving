def set_cover(universe, subsets):
    elements = set(e for s in subsets for e in s) # set으로 변환
    
    if elements != universe: # U에 element가 없다면 
        return None
    covered = set() # Set() 자료구조 선언
    cover = [] # 커버 가능한 S를 저장할 리스트 
    while covered != elements: # covered와 element가 다를동안 반복함.
        subset = max(subsets, key=lambda s:len(s-covered))
        
        cover.append(subset)
        covered |= subset
    return cover

universe = set(range(0, 6))
subsets = [set([0,3,4]),
            set([1,2,3]),
            set([2,3,4]),
            set([0,4,5]),
            set([1,4,5]),
            set([2,4,5])]
cover = set_cover(universe, subsets)
print(cover)
