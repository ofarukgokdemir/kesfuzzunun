sayı1 = float(input("birinci sayıyı giriniz:"))
sayı2 = float(input("ikinci sayıyı giriniz:"))
sayı3 = float(input("üçüncü sayıyı giriniz:"))

if (sayı1>sayı2 and sayı1>sayı3):
    print("en büyük sayı",sayı1)
elif (sayı2>sayı3 and sayı2>sayı1):
    print("en büyük sayı", sayı2)
elif (sayı3>sayı1 and sayı3>sayı2):
    print("en büyük sayı",sayı3)


