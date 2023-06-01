for a in range(0,100):
    pod = True
    for x in range(0,100):
        for y in range(0,100):
            if ((x+y<=32) or (y<=x+4) or (y>=a)) == False:
                pod = False

    if pod:
        print(a)