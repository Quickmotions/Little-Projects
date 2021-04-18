#FERGUS HAAK 18/04/21#
def card_hide(card):
	length = len(card)
	card = card[-4:]
	return card.rjust(length, '*')


answer = card_hide("20401284125325")
print(answer)
#censors the code only showing last 4 digitss