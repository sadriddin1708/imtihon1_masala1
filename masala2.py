a = int(input("Birinchi son = "))
b = int(input("Ikkinchi son = "))

while a!=0 and b!=0 :
    if a > b:
        a = a % b
    else :
        b = b % a
print (f"EKUB = {a+b}")