word_X = ['hello','world','my','name','is','Anna']
char = 'o'
hasO = []
for i in range(0,len(word_X)- 1):
	if char in word_X[i]:
		hasO.append(word_X[i])
print hasO