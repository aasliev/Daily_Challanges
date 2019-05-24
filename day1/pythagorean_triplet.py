import math

def checkForPythagoreanTriples(a,n):
   for i in range(n-1,2,-1):
       first = 0
       last = i-1
       while(first<last):
           if(a[first]+a[last]==a[i]):
               return True
           elif(a[first]+a[last]<a[i]):
               first=first+1
           else:
               last = last-1
   return False
        

def getInputs():
    print('Enter n: ')
    n= int(input())
    print('Array: ')
    a=list(map(int,input().split()))
    return n,a

def main():
    print('Enter T: ')
    T = int(input())
    for i in range(T):
        n,a = getInputs()
        a.sort()
        for i in range (0,n):
            a[i] = int(math.pow(a[i],2))
        print(a)
        if(checkForPythagoreanTriples(a,n)):
            print('yes')
        else:
            print('no')
    a.clear()
        
main()





