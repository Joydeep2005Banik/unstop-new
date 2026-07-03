from collections import deque
def smallest_max_difference(arr, k):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers
        k (int): Size of the subarray
    Returns:
        int: Smallest maximum difference among all contiguous subarrays of size k
    """
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    max_deque=deque()  
    min_deque=deque()  
    
    min_diff=float('inf')
    
    for i in range(k):
        while max_deque and arr[max_deque[-1]] <= arr[i]:
            max_deque.pop()
        max_deque.append(i)
        
        while min_deque and arr[min_deque[-1]] >= arr[i]:
            min_deque.pop()
        min_deque.append(i)
    
    min_diff=arr[max_deque[0]]-arr[min_deque[0]]
    
    for i in range(k,len(arr)):
        while max_deque and max_deque[0] <= i-k:
            max_deque.popleft()
        while min_deque and min_deque[0] <= i-k:
            min_deque.popleft()
        
        while max_deque and arr[max_deque[-1]] <= arr[i]:
            max_deque.pop()
        max_deque.append(i)
        
        while min_deque and arr[min_deque[-1]] >= arr[i]:
            min_deque.pop()
        min_deque.append(i)
        
        curr_diff=arr[max_deque[0]]-arr[min_deque[0]]
        min_diff=min(min_diff,curr_diff)
    
    return min_diff


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # The first line of input contains an integer N
    arr = list(map(int, data[1:n+1]))  # The second line contains the array of length N
    k = int(data[n+1])  # The third line contains the integer K
    
    # Call the user logic function and print the output
    result = smallest_max_difference(arr, k)
    print(result)


if __name__ == "__main__":
    main()