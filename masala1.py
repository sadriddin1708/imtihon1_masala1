narx = int(input("Narx: "))
foiz = float(input("Yillik foiz stavkasini kiriting: "))
foiz = foiz / 100
yil = int(input("Necha yildan so'ng qaytarib mablag'ingizni olishingizni kiriting: "))
for i in range(0, yil):
    narx = narx + (narx * foiz)
print (f"{yil} yildan so'ng qaytarib oladigan summangiz : {narx} so'm")
    