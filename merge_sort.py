import math

# マージソート
def mergeSort(arr):
    return mergeSortHerper(arr,0,len(arr)-1)

def mergeSortHerper(arr,start,end):
    # 要素を1つに特定できた場合、返却
    if start == end: return [arr[start]]

    # 要素が複数の場合、分割
    mid = math.floor((start+end)/2)
    leftArr = mergeSortHerper(arr,start,mid)
    rightArr = mergeSortHerper(arr,mid+1,end)

    # 各配列の末尾にinfitintyを追加
    leftArr.append(math.inf)
    rightArr.append(math.inf)

    l = len(leftArr) + len(rightArr) - 2
    li = 0
    ri = 0
    merged = []

    # leftArrとrightArrを比較して小さい要素を結果に格納
    while (li+ri) < l:
        if leftArr[li] <= rightArr[ri]:
            merged.append(leftArr[li])
            li += 1
        else:
            merged.append(rightArr[ri])
            ri += 1
    
    return merged


lst = [3,5,2,6,12,8,0]
print(lst)

print(mergeSort(lst))
