
def fun9(input):
    out = "Better luck next time"
    l=[]
    for x in input:
        if(len(x)%2==1):
            l.append(x)
    if (len(l)==0):
        return out
    else:
        max = 0
        for x in l:
            if (len(x)>max):
                max = len(x)
                out = x
        return out

if __name__ == '__main__':
    n = int(input())
    inp = input().split()
    print(fun9(inp))