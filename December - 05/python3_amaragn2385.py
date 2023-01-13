
def fun5(input):
    exp = 62*price+36
    return (exp,"EXPENDITURE WITHIN LIMIT") if exp<=5000 else (exp,"EXPENDITURE EXCEEDING LIMIT")


if __name__ == '__main__':
    print("fuel_price=",end='')
    price = int(input())
    expenditure,remark = fun5(price)
    print("Expenditure=", expenditure,sep='')
    print(remark)