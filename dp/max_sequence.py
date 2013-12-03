def findMaxSequence(list):
    curr_sum = 0
    curr_start = 0
    max_sum = 0
    for i in range(0, len(list)):
        # if the current sum is over zero, it means the
        # next value has the potential to bring it to a maximum
        if curr_sum > 0:
            curr_sum += list[i]
        # if the current sum is less than zero, adding the next value will
        # yeild a higher sum than starting afresh.
        else:
            curr_sum = list[i]
            curr_start = i

        # now, if out current chain exceeds the last known max value,
        # replace it and record the indexes
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = curr_start
            end = i

    return list [start: end + 1]

ms = findMaxSequence([-1, 3, -4, 10, 2, -5, 1, 4, 2, -5, 1, 3, -6, 4])
print ms