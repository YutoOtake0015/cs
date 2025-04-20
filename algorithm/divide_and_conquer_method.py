# 分割統治法
import math

def sumOfArray(arr):
    return sumOfArrayHelper(arr, 0, len(arr)-1)

def sumOfArrayHelper(arr, start, end):
    if start == end:
        return arr[start]
    
    # 配列の中間のインデックス
    mid = math.floor((start+end) / 2)

    # leftArr→先頭から中間、rightArr→中間+1から終端
    leftArr = sumOfArrayHelper(arr, start, mid)
    rigthArr = sumOfArrayHelper(arr, mid+1, end)

    return leftArr+rigthArr

lst = [1,2,3,4,5,6,7,8,9,10]
print(sumOfArray(lst))
