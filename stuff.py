
def invert(number):
	if '-' in str(number):
		return float(str(number)[1:])
	else:
		return float('-'+str(number))
