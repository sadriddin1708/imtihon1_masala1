royxat = [] 
n = int(input("n= "))
for i in range(0, n):
    son = int(input(f"{i+1}-sonni kiriting: "))
    royxat.append(son)
sararlash = list(filter(lambda x: x % 2 == 0, royxat))


print(f"Namuna roʻyxati : {str(royxat)} \nKutilayotgan natija: {str(sararlash)}")