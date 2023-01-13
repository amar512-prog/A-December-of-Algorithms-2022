
def fun6(i,inp_list,player,other):
    inp_list[0]-=1
    temp = inp_list[i]
    inp_list[i] = inp_list[0]
    inp_list[0] = temp
    if(inp_list[0]==0):
        return other+" wins the game!\n"+player+" loses the game!"
    return fun6(i,inp_list,player,other)
if __name__ == '__main__':
    position = int(input("Enter the position: "))-1
    numbers_str = input("Enter the set of numbers: ")
    l = list(map(int, numbers_str.split()))
    player = input("Enter the player going first: ")
    other = ""
    if player=="Tanika":
        other = "Bob"
    else:
        other ="Tanika"
    print(fun6(position,l,other,player))