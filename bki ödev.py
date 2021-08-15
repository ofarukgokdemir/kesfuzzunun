print("bki hesaplama aracına hoşgeldiniz")
boy = float(input("boyunuzu giriniz:"))
kilo = int(input("kilonuzu giriniz:"))

BKİ = kilo / boy ** boy

if BKİ < 18.5 :
    print("zayıf")
elif BKİ < 25 :
    print("normal")
elif BKİ < 30 :
    print("fazla kilolu")
else :
    print("obez")

input("helal")




