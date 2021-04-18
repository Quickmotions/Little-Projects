#FERGUS HAAK 18/04/21
def stutter(word):
	return word[0:2] + "..." + word[0:2] + "..." + word + "?"

word = input("word = ")
stutterword = stutter(word)
print(stutterword)