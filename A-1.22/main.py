array = [54326, 2, 3, 5, 65, 5324, 34, 324, 5, 23,
         61, 6, 123, 52334, 2, 562, 34, 5, 12, 4223]
for i in range(1, len(array)):
    for j in range(0, len(array)-i):
        if(array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
print(array)
