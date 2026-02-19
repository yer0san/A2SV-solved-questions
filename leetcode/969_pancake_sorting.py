class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for i in range(n, 1, -1):
            largest = 0
            for j in range(i):
                if arr[j] > arr[largest]:
                    largest = j

            if largest == i - 1:
                continue

            if largest != 0:
                res.append(largest + 1)
                arr[:largest+1] = arr[:largest+1][::-1]

            res.append(i)
            arr[:i] = arr[:i][::-1]

        return res
