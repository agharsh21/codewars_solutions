def maxSequence(arr):
    n = len(arr)
    max_sum=[]
    if n==0:
        return 0
    else:
        for k in range(0,n+1):
            for i in range(n - k + 1):
                current_sum = 0
                for j in range(k):
                    current_sum = current_sum + arr[i + j]
                max_sum.append(current_sum)
        max_sum.sort()
        return max_sum[-1]
