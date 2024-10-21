def two_sum(arr, target):
    # Sort the array
    arr = quick_sort(arr)
    
    # Initialize two pointers
    left = 0
    right = len(arr) - 1
    
    # Loop until the pointers meet
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []  # Return an empty list if no pair is found

# Quick sort function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [1, 2, 3]
target = 5
result = two_sum(arr, target)
print(result)  # Output: [2, 3]
