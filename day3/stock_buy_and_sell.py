'''def find_max(a,n):
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




'''


#code
noProfCond = True

def checkNoProfit():
    global noProfCond
    if noProfCond:
        print ("No Profit", end="")
    print()

def printStr(buy, sell):
    global noProfCond
    string = "("+ str(buy)+" "+ str(sell)+") "
    print(string, end="")
    noProfCond = False

def getBestStock(lst, listLen):
    arr = list(map(int, lst))
    buyStock = 0
    lastDayCheck = False
    for i in range(listLen-1):
        if (arr[buyStock] > arr[i]):
            buyStock = i
        if (arr[i]>arr[i+1] or i == listLen -2) and arr[buyStock] < arr[i]:
            if arr[i]>arr[i+1]:
                printStr(buyStock, i)
            else:
                printStr(buyStock, i+1)
                lastDayCheck = True
            buyStock = i+1
            
    if arr[i] < arr[i+1] and (not lastDayCheck):
        printStr(i, i+1)
    arr.clear()

def main():
    numOfTestCases = int(input())
    for i in range(numOfTestCases):
        listSize = int(input())
        lst = input().split()
        getBestStock(lst, listSize)
        checkNoProfit()
        lst.clear
        
if __name__== "__main__":
  main()