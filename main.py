nums = [1,2,1]
# Output: [1,2,1,1,2,1]
#
nums2 = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]

def list_concatenation(lst):
    new_nums = []
    for i in range(len(lst)):
        new_nums.append(lst[i])
    for j in range(len(new_nums)):
        new_nums.append(new_nums[j])
    print(new_nums)
list_concatenation(nums)
list_concatenation(nums2)
