
def fun10(input):
    out = "YES"
    vowels = "aeiou"
    for i,x in enumerate(input):
        if(i+3<len(input) and (input[i] not in vowels) and (input[i+1] not in vowels) and (input[i+2] not in vowels) and (input[i+3] not in vowels)):
            return out
    return "NO"
if __name__ == '__main__':
    t = int(input())
    while(t):
        n = int(input())
        inp = input()
        print(fun10(inp))
        t-=1