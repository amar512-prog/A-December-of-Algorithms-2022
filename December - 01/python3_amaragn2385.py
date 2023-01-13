
def fun1(input):
    input_list = input.translate({ord(i): None for i in '{}'}).split(', ')
    return ''.join([chr(int(x, 16)) for x in input_list])
if __name__ == '__main__':
    t = int(input())
    while(t):
        inp = input()
        print(fun1(inp))
        t-=1