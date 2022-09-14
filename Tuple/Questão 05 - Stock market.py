def stockmarket(stock):
    dic = {}
    for c in stock:
        #print(c[0])
        var1 = dic[c[0]] = c[1] * c[2]
        dic[c[0]] = c[1] * c[2]

    return (dic)


stock = [('24-Out-2020', 43.0, 25, 'NUB'),
('24-Out-2020', 20.0, 50, 'NUB'),
('25-Out-2020', 30.0, 75, 'ITU'),
('25-Out-2020', 35.0, 100, 'ITU')]
print(stockmarket(stock))