from typing import List

class Solution:
    
    def duplicate_zeros(self, arr: List[int]):
        i = 0
        j = len(arr) - 1
        zero = 0
        while j > i and len(arr) > 1:
            if arr[i] == 0:
                zero += 1
                i += 1
                j -= 1
            else:
                i += 1
        
        m = len(arr) -1
        while j >= 0:
            arr[m] = arr[j]
            j -= 1
            m -= 1
        
        if zero > 0:
            for i in range(0, zero):
                arr[i] = 0
        
        n = 0
        p = m + 1
        while p < len(arr) and zero > 0:
            if arr[p] == 0:
                zero -= 1
                arr[p], arr[n] = arr[n], arr[p]
                p += 1
                n += 2
            else:
                arr[p], arr[n] = arr[n], arr[p]
                n += 1
                p += 1
        return arr
        