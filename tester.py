

for i in range(10):
    try:
        print(i)
        if i == 5:
            raise Exception()
    except:
        break