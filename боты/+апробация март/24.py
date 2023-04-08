a = open('24.txt').readline()
a = a.replace('CFE', '*').replace('FCE', '*').replace('C', ' ').replace('F', ' ').replace('E', ' ')
print(max(len(s) for s in a.split()))
