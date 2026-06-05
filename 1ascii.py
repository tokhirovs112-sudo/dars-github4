with open(r'jsonfayl\input.txt', 'r') as f:
    k = f.read().strip()

numbers = k.split()
text = ''.join(chr(int(n)) for n in numbers)

with open(r'jsonfayl\output.txt', 'w') as f:
    f.write(text)