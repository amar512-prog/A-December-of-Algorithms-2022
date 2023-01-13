
def fun8(input):
    out = ""
    for i in range(0,len(input),2):
        if(i+1<len(input)):
            out+=(input[i+1]+input[i])
        else:
            out+=(input[i])
    return out

if __name__ == '__main__':
    inp = input()
    print(fun8(inp))