from datetime import datetime
 
strkun = str(input('Birinchi sana: (yyyy-mm-dd): '))
strkun2 = str(input('Ikkinchi sana: (yyyy-mm-dd): '))
kundate = datetime.strptime(strkun, "%Y-%m-%d")
kundate2 = datetime.strptime(strkun2, "%Y-%m-%d")

print (f"Birinchi sanadan ikkinchi sanagacha {kundate2-kundate} kun o'tdi")


 
