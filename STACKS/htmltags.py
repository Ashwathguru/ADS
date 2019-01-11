import LimitedStack
str1="<html>{Ashwath}(Fuck)[Dead]{}[]{()}"
def evaluateExp(str1):
	stk=LimitedStack.LimitedStack()
	lefty='{([<'
	righty='})]>'
	for ch in str1:
		if ch in lefty:
			stk.stackPush(ch)
		else:
			if ch in righty:
				if stk.isStackEmpty():
					return False
				if righty.index(ch)!=lefty.index(stk.stackPop()):
					return False
	return stk.isStackEmpty()

evaluateExp(str1)