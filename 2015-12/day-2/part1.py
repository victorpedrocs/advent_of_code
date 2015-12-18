f = open('input.txt')
sum = 0
for line in f:
    numbers = line.split('x')
    l = int(numbers[0])
    w = int(numbers[1])
    h = int(numbers[2])
    s = []
    s.append(l*w)
    s.append(w*h)
    s.append(h*l)
    smallest = s[0]
    for i in range(1,3):
        if( s[i] < smallest):
            smallest = s[i]
    sum += 2*l*w + 2*w*h + 2*h*l
    sum += smallest

print sum

