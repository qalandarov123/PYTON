##1
# def hisobla_daromad(kun):
#     kun = kun.lower()
#     oddiy_kun_daromad = 47 * 22000
#
#     if kun in ["shanba", "yakshanba"]:
#         daromad = 1.5 * oddiy_kun_daromad
#     else:
#         daromad = oddiy_kun_daromad
#     return round(daromad)
# kun_nomi = input("Hafta kunini kiriting (masalan, 'dushanba'): ")
# daromad = hisobla_daromad(kun_nomi)
#
# print(f"{kun_nomi.capitalize()} kuni daromad: {daromad} so'm")

##2
# qadamlar = 8200
# qadam_uzunligi = 0.7
#
# masofa_m = qadamlar * qadam_uzunligi
# masofa_km = masofa_m / 1000
#
# print(f"Farrux bugun jami {masofa_km:.2f} kilometr yo'l yurgan.")
#

##3
# chiroqlar_soni = 4
# chiroq_quvvati = 60
# yoqilgan_vaqt = 6
#
# umumiy_quvvat = chiroqlar_soni * chiroq_quvvati
# kunlik_energiya_vatt_soat = umumiy_quvvat * yoqilgan_vaqt
# kunlik_energiya_kvt_soat = kunlik_energiya_vatt_soat / 1000
#
# print(f"Dilnoza kuniga {kunlik_energiya_kvt_soat:.2f} kVt·soat elektr energiyasi sarflaydi.")

##4
# tort_soni = 3
#
# un_bitta = 450
# tuxum_bitta = 5
# shakar_bitta = 250
#
# un_jami = un_bitta * tort_soni
# tuxum_jami = tuxum_bitta * tort_soni
# shakar_jami = shakar_bitta * tort_soni
#
# print(f"3 ta tort uchun kerak bo'ladigan mahsulotlar:")
# print(f"Un: {un_jami} gramm")
# print(f"Tuxum: {tuxum_jami} dona")
# print(f"Shakar: {shakar_jami} gramm")


##5

# height = float(input("Bo'yingizni metrda kiriting (masalan, 1.75): "))
# weight = float(input("Vazningizni kilogrammda kiriting (masalan, 70): "))
#
#
# bmi = weight / (height ** 2)
#
# print(f"Sizning BMI ko'rsatkichingiz: {bmi:.2f}")
#
# if bmi < 18.5:
#     print("Siz ozg'insiz.")
# elif 18.5 <= bmi < 25:
#     print("Sizning vazningiz ideal.")
# elif 25 <= bmi < 30:
#     print("Sizda ortiqcha vazn mavjud.")
# else:
#     print("Sizda semizlik muammosi bor.")


##6
# initial = 1200
# rate = 0.988
# days = 10
#
# remaining = initial * (rate ** days)
# print(round(remaining, 1))


##7
# import math
# total_pages = 480
# daily_percent = 12
# daily_pages = total_pages * daily_percent / 100
# days_needed = math.ceil(total_pages / daily_pages)
# print(days_needed)


##8
# burchak = 0
# burchak -= 30
# burchak += 75
# kompas_burchagi = burchak % 360
# print("Yakuniy burchak:", kompas_burchagi, "daraja")


##9
# import math
# radius = 20
# n = 8
# s_per_person = math.pi * (radius ** 2) / n
# print("Har bir do'stga to'g'ri keladigan pitsa yuzasi:", round(s_per_person, 2), "kvadrat santimetr")

##10
# mahsulot1 = 12000
# mahsulot2 = 25000
# mahsulot3 = 9000
# umumiy_summa = mahsulot1 + mahsulot2 + mahsulot3
# if umumiy_summa > 40000:
#     chegirma = umumiy_summa * 0.10
#     yakuniy_summa = umumiy_summa - chegirma
#     print(" 10% chegirma qo'llanildi.")
#     print("Chegirma miqdori:", round(chegirma), "so'm")
# else:
#     yakuniy_summa = umumiy_summa
#     print(" Chegirma qo'llanilmadi.")
# print("Yakuniy to'lov summasi:", round(yakuniy_summa), "so'm")

#11
# a = float(input("Kub tomoni uzunligini kiriting (sm): "))
# V2 = a ** 3 * 1.008
# print(f"Muzning yangi hajmi: {V2:.3f} kub santimetr")

##12
# kundalik_soatlar = {
#     "Dushanba": 7.5,
#     "Seshanba": 7.5,
#     "Chorshanba": 7.5,
#     "Payshanba": 7.5,
#     "Juma": 3.75,
#     "Shanba": 0,
#     "Yakshanba": 0
# }
# jami_soatlar = sum(kundalik_soatlar.values())
# print("Anvar bir haftada jami", jami_soatlar, "soat ishlaydi.")


##13
# def hisobla_taksi_narxi(masofa):
#     minimal_tolov = 10000
#     qo‘shimcha_narx_har_km = 4000
#     if masofa <= 2:
#         return minimal_tolov
#     else:
#         ortiqcha_masofa = masofa - 2
#         qo‘shimcha_tolov = ortiqcha_masofa * qo‘shimcha_narx_har_km
#         umumiy_tolov = minimal_tolov + round(qo‘shimcha_tolov)
#         return int(umumiy_tolov)

##14
# **Tavsif:**
# Zargarlik do'konida turli xil oltin taqinchoqlar sotiladi. Bugungi kunda oltin juda qimmat - 1 gramm sof oltin 780 000 so'mdan baho berilmoqda
# Madina o'zi uchun chiroyli uzuk tanladi. Zargar aytishicha, uzuk 8.3 gramm sof oltindan tayyorlangan. Lekin uzuk tayyorlash uchun ustaning mehnat haqi ham to'lanadi - bu umumiy narxning 2% ini tashkil qiladi.
# Yakuniy narx qanday hisoblanadi?
# 1. Avval oltinning o'zi: 8.3 * 780 000
# 2. So'ng ustaga 2% qo'shimcha to'lov qo'shiladi
# Dastur yozing va uzukning yakuniy narxini ko'rsating.

##15
# import math
# def korinish_radiusini_hisobla(R=6371, h=550):
#     d = math.sqrt(2 * R * h + h ** 2)
#     return round(d, 2)
# print("XKS dan ko'rinadigan Yer radiusi:", korinish_radiusini_hisobla(), "km")

##16
# def quyosh_energiyasi(yuza_m2=12, quyosh_quvvati=800, foydalilik=0.18, soat=5):
#     umumiy_quvvat = quyosh_quvvati * yuza_m2
#     foydali_quvvat = umumiy_quvvat * foydalilik
#     energiya_kvt_soat = (foydali_quvvat * soat) / 1000
#     return round(energiya_kvt_soat, 2)
# print("Quyosh paneli ishlab chiqaradigan energiya:", quyosh_energiyasi(), "kVt·soat")

##17
# import math
# def robot_masofasi(a, b):
#     d = math.sqrt(a**2 + b**2)
#     return round(d, 2)
# a = float(input("a koordinatasini kiriting: "))
# b = float(input("b koordinatasini kiriting: "))
# natija = robot_masofasi(a, b)
# print(f"Robotning bosib o'tgan masofasi: {natija}")

##18
# P = 10_000_000
# r = 0.02
# n = 12
#
# S = P * (1 + r)**n
# print(f"12 oy oxirida jami summa: {S:.2f} so'm")


##19
# v_initial = 0
# v_final = 1000
# t_acceleration = 5
# t_total = 12
# a = (v_final - v_initial) / t_acceleration
# s = 0.5 * a * t_total**2
# print(f"Raketaning tezlanishi: {a} m/s^2")
# print(f"{t_total} soniya davomida bosib o'tilgan yo'l: {s} metr")

#20
# dollar = 1200
# kurs = 12560
# komissiya = 0.96
# soliq = 0.88
# som = dollar * kurs
# som_after_komissiya = som * komissiya
# som_after_soliq = som_after_komissiya * soliq
# print(f"Jahongir qo'liga sof: {som_after_soliq:.2f} so'm")


