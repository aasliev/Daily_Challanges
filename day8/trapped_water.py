def trapped_water(a,n):
    max_water = 0
    leftWall, rightWall = get_walls(a,n)
    for i in range(1,n-1):
        if min(leftWall[i],rightWall[i])-a[i] >=0:
            max_water +=min(leftWall[i],rightWall[i])-a[i]
    return max_water


def get_walls(a,n):
    rightWall = []
    leftWall = []
    leftWall.append(a[0])
    rightWall.append(a[n-1])
    for i in range (1,n):
        leftWall.append(max(leftWall[i-1],a[i]))
        rightWall.insert(0,max(rightWall[0],a[n-1-i]))
    return leftWall, rightWall



def getInputs():
    n= int(input())
    a=list(map(int,input().split()))
    return n,a

def main():
    T = int(input())
    for i in range(T):
        n,a = getInputs()
        print(trapped_water(a,n))
        
    a.clear()
        
main()