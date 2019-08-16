# 1) Sort all jobs in decreasing order of profit.
# 2) Initialize the result sequence as first job in sorted jobs.
# 3) Do following for remaining n-1 jobs
# a) If the current job can fit in the current result sequence without missing the deadline
# add current job to the result. Else ignore the current job.

def job_schedule(arr , key):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j+1][2]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
        
    result = [False] * key
    output = ['-1'] * key

    for i in range(len(arr)):
        for j in range(min(key-1, arr[i][1] - 1) , -1 , -1):
            if result[j] is False:
                print('value is: ')
                print(j)
                result[j] = True
                output[j] = arr[i][0]
                break

    print(output)

arr = [['a', 2, 100],
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]] 
  
  
print("Profit of jobs") 
print(job_schedule(arr, 3))
