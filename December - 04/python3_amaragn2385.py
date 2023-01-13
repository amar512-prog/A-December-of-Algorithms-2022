def max_profit(stock_market):
    max_sum = max_start = max_end = 0
    current_sum = 0
    current_start = 0
    for i, value in enumerate(stock_market):
        if current_sum < 0:
            current_sum = value
            current_start = i
        else:
            current_sum += value
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = i
    return max_sum, max_start, max_end

if __name__ == '__main__':
    print("No. of Days: ",end='')
    n = int(input())
    print("Given stock market change values: ",end='')
    inp = input()
    stocks = list(map(int,inp.translate({ord(i): None for i in '{}'}).split(',')))
    profit, start_day, end_day = max_profit(stocks)
    print("Profit Value:", profit)
    print("Proposed days to sell: Day", start_day + 1, "to Day", end_day + 1)
    print("Stock market Change Values:", str(stocks[start_day:end_day + 1]).replace('[','{').replace(']','}'))

