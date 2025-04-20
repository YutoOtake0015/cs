# 選択ソート
def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        minIndex = i

        # arrから、iより右側から最小値のインデックスを探索
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        # 最小値を入れ替え
        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp

    return arr


lst = [2,19,5,7,10,49]
print(lst)

selectionSort(lst)
print(lst)

        
        
        
