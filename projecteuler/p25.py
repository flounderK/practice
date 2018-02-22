sequence = list()
sequence.append(1)
sequence.append(1)
fin = False
while not fin:
    sequence.append(sequence[-1] + sequence[-2])
    if len(str(sequence[-1])) >= 1000:
        fin = True

print(len(sequence))
