f = open('input.txt')
input = f.read()

coordinates = {}

x = 0
y = 0

for d in input:
	if d == "^":
		y += 1
		key = str( x ) + str( y )
		coordinates[key] = 1
	if d == "v":
		y -= 1
		key = str( x ) + str( y )
		coordinates[key] = 1
	if d == "<":
		x -= 1
		key = str( x ) + str( y )
		coordinates[key] = 1
	if d == ">":
		x += 1
		key = str( x ) + str( y )
		coordinates[key] = 1

print len( coordinates.keys() )