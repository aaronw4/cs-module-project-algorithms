'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
#Recursive
# def sliding_window_max(nums, k):
#     # Your code here
#     index = k - 1

#     if len(nums) == k:
#         nums.sort()
#         return [nums[index]]
#     else:        
#         temp = nums[:k]
#         temp.sort()
#         return [temp[index]] + sliding_window_max(nums[1:], k)

#Iterative
def sliding_window_max(nums, k):
    arr = []
    
    while len(nums) >= k:
        temp = nums[:k]
        temp.sort()
        arr.append(temp[k-1])
        nums.pop(0)
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    # arr = [1, 3, 2]
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
