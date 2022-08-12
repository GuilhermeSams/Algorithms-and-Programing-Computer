tweet = str(input())
censura = str(input())

if censura in tweet:
    x = tweet.replace(censura, "*")
    print(x)
else:
    print("tudo certo :)")
