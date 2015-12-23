def getSmallest( a, b, c ):
	array = [a, b, c]
	sm1 = a
	for i in range(1,3):
		if array[i] < sm1:
			sm1 = array[i]
	array.remove(sm1)
	sm2 = array[0]
	if array[1] < array[0]:
		sm2 = array[1]

	return sm1, sm2


f = open('input.txt')
sum = 0
for line in f:
    numbers = line.split('x')
    l = int(numbers[0])
    w = int(numbers[1])
    h = int(numbers[2])
    a, b = getSmallest(l, w, h)
    sum += (a + a + b + b) + (l * w * h)

print sum 