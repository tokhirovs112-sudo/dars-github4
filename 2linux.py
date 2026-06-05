
with open('jsonfayl/matn.txt', 'r') as f:
    kontent = f.read()

soz = input("So'z kiriting: ")

if kontent.lower().find(soz.lower()) != -1:
    print("Siz kiritgan so'z faylda bor.")
else:
    print("Siz kiritgan so'z faylda yo'q.")