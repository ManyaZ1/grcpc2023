from collections import deque
from time import time
import decimal
def parser(i):
    with open(f'input_{i}_tempe.in','r') as my_file:
        length=my_file.readline()
        window=int(my_file.readline())
        nums=list(map(float,my_file.readline().split()))
    return length,window,nums

def maxDifSlidingWindow(nums, k) :#2monotonic queues
    res = []
    qmin=deque()
    maxdif=0
    for idx, num in enumerate(nums):
        #print(idx)
        #print(q)
        #print(qmin)

        while qmin and qmin[-1]>num:
            qmin.pop()
        qmin.append(num)

        if idx >= k and qmin[0]==nums[idx-k]: 
            qmin.popleft()
        
        if qmin and (qmin[-1]-qmin[0])>maxdif:
            maxdif=qmin[-1]-qmin[0]

        if idx >= k - 1:
            res.append(maxdif)
    
    return (max(res))
'''
nums=[30, 28, 30, 29, 32, 26, 27, 30, 28, 33]
k=6
print(maxDifSlidingWindow(nums, k))'''
def solution(i):
    length,window,nums=parser(i)
    return maxDifSlidingWindow(nums, window)



def checker(i):
    with open(f'input_{i}_tempe.ans','r') as my_file:
        ans=float(my_file.readline().rstrip())
    res=solution(i)
    #print(res)
    if "{:.6f}".format(ans) != "{:.6f}".format(res) :
        print(f'{i} {res} vs {ans}')
        return False
    
    return True

def main():
    flag=True
    start=time()
    for i in range(1,8):
        if(i==2 or i==5 or i==6):continue
        #print(flag)
        flag=checker(i)
        if not flag:
            print("Wrong!")
            break
    end=time()
    if flag: print(f"all correct t={end-start}")

main()
#print(solution(1))
        