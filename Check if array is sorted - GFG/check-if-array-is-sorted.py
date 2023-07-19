#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        slowpt = 0
        fastpt = 1
        if n == 1:
            return True
        elif n == 2:
            if arr[1] >= arr[0]:
                return True
            else:
                return False
        else:
            while fastpt < n:
                if arr[slowpt] > arr[fastpt]:
                    return False
                slowpt += 1
                fastpt += 1
        return True
            
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends