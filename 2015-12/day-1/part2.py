f = open('input.txt', 'r')
text = f.read()
soma = 0
cont = 0
for c in text:
    cont += 1
    if c == '(':
        soma += 1
    elif c == ')':
        soma -= 1

    if soma < 0 :
        print "Basement: ", soma, "at", cont, "position"
        break
