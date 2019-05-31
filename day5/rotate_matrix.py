def rotate(a,n):
    for i in range(n):
        for j in range (n-1,-1,-1):
            print(a[i+j*n], end=' ')
    

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
        rotate(a,n)
        print('\n')
    a.clear()
        
main()
