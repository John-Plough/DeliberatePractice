# def largestAltitude(gain):

#     alts = [0]
#     alt = 0

#     for num in gain:
#         alts.append(num + alt)
#         alt = alts[-1]

#     return max(alts)


# def largestAltitude(gain):

#     max_alt = 0
#     curr_alt = 0

#     for num in gain:
#         curr_alt += num
#         max_alt = max(max_alt, curr_alt)
    
#     return max_alt




def findDifference(nums1, nums2): 
    answer = [[],[]]

    for num in nums1:
        if num not in nums2 and num not in answer[0]:
            answer[0].append(num)

    for num in nums2:
        if num not in nums1 and num not in answer[1]:
            answer[1].append(num)
    
    return answer 

#nums1 = [1,2,3], nums2 = [2,4,6]  --->  [[1,3],[4,6]]

def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    res1 = set()
    res2 = set()

    for num in nums1:
        if num not in set2:
            res1.add(num)

    for num in nums2:
        if num not in set1:
            res2.add(num)

    return [list(res1), list(res2)]


def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return [list(set1 - set2), list(set2 - set1)]

nums1 = [1,2,3]
nums2 = [2,4,6]  
#--->  [[1,3],[4,6]]

print(findDifference(nums1, nums2))