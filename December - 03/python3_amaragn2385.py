def isin(index,m):
    if index not in range(m):
        return False
    else:
        return True

def fun3():
    out = [[0 for x in range(n)] for y in range(n)] 
    str_out = [["" for x in range(n)] for y in range(n)] 
    print(out)
    for i in range(n):
        for j in range(n):
            if('#' == arr[i][j]):
                if(isin(i-1,n) and isin(j-1,n) and '-' == arr[i-1][j-1]):
                    out[i-1][j-1]+=1
                if(isin(i-1,n) and isin(j,n) and '-' == arr[i-1][j]):
                    out[i-1][j]+=1
                if(isin(i-1,n) and isin(j+1,n) and '-' == arr[i-1][j+1]):
                    out[i-1][j+1]+=1
                if(isin(i,n) and isin(j-1,n) and '-' == arr[i][j-1]):
                    out[i][j-1]+=1
                if(isin(i,n) and isin(j+1,n) and '-' == arr[i][j+1]):
                    out[i][j+1]+=1
                if(isin(i+1,n) and isin(j-1,n) and '-' == arr[i+1][j-1]):
                    out[i+1][j-1]+=1
                if(isin(i+1,n) and isin(j,n) and '-' == arr[i+1][j]):
                    out[i+1][j]+=1
                if(isin(i+1,n) and isin(j+1,n) and '-' == arr[i+1][j+1]):
                    out[i+1][j+1]+=1
                str_out[i][j] = "#"
    for i in range(n):
        for j in range(n):
            if("#" != str_out[i][j]):
                str_out[i][j]=str(out[i][j])
    return str_out

if __name__ == '__main__':
    n = int(input())
    arr = [input().translate({ord(i): None for i in '[]" '}).split(',')  for x in range(n)]
    print(str(fun3())[1:-1])