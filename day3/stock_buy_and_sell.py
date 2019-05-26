def find_max(a,n):
    tmpMin,tmpMax,result = 0,0,''
    for i in range(1,n):
        if (a[i]>a[tmpMax]):
            tmpMax = i
        elif (a[i]<a[tmpMin] or a[i]<a[tmpMax]):
            if tmpMin != tmpMax:
                result = result + '('+str(tmpMin)+' ' + str(tmpMax)+')'
            tmpMin, tmpMax = i,i
    if tmpMin != tmpMax:
        result = result + '('+str(tmpMin)+' ' + str(tmpMax)+')'
    if result == '':
        result = 'No Profit'
    return result




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
        print(find_max(a,n))
    a.clear()
        
main()
