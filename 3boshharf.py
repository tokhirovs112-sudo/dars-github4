with open(r'jsonfayl\lll.txt', 'r') as f:
    k = f.read()

text = k.title()

with open(r'jsonfayl\soz.txt', 'w') as f:
    f.write(text)