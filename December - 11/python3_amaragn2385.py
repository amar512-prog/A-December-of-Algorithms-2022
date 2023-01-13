
def fun(input,jump):
    out = 0
    i = 0
    for x in jump:
        if(input[i]=='~'):
            return out
        else:
            out+=1
            i+=x
    if(input[i]=='~'):
        return out-1
    else:
        return out

if __name__ == '__main__':
    t = input().translate({ord(x):None for x in "[]' "})
    input_list = t.split(',')
    jump = list(map(int,input().translate({ord(x):None for x in "[] "}).split(',')))
    print(fun(input_list,jump))
