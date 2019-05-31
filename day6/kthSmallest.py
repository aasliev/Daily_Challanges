import random


def partition(arr,low,high): 
    iPivot = random.randint(low,high)
    print(iPivot)
    arr[iPivot],arr[high]=arr[high],arr[iPivot]
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


def findKthSmallest(a,l,r,k):
    if(r-l+1>k):
        pivot = partition(a,l,r)
        if pivot+1 == k:
            return a[pivot]
        elif pivot+1>k:
            return findKthSmallest(a,l,pivot-1,k)
        elif pivot+1<k:
            return findKthSmallest(a,pivot+1,r,k-pivot-1)

def getInputs():
    print('Enter n: ')
    n= int(input())
    print('Array: ')
    a=list(map(int,input().split()))
    print('Enter k: ')
    k=int(input())
    return n,a,k

def main():
    print('Enter T: ')
    T = int(input())
    for i in range(T):
        n,a,k = getInputs()
        print(findKthSmallest(a,0,n-1,k))
        
    a.clear()
        
main()

