# ####### THIS IS JUST FOR TESTING

def binarySearch(nums, num):
    low = 0
    high = len(nums)
    while low <= high:
        mid = (low + high) // 2
        if num == nums[mid]:
            return mid
        elif num > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binarySearch([1,3,4,5,6,6,6,6,8,9,12,14,18], 11))
