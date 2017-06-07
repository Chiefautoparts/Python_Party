'''words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
newWords = words.replace('day', 'month')
print newWords'''

'''x = [2,54,-2,7,12,98]
min = min(x)
max = max(x)
print min 
print max'''

'''x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]
newX = []
newX.append(x[0])
newX.append(x[-1])
print newX'''

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
halfX = x[:len(x)/2]
x = x[len(x)/2:]
#print halfX
x.insert(0,halfX)
print x