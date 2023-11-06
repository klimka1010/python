for a in range(100):
    pod = True
    for x in range(100):
        for y in range(100):
            if ((x<a) or (y<a) or (x+2*y>50)) == False:
                pod = False

    if pod:
        print(a)
        break














# for a in range(0, 200):
#     pod = True
#     for x in range(0, 100):
#         for y in range(0, 100):
#             if ((x>=9) or (2*x<y) or (x*y<a)) == False:
#                 pod = False
#     if pod:
#         print(a)
