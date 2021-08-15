print("****************Harf Notu Hesaplama Aracı*******************")

vize1 = int(input("vize1 notunuz:"))
vize2 = int(input("vize2 notunuz:"))
final = int(input("final notunuz:"))

toplam = vize1*30/100 + vize2*30/100 + final*40/100

if toplam >= 90:
    print("AA")
elif toplam >= 85:
    print("BA")
elif toplam >= 80:
    print("BB")
elif toplam >= 75:
    print("CB")
elif toplam >= 70:
    print("CC")
elif toplam >= 65:
    print("DC")
elif toplam >= 60:
    print("DD")
else :
    print("FF")


