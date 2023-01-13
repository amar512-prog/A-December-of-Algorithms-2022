
def find_word(word):
    for i in range(len(str_list)):
        for j in range(len(str_list[i])):
            if str_list[i][j] == word[0]:
                if check_horizontal(i, j, word) or check_vertical(i, j, word):
                    return True
    return False

def check_horizontal(i, j, word):
    if j + len(word) > len(str_list[i]):
        return False
    for k in range(len(word)):
        if str_list[i][j+k] != word[k]:
            return False
    return True

def check_vertical(i, j, word):
    if i + len(word) > len(str_list):
        return False
    for k in range(len(word)):
        if str_list[i+k][j] != word[k]:
            return False
    return True

str_list = ["ASSERTIVENESSLJ", "CFOGOODPOSITIVE", "OPENBMUREWOPRPS", "MEDIATIONELDIOG", "MAASREGJEWINWIN", 
            "UCIAEMOEECSKENI", "NEMRSHACDVTWTTL", "ITEHOTLTSTERAOE", "CASPLGLSIUNERFE", "AISAUSYTPOISEVF", 
            "TTARTTDOCENPPIH", "IOGAIGUPYMGOOEE", "OGEPOAFPQIENOWA", "NECONFLICTSDCER", "FNHTCATNOCEYEBT"]
if __name__ == '__main__':
    word = input()
    if find_word(word):
        print("Found")
    else:
        print("Not Found")

