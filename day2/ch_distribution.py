def ch_distribution(a,n,m):
    tmp = a[m-1]-a[0]   
    for i in range(n-m):
        if(tmp>a[m+i]-a[i+1]):
            tmp = a[m+i]-a[i+1]
    return tmp
        

def getInputs():
    print('Enter n: ')
    n= int(input())
    print('Array: ')
    a=list(map(int,input().split()))
    print('Enter m: ')
    m= int(input())
    return n,m,a

def main():
    print('Enter T: ')
    T = int(input())
    for i in range(T):
        n,m,a = getInputs()
        a.sort()
        print(ch_distribution(a,n,m))
    a.clear()
        
main()





