import math

def radixSortNumber(array):
    maxLen = -1
    for number in array:
        numLen = int(math.log10(number)) + 1
        if numLen > maxLen:
            maxLen = numLen

    buckets = [[] for i in range(1, 10)]

    for digit in range(0, maxLen):
        for number in array:
            buckets[int(number / 10 ** digit % 10)].append(number)
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]


n = int(input("Enter number of elements : ")) 
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 

radixSortNumber(arr)
print(arr)
