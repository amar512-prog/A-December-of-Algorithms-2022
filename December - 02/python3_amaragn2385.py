
def fun2(input):
    return (input[-4:-2]+input[:-4])

if __name__ == '__main__':
    inp = input()
    print(fun2(inp))