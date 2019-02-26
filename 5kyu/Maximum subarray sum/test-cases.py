test.describe("Tests")
test.it('should work on an empty array')   
test.assert_equals(maxSequence([]), 0)
test.it('should work on the example')
test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
test.it('should work on the example with negative numbers')
test.assert_equals(maxSequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
test.it('should work on random arrays')
from random import randint
def randomArray(size): return [randint(-30, 30) for i in range(0, size)]

def maxSequenceSol(arr):
	lowest = ans = total = 0
	for i in arr:
		total += i
		lowest = min(lowest, total)
		ans = max(ans, total - lowest)
	return ans
for i in range(50):
	ary = randomArray(50)
	test.assert_equals(maxSequence(ary[:]), maxSequenceSol(ary))
