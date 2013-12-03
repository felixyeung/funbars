def mergeSort(list):
    if len(list) <= 1:
        return list
    else:
        middle = findMiddle(list)
        left = mergeSort(list[:middle])
        right = mergeSort(list[middle:])
        return mergeHelper(left, right)

def mergeHelper(left, right):
    print "merging"
    merged_list = []
    while left and right:
        if left[0] < right[0]:
            merged_list.append(left[0])
            left = left[1:]
        else:
            merged_list.append(right[0])
            right = right[1:]
    while left:
        merged_list.append(left[0])
        left = left[1:]
    while right:
        merged_list.append(right[0])
        right = right[1:]
    return merged_list

def findMiddle(list):
    if len(list) % 2 == 1:
        return (len(list) - 1) / 2
    else:
        return len(list) / 2

ms = mergeSort([11, 3, 12, 12, 7, 4, 9, 4, 1, 6, 2, 5, 8, 6, 10, 13])

print ms
