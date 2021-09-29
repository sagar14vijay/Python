# Count triplets with sum smaller than a given value
# Given a list of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value.
# The expected Time Complexity is O(n2).
# Input : arr = [-2, 0, 1, 3]
#         sum = 2.
# Output : 2
# Explanation :  Below are triplets with sum less than 2
#                (-2, 0, 1) and (-2, 0, 3)
# Input : arr = [5, 1, 3, 4, 7]
#         sum = 12.
# Output : 4
# Explanation :  Below are triplets with sum less than 12
#                (1, 3, 4), (1, 3, 5), (1, 3, 7) and
#                (1, 4, 5)
from bisect import bisect_left, bisect_right

lst = [-2, 0, 1, 3]

def triplets(lst, target):
    l = len(lst)
    count = 0
    for i in range(l - 2):
        for j in range(i + 1, l - 1):
            sm = lst[i] + lst[j]
            rem = target - sm
            index = bisect_left(lst, rem - 1)
            if rem - 1 in lst:
                index -= 1

            if index > j:
                count += (index - j)
            else:
                break
    print(count)
    return count


ans = triplets(lst, 2)
