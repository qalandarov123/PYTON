##1
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# summa = a + b
# print("Yig'indisi:", summa)


##2
# l = float(input("To‘rtburchakning uzunligini kiriting (l): "))
# w = float(input("To‘rtburchakning enini kiriting (w): "))
# area = l * w
# print("To‘rtburchakning yuzasi:", area)


##3
# x = float(input("Birinchi sonni kiriting (x): "))
# y = float(input("Ikkinchi sonni kiriting (y): "))
# z = float(input("Uchinchi sonni kiriting (z): "))
# avg = (x + y + z) / 3
# print("Arifmetik o‘rtacha:", avg)


#4
# a = float(input("To‘rtburchakning birinchi tomonini kiriting (a): "))
# b = float(input("To‘rtburchakning ikkinchi tomonini kiriting (b): "))
# p = 2 * (a + b)
# print("To‘g‘ri to‘rtburchakning perimetri:", p)

##5
# h = int(input("Soatni kiriting: "))
# m = int(input("Daqiqani kiriting: "))
# total_min = h * 60 + m
# print("Umumiy daqiqalar:", total_min)


##6
# usd = float(input("Dollar miqdorini kiriting: "))
# kurs = 11500
# sum = usd * kurs
# print(f"{usd} dollar = {sum} so'm")

##7
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# diff = abs(a - b)
# print("Ikki sonning modul farqi:", diff)


##8
# x = float(input("Asos x ni kiriting: "))
# n = int(input("Daraja n ni kiriting: "))
# power = x ** n
# print(f"{x} ning {n}-darajasi = {power}")


##9
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
# quotient = a // b
# remainder = a % b
# print(f"{a} // {b} = {quotient}")
# print(f"Qoldiq = {remainder}")


##10
# a = input("a ni kiriting: ")
# b = input("b ni kiriting: ")
# a, b = b, a
# print("Almashgandan keyingi qiymatlar:")
# print("a =", a)
# print("b =", b)





##11
# total_rent = float(input("Umumiy ijara to‘lovi (so‘m): "))
# n = int(input("Necha oyga bo‘lib to‘lash: "))
# per_month = total_rent / n
# print(f"Har oy to‘lanadigan summa: {per_month} so‘m")


##12
# d = float(input("Masofani kiriting (km): "))
# v = float(input("Tezlikni kiriting (km/soat): "))
# if v != 0:
#     time = d / v
#     print("Yo‘l bosib o‘tish vaqti:", time, "soat")
# else:
#     print("Tezlik 0 bo‘lishi mumkin emas.")

##13

# seats = int(input("Avtobusdagi o‘rinlar soni: "))
# passengers = int(input("Yo‘lovchilar soni: "))
# per_person = passengers // seats
# left = passengers % seats
# print("Har bir o‘ringa to‘g‘ri keladigan yo‘lovchilar soni:", per_person)
# print("Ortib qolgan yo‘lovchilar soni:", left)


##14
# consumption = float(input("100 km uchun yoqilg‘i sarfi (litr): "))
# d = float(input("Bosilgan masofa (km): "))
# fuel = consumption * d / 100
# print("Umumiy yoqilg‘i sarfi:", fuel, "litr")



##15
# salary = float(input("Brutto oylik maoshni kiriting: "))
# net = salary * (1 - 0.12)
# print("Netto maosh:", net)


##16
# amount = float(input("Hisob-kitob bo‘yicha summa (so‘m): "))
# days = int(input("Kechikish kunlari soni: "))
# penalty = amount * 0.001 * days
# total = amount + penalty
# print("Jami to‘lov:", total)


##17
# price = float(input("Mahsulot narxini kiriting: "))
# discount = float(input("Chegirma foizini kiriting (%): "))
# paid = price * (1 - discount / 100)
# print("To'lanadigan summa:", paid)



##18
# P = float(input("Asos (P) ni kiriting: "))
# r = float(input("Yillik foiz stavkasi (r) ni kiriting (%): "))
# t = float(input("Yillar (t) ni kiriting: "))
# interest = P * r / 100 * t
# total = P + interest
# print(f"Oddiy foiz: {interest}")
# print(f"Jami summa: {total}")


##19
# base_qty = float(input("Base miqdorini kiriting (grammda, 4 kishi uchun): "))
# people = int(input("Nechta kishi uchun retsept kerak: "))
# per_person = base_qty / 4
# needed = per_person * people
# print(f"{people} kishi uchun kerak bo'lgan miqdor: {needed} gramm")


##20
# bill = float(input("Hisob-kitob summasini kiriting (so'mda): "))
# tip = bill * 0.10
# total = bill + tip
# print(f"Tip: {tip} so'm")
# print(f"Jami summa: {total} so'm")
