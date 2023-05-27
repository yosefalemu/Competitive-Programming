#User function Template for python3

class Solution: 
    def select(self, input_list, i):
        n = len(input_list)
        for i in range(n - 1):
            min_index = i
            for j in range(i, n):
                if input_list[j] < input_list[min_index]:
                    min_index = j
            if min_index != i:
                input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
        return input_list
    
    def selectionSort(self, arr,n):
        return self.select(arr, 0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends