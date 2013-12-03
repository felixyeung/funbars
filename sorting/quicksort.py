def quickSort(values):
    # if our list contains one or less elements, it must be sorted.
    if len(values) <= 1:
        return values
    left = []
    right = []
    pivot =  choosePivot(values)
    print "looking at value %s at %s as pivot" % (values[pivot], pivot)
    for val in (values[:pivot] + values[pivot + 1:]):
        if val < values[pivot]:
            left.append(val)
        else:
            right.append(val)
    print left
    print right

    return quickSort(left) + [values[pivot]] + quickSort(right)

def choosePivot(list):
    if len(list) % 2 == 1:
        return (len(list) - 1) / 2
    else:
        return len(list) / 2

qs = quickSort([11, 3, 12, 12, 7, 4, 9, 4, 1, 6, 2, 5, 8, 6, 10, 13])

print qs