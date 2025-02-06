#brute force
nums = [2,7,11,15]
target=int(input("please enter target"))
def sum_brute_force(nums, target):
    n = len(nums)
    for i in range (n):
        for j in range(i + 1, n):
            if nums[i] + nums[j]== target:
                print([i,j])
    return []           
sum_brute_force(nums, target)
    
    #hash map dictionary
def sum_optimized(nums,target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            print ([num_map[complement],i])
        num_map[num]= i
    return []
sum_optimized(nums,target)