with open(r'jsonfayl\kkk.txt', 'r') as f:
    k = f.read()

numbers = list(map(int, k.split()))
ortacha = round(sum(numbers) / len(numbers))

with open(r'jsonfayl\sss.txt', 'w') as f:
    f.write(str(ortacha))