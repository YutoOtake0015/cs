# 選択ソート
def insertionSort(arr):
    n = len(arr)

    for i in range(n):
        currentValue = arr[i]
        
        # arrの左側から現在の値より大きい値と入れ替える
        for j in range(i-1, -1, -1):
            if currentValue <= arr[j]:
                arr[j+1] = arr[j]
                arr[j] = currentValue
            else: break
    return arr


lst = [2,19,5,7,10,49]
print(lst)

insertionSort(lst)
print(lst)

        
        
        
