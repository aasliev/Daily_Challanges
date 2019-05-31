def fnc(a,n):
    tmpMin = []
    tmpMax = []
    tmpMax.append(a[0])
    tmpMin.append(a[n-1])
    for i in range (1,n):
        tmpMax.append(max(tmpMax[i-1],a[i]))
    for j in range (n-2,-1,-1):
        tmpMin = min(tmpMin[j+1],a[j]) + tmpMin
    for k in range (1,n-1):
        if tmpMax[k]==tmpMin[k]:
            return tmpMin[k]
    return -1
            

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
        print(fnc(a,n))
    a.clear()
        
main()
