string = input("Harf tahlili qilmoqchi bo'lgan gapingizni yozing: ")
katta = 0
kichik = 0
for i in string:
    if i.isupper():
        katta += 1
    elif i.islower():
        kichik += 1
        
output = f"""Kutilayotgan natija: Katta harflar soni :{str(katta)} Kichik harflar soni :{str(kichik)}"""
print(output)