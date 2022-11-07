from tkinter import E


pewaris = input("Pewaris : ")
harta = 0
suami = "0"
istri = 0
ayah = "0"
ibu = "0"
kakek = "0"
nenek = 0
anak_pr = 0
anak_lk = 0
cucu_pr = 0
cucu_lk = 0
saudari_knd = 0
saudara_knd = 0
saudari_sayah = 0
saudara_sayah = 0
saudari_sibu = 0
saudara_sibu = 0

if (pewaris == "istri" or pewaris == "ISTRI" or pewaris == "Istri" or pewaris == "2"):
    harta = int(input("Masukan Jumlah Harta : "))
    suami = str(input("Apakah memiliki suami? :"))
elif (pewaris == "suami" or pewaris == "SUAMI" or pewaris == "Suami" or pewaris == "1"):
    harta = int(input("Masukan Jumlah Harta : "))
    istri = int(input("Masukan Jumlah Istri : "))
else:
    print("Maaf, anda diwajibkan mengisi Muwwarits!")
    exit()
anak_pr = int(input("Masukan Jumlah anak perempuan kandung : "))
anak_lk = int(input("Masukan Jumlah anak laki-laki kandung : "))
ayah = str(input("apakah memiliki ayah kandung? : "))
ibu = str(input("apakah memiliki ibu kndung? : "))
kakek = str(input("apakah memiliki kakek? : "))
nenek = int(input("Masukan Jumlah nenek? : "))
cucu_pr = int(
    input("Masukan Jumlah cucu perempuan dari turunan anak laki-laki : "))
cucu_lk = int(
    input("Masukan Jumlah cucu laki-laki dari turunan anak laki-laki : "))
saudari_knd = int(input("Masukan Jumlah saudari kandung : "))
saudara_knd = int(input("Masukan Jumlah saudara kandung : "))
saudari_sayah = int(input("Masukan Jumlah saudari seayah : "))
saudara_sayah = int(input("Masukan Jumlah saudara seayah : "))
saudari_sibu = int(input("Masukan Jumlah saudari seibu : "))
saudara_sibu = int(input("Masukan Jumlah saudara seibu : "))
########################################SUAMI####################################################
if (pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
    if (suami == "y"):
        if (anak_pr == 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk == 0):
            bagiansuami = 0.5
            print(f"Bagian suami {bagiansuami}")
        elif (anak_pr > 0 or anak_lk > 0 or cucu_pr > 0 or cucu_lk > 0):
            bagiansuami = 0.25
            print(f"Bagian suami {bagiansuami}")
    else:
        bagiansuami = 0
#################################################################################################
elif (pewaris == "suami" or pewaris == "Suami" or pewaris == "SUAMI" or pewaris == "1"):
    if (istri == 0):
        bagianIstri = 0
    else:
        if (anak_pr == 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk == 0):
            bagianIstri = 0.25
            print(f"Bagian Istri {bagianIstri}")
        elif (anak_pr > 0 or anak_lk > 0 or cucu_pr > 0 or cucu_lk > 0):
            bagianIstri = 0.125
            print(f"Bagian Istri {bagianIstri}")
############################# ANAK PEREMPUAN $ ANAK LAKI-LAKI ######################################################
if (anak_pr == 1 and anak_lk == 0):
    bagiananak_pr = 0.5
    print(f"Bagian anak perempuan {bagiananak_pr}")
elif (anak_pr > 1 and anak_lk == 0):
    bagiananak_pr = 0.6
    print(f"Bagian anak perempuan {bagiananak_pr}")
elif (anak_pr > 0 and anak_lk > 0):
    bagiananak_pr = "sisa"
    bagiananak_lk = "sisa"
    print(f"Bagian anak perempuan {bagiananak_pr}")
    print(f"Bagian anak laki-laki {bagiananak_lk}")
elif (anak_lk >= 1):
    bagiananak_lk = "sisa"
    print(f"Bagian anak laki-laki {bagiananak_lk}")
############################ AYAH #################################################################
if (ayah == "y" or ayah == "ada"):
    if (anak_pr == 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk == 0):
        bagianayah = "sisa"
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr == 0 and anak_lk == 0 and cucu_pr > 0 and cucu_lk > 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr == 0 and anak_lk > 0 and cucu_pr > 0 and cucu_lk == 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr == 0 and anak_lk > 0 and cucu_pr == 0 and cucu_lk > 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr == 0 and anak_lk > 0 and cucu_pr == 0 and cucu_lk == 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr == 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk > 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr == 0 and anak_lk > 0 and cucu_pr > 0 and cucu_lk > 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr == 0 and anak_lk == 0 and cucu_pr > 0 and cucu_lk == 0):
        bagianayah = 0.16
        bagiansisa = "+sisa"
        print(f"Bagian ayah {bagianayah} {bagiansisa}")
    elif (anak_pr > 0 and anak_lk == 0 and cucu_pr > 0 and cucu_lk == 0):
        bagianayah = 0.16
        bagiansisa = "+sisa"
        print(f"Bagian ayah {bagianayah} {bagiansisa}")
    elif (anak_pr > 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk == 0):
        bagianayah = 0.16
        bagiansisa = "+sisa"
        print(f"Bagian ayah {bagianayah} {bagiansisa}")
    elif (anak_pr > 0 and anak_lk > 0 and cucu_pr > 0 and cucu_lk > 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr > 0 and anak_lk > 0 and cucu_pr == 0 and cucu_lk == 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr > 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk > 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr > 0 and anak_lk > 0 and cucu_pr > 0 and cucu_lk == 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr > 0 and anak_lk == 0 and cucu_pr > 0 and cucu_lk > 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr == 0 and anak_lk > 0 and cucu_pr > 0 and cucu_lk > 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
    elif (anak_pr > 0 and anak_lk > 0 and cucu_pr == 0 and cucu_lk > 0):
        bagianayah = 0.16
        bagiansisa = ""
        print(f"Bagian ayah {bagianayah}")
else:
    bagianayah = 0
    # print(f"Bagian ayah {bagianayah}")
############################### KAKEK #################################################################
if (bagianayah == 0):
    if (kakek == "y"):
        if (anak_pr == 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk == 0):
            bagiankakek = "sisa"
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr == 0 and anak_lk == 0 and cucu_pr > 0 and cucu_lk > 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr == 0 and anak_lk > 0 and cucu_pr > 0 and cucu_lk == 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr == 0 and anak_lk > 0 and cucu_pr == 0 and cucu_lk > 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr == 0 and anak_lk > 0 and cucu_pr == 0 and cucu_lk == 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr == 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk > 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr == 0 and anak_lk > 0 and cucu_pr > 0 and cucu_lk > 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr == 0 and anak_lk == 0 and cucu_pr > 0 and cucu_lk == 0):
            bagiankakek = 0.16
            bagiansisakakek = "+sisa"
            print(f"Bagian kakek {bagiankakek} {bagiansisakakek}")
        elif (anak_pr > 0 and anak_lk == 0 and cucu_pr > 0 and cucu_lk == 0):
            bagiankakek = 0.16
            bagiansisakakek = "+sisa"
            print(f"Bagian kakek {bagiankakek} {bagiansisakakek}")
        elif (anak_pr > 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk == 0):
            bagiankakek = 0.16
            bagiansisakakek = "+sisa"
            print(f"Bagian kakek {bagiankakek} {bagiansisakakek}")
        elif (anak_pr > 0 and anak_lk > 0 and cucu_pr > 0 and cucu_lk > 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr > 0 and anak_lk > 0 and cucu_pr == 0 and cucu_lk == 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr > 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk > 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr > 0 and anak_lk > 0 and cucu_pr > 0 and cucu_lk == 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr > 0 and anak_lk == 0 and cucu_pr > 0 and cucu_lk > 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr == 0 and anak_lk > 0 and cucu_pr > 0 and cucu_lk > 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
        elif (anak_pr > 0 and anak_lk > 0 and cucu_pr == 0 and cucu_lk > 0):
            bagiankakek = 0.16
            bagiansisakakek = ""
            print(f"Bagian kakek {bagiankakek}")
    else:
        bagiankakek = 0
else:
    bagiankakek = 0
######################### IBU ##################################################################################################
if (ibu == "y" or ibu == "ada"):
    if (anak_pr == 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk == 0 and saudari_knd == 0 and saudara_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
        bagianibu = "0.33"
        bagiansisaibu = "*sisa"
        print(f"Bagian ibu {bagianibu} {bagiansisaibu}")
    elif (anak_pr > 0 or anak_lk > 0 or cucu_pr > 0 or cucu_lk > 0 or saudari_knd > 0 or saudara_knd > 0 or saudari_sayah > 0 or saudara_sayah > 0 or saudari_sibu > 0 or saudara_sibu > 0):
        bagianibu = 0.16
        bagiansisaibu = ""
        print(f"Bagian ibu {bagianibu}")
    if (nenek < 3 and nenek != 0):
        if (ibu == "y" or ibu == "ada"):
            bagiannenek = "termahjub"
            print(f"bagian nenek  {bagiannenek}")
else:
    bagianibu = 0
    bagiannenek = 0
############################### NENEK #####################################################################
    if (bagianibu == 0):
        if (nenek > 0):
            bagiannenek = 0.16
            print(f"bagian nenek  {bagiannenek}")
################################ CUCU PEREMPUAN & CUCU LAKI-LAKI ################################################################
if (cucu_pr >= 1 and cucu_lk >= 1):
    if (anak_pr == 0 and anak_lk >= 1):
        bagiancucupr = "termahjub"
        print(f"bagian cucu perempuan {bagiancucupr}")
        bagiancuculk = "termahjub"
        print(f"bagian cucu laki-laki {bagiancuculk}")
    elif (anak_pr > 1 and anak_lk == 0):
        bagiancucupr = "termahjub"
        print(f"bagian cucu perempuan {bagiancucupr}")
        bagiancuculk = "sisa"
        print(f"bagian cucu laki-laki {bagiancuculk}")
    elif (anak_pr == 0 and anak_lk == 0):
        bagiancucupr = "sisa"
        bagiancuculk = "sisa"
        print(f"bagian cucu perempuan {bagiancucupr}")
        print(f"bagian cucu laki-laki {bagiancuculk}")
    elif (anak_pr == 1 and anak_lk == 0):
        bagiancucupr = "sisa"
        bagiancuculk = "sisa"
        print(f"bagian cucu perempuan {bagiancucupr}")
        print(f"bagian cucu laki-laki {bagiancuculk}")
    elif (anak_pr > 0 and anak_lk > 0):
        bagiancucupr = "termahjub"
        bagiancuculk = "termahjub"
        print(f"bagian cucu perempuan {bagiancucupr}")
        print(f"bagian cucu laki-laki {bagiancuculk}")
elif (cucu_pr == 0 and cucu_lk >= 1):
    if (anak_lk >= 1 and anak_pr == 0):
        bagiancuculk = "termahjub"
        print(f"bagian cucu laki-laki {bagiancuculk}")
    elif (anak_lk == 0 and anak_pr == 0):
        bagiancuculk = "sisa"
        print(f"bagian cucu laki-laki {bagiancuculk}")
    elif (anak_pr >= 1 and anak_lk == 0):
        bagiancuculk = "sisa"
        print(f"bagian cucu laki-laki {bagiancuculk}")
elif (cucu_pr == 1 and cucu_lk == 0):
    if (anak_lk == 0 and anak_pr == 0):
        bagiancucupr = 0.5  # 1/2
        print(f"bagian cucu perempuan {bagiancucupr}")
    elif (anak_lk >= 1 and anak_pr == 0):
        bagiancucupr = 0.5  # 1/2
        print(f"bagian cucu perempuan {bagiancucupr}")
    elif (anak_lk == 0 and anak_pr == 1):
        bagiancucupr = 0.16  # 1/6
        print(f"bagian cucu perempuan {bagiancucupr}")
    elif (anak_lk == 0 and anak_pr > 1):
        bagiancucupr = "termahjub"
        print(f"bagian cucu perempuan {bagiancucupr}")
elif (cucu_pr > 1 and cucu_lk == 0):
    if (anak_lk >= 1 and anak_pr == 0):
        bagiancucupr = "termahjub"
        print(f"bagian cucu perempuan {bagiancucupr}")
    elif (anak_lk == 0 and anak_pr == 0):
        bagiancucupr = 0.6  # 2/3
        print(f"bagian cucu perempuan {bagiancucupr}")
    elif (anak_lk == 0 and anak_pr == 1):
        bagiancucupr = 0.16  # 1/6
        print(f"bagian cucu perempuan {bagiancucupr}")
    elif (anak_lk == 0 and anak_pr > 1):
        bagiancucupr = "termahjub"
        print(f"bagian cucu perempuan {bagiancucupr}")
###################### SAUDARI KANDUNG #######################################################
if (ayah == "0" and kakek == "0" and anak_lk == 0 and cucu_lk == 0):
    if (saudari_knd > 0 and saudara_knd > 0):
        bagiansaudariknd = "sisa"
        bagiansaudaraknd = "sisa"
        print(f"bagian Saudari kandung {bagiansaudariknd}")
        print(f"bagian Saudara kandung {bagiansaudaraknd}")
    elif (saudari_knd == 1 and saudara_knd == 0):
        if (anak_pr == 0 and cucu_pr == 0):
            bagiansaudariknd = 0.5  # 1/2
            print(f"bagian Saudari kandung {bagiansaudariknd}")
        elif (anak_pr >= 1 and cucu_pr == 0):
            bagiansaudariknd = "sisa"
            print(f"bagian Saudari kandung {bagiansaudariknd}")
        elif (anak_pr == 0 and cucu_pr >= 1):
            bagiansaudariknd = "sisa"
            print(f"bagian Saudari kandung {bagiansaudariknd}")
        elif (anak_pr >= 1 and cucu_pr >= 1):
            bagiansaudariknd = "sisa"
            print(f"bagian Saudari kandung {bagiansaudariknd}")
    elif (saudari_knd > 1 and saudara_knd == 0):
        if (anak_pr == 0 and cucu_pr == 0):
            bagiansaudariknd = 0.6  # 2/3
            print(f"bagian Saudari kandung {bagiansaudariknd}")
        elif (anak_pr == 1 and cucu_pr == 1):
            bagiansaudariknd = "sisa"
            print(f"bagian Saudari kandung {bagiansaudariknd}")
        elif (anak_pr >= 1 and cucu_pr == 0):
            bagiansaudariknd = "sisa"
            print(f"bagian Saudari kandung {bagiansaudariknd}")
        elif (anak_pr == 0 and cucu_pr >= 1):
            bagiansaudariknd = "sisa"
            print(f"bagian Saudari kandung {bagiansaudariknd}")
        elif (anak_pr >= 1 and cucu_pr >= 1):
            bagiansaudariknd = "sisa"
            print(f"bagian Saudari kandung {bagiansaudariknd}")
    elif (saudari_knd == 0 and saudara_knd > 0):
        if (anak_pr > 0 and cucu_pr > 0):
            bagiansaudaraknd = "sisa"
            print(f"bagian saudara kandung {bagiansaudaraknd}")
        elif (anak_pr == 0 and cucu_pr > 0):
            bagiansaudaraknd = "sisa"
            print(f"bagian saudara kandung {bagiansaudaraknd}")
        elif (anak_pr > 0 and cucu_pr == 0):
            bagiansaudaraknd = "sisa"
            print(f"bagian saudara kandung {bagiansaudaraknd}")
        elif (anak_pr == 0 and cucu_pr == 0):
            bagiansaudaraknd = "sisa"
            print(f"bagian saudara kandung {bagiansaudaraknd}")
elif (ayah == "y" or kakek == "y" or anak_lk > 0 or cucu_lk > 0):
    if (saudari_knd > 0 and saudara_knd > 0):
        bagiansaudariknd = "termahjub"
        bagiansaudaraknd = "termahjub"
        print(f"bagian Saudari kandung {bagiansaudariknd}")
        print(f"bagian Saudara kandung {bagiansaudaraknd}")
    elif (saudari_knd > 0 and saudara_knd == 0):
        bagiansaudariknd = "termahjub"
        print(f"bagian Saudari kandung {bagiansaudariknd}")
    elif (saudari_knd == 0 and saudara_knd > 0):
        bagiansaudaraknd = "termahjub"
        print(f"bagian Saudara kandung {bagiansaudaraknd}")
# elif (ayah == "0" and kakek == "0" and anak_lk == 0 and cucu_lk > 0):
#     if (saudari_knd > 0 and saudara_knd > 0):
#         bagiansaudariknd = "termahjub"
#         bagiansaudaraknd = "termahjub"
#         print(f"bagian Saudari kandung {bagiansaudariknd}")
#         print(f"bagian Saudara kandung {bagiansaudaraknd}")
#     elif (saudari_knd > 0 and saudara_knd == 0):
#         bagiansaudariknd = "termahjub"
#         print(f"bagian Saudari {bagiansaudariknd}")
#     elif (saudari_knd == 0 and saudara_knd > 0):
#         bagiansaudaraknd = "termahjub"
#         print(f"bagian Saudara kandung {bagiansaudaraknd}")
# elif (ayah == "0" and kakek == "0" and anak_lk > 0 and cucu_lk > 0):
#     if (saudari_knd > 0 and saudara_knd > 0):
#         bagiansaudariknd = "termahjub"
#         bagiansaudaraknd = "termahjub"
#         print(f"bagian Saudari kandung {bagiansaudariknd}")
#         print(f"bagian Saudara kandung {bagiansaudaraknd}")
#     elif (saudari_knd > 0 and saudara_knd == 0):
#         bagiansaudariknd = "termahjub"
#         print(f"bagian Saudari kandung {bagiansaudariknd}")
#     elif (saudari_knd == 0 and saudara_knd > 0):
#         bagiansaudaraknd = "termahjub"
#         print(f"bagian Saudara kandung {bagiansaudaraknd}")
# elif (ayah == "y" and kakek == "y" and anak_lk > 0 and cucu_lk > 0):
#     if (saudari_knd > 0 and saudara_knd > 0):
#         bagiansaudariknd = "termahjub"
#         bagiansaudaraknd = "termahjub"
#         print(f"bagian Saudari kandung {bagiansaudariknd}")
#         print(f"bagian Saudara kandung {bagiansaudaraknd}")
#     elif (saudari_knd > 0 and saudara_knd == 0):
#         bagiansaudariknd = "termahjub"
#         print(f"bagian Saudari kandung {bagiansaudariknd}")
#     elif (saudari_knd == 0 and saudara_knd > 0):
#         bagiansaudaraknd = "termahjub"
#         print(f"bagian Saudara kandung {bagiansaudaraknd}")

###################################### SAUDARI SEAYAH ##############################################################
if (ayah == "0" and kakek == "0" and anak_lk == 0 and cucu_lk == 0 and saudara_knd == 0):
    if (saudari_sayah > 0 and saudara_sayah > 0 and saudari_knd == 0):
        if (anak_pr >= 1 and cucu_pr >= 1):
            bagiansaudarisayah = "sisa"
            bagiansaudarasayah = "sisa"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
            print(f"bagian Saudara seyah 1 {bagiansaudarasayah}")
        elif (anak_pr >= 1 and cucu_pr == 0):
            bagiansaudarisayah = "sisa"
            bagiansaudarasayah = "sisa"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
            print(f"bagian Saudara seyah 2 {bagiansaudarasayah}")
        elif (anak_pr == 0 and cucu_pr >= 1):
            bagiansaudarisayah = "sisa"
            bagiansaudarasayah = "sisa"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
            print(f"bagian Saudara seayah 3 {bagiansaudarasayah}")
        elif (anak_pr == 0 and cucu_pr == 0):
            bagiansaudarisayah = "sisa"
            bagiansaudarasayah = "sisa"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
            print(f"bagian Saudara seyah 4 {bagiansaudarasayah}")
    elif (saudari_sayah > 0 and saudara_sayah > 0 and saudari_knd >= 1):
        if (anak_pr >= 1 and cucu_pr >= 1):
            bagiansaudarisayah = "termahjub"
            bagiansaudarasayah = "termahjub"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
            print(f"bagian Saudara seyah 1 {bagiansaudarasayah}")
        elif (anak_pr >= 1 and cucu_pr == 0):
            bagiansaudarisayah = "termahjub"
            bagiansaudarasayah = "termahjub"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
            print(f"bagian Saudara seyah 2 {bagiansaudarasayah}")
        elif (anak_pr == 0 and cucu_pr >= 1):
            bagiansaudarisayah = "termahjub"
            bagiansaudarasayah = "termahjub"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
            print(f"bagian Saudara seayah 3 {bagiansaudarasayah}")
        elif (anak_pr == 0 and cucu_pr == 0):
            bagiansaudarisayah = "termahjub"
            bagiansaudarasayah = "termahjub"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
            print(f"bagian Saudara seyah 4 {bagiansaudarasayah}")
    elif (saudari_sayah == 1 and saudara_sayah == 0 and saudari_knd == 0):
        if (anak_pr == 0 and cucu_pr == 0):
            bagiansaudarisayah = 0.5  # 1/2
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
        elif (anak_pr >= 1 and cucu_pr >= 1):
            bagiansaudarisayah = 0.5  # 1/2
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
        elif (anak_pr >= 1 and cucu_pr == 0):
            bagiansaudarisayah = 0.5  # 1/2
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
        elif (anak_pr == 0 and cucu_pr >= 1):
            bagiansaudarisayah = 0.5  # 1/2
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
    elif (saudari_sayah > 1 and saudara_sayah == 0 and saudari_knd == 0):
        if (anak_pr == 0 and cucu_pr == 0):
            bagiansaudarisayah = 0.6  # 2/3
            print(f"bagian Saudari seayah{bagiansaudarisayah}")
        elif (anak_pr >= 1 and cucu_pr >= 1):
            bagiansaudarisayah = 0.6  # 2/3
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
        elif (anak_pr >= 1 and cucu_pr == 0):
            bagiansaudarisayah = 0.6  # 2/3
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
        elif (anak_pr == 0 and cucu_pr >= 1):
            bagiansaudarisayah = 0.6  # 2/3
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
    elif (saudari_sayah >= 1 and saudara_sayah == 0 and saudari_knd == 1):
        if (anak_pr == 0 and cucu_pr == 0):
            bagiansaudarisayah = 0.16  # 1/6
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
        elif (anak_pr >= 1 and cucu_pr >= 1):
            bagiansaudarisayah = "termahjub"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
        elif (anak_pr >= 1 and cucu_pr == 0):
            bagiansaudarisayah = "termahjub"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
        elif (anak_pr == 0 and cucu_pr >= 1):
            bagiansaudarisayah = "termahjub"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
    elif (saudari_sayah >= 1 and saudara_sayah == 0 and saudari_knd > 1):
        if (anak_pr >= 0 and cucu_pr >= 0):
            bagiansaudarisayah = "termahjub"
            print(f"bagian Saudari seayah {bagiansaudarisayah}")
    ######### SAUDARA SEAYAH ############################
    elif (saudari_sayah == 0 and saudara_sayah >= 1 and saudari_knd == 0):
        if (anak_pr >= 1 and cucu_pr >= 1):
            bagiansaudarasayah = "sisa"
            print(f"bagian Saudara seayah a {bagiansaudarasayah}")
        elif (anak_pr >= 1 and cucu_pr == 0):
            bagiansaudarasayah = "sisa"
            print(f"bagian Saudara seayah b {bagiansaudarasayah}")
        elif (anak_pr == 0 and cucu_pr >= 1):
            bagiansaudarasayah = "sisa"
            print(f"bagian Saudara seayah c {bagiansaudarasayah}")
        elif (anak_pr == 0 and cucu_pr == 0):
            bagiansaudarasayah = "sisa"
            print(f"bagian Saudara seayah c {bagiansaudarasayah}")
    elif (saudari_sayah == 0 and saudara_sayah >= 1 and saudari_knd >= 1):
        if (anak_pr >= 1 and cucu_pr >= 1):
            bagiansaudarasayah = "termahjub"
            print(f"bagian saudara seayah {bagiansaudarasayah}")
        if (anak_pr == 0 and cucu_pr == 0):
            bagiansaudarasayah = "sisa"
            print(f"bagian saudara seayah {bagiansaudarasayah}")
        elif (anak_pr >= 1 and cucu_pr == 0):
            bagiansaudarasayah = "termahjub"
            print(f"bagian saudara seayah {bagiansaudarasayah}")
        if (anak_pr == 0 and cucu_pr >= 1):
            bagiansaudarasayah = "termahjub"
            print(f"bagian saudara seayah {bagiansaudarasayah}")
    # elif (saudari_sayah >= 1 and saudara_sayah >= 1 and saudari_knd == 0):
    #     if (anak_pr >= 1 and cucu_pr >= 1):
    #         bagiansaudarisayah = "sisa"
    #         bagiansaudarasayah = "sisa"
    #         print(f"bagian saudari seayah {bagiansaudarisayah}")
    #         print(f"bagian saudara seayah {bagiansaudarasayah}")
    #     elif (anak_pr >= 1 and cucu_pr == 0):
    #         bagiansaudarisayah = "sisa"
    #         bagiansaudarasayah = "sisa"
    #         print(f"bagian saudari seayah {bagiansaudarisayah}")
    #         print(f"bagian saudara seayah {bagiansaudarasayah}")
    #     elif (anak_pr == 0 and cucu_pr >= 1):
    #         bagiansaudarisayah = "sisa"
    #         bagiansaudarasayah = "sisa"
    #         print(f"bagian saudari seayah {bagiansaudarisayah}")
    #         print(f"bagian saudara seayah {bagiansaudarasayah}")
    #     elif (anak_pr == 0 and cucu_pr == 0):
    #         bagiansaudarisayah = "sisa"
    #         bagiansaudarasayah = "sisa"
    #         print(f"bagian saudari seayah {bagiansaudarisayah}")
    #         print(f"bagian saudara seayah {bagiansaudarasayah}")
elif (ayah == "y" or kakek == "y" or anak_lk >= 1 or cucu_lk >= 1 or saudara_knd >= 1):
    if (saudari_sayah >= 1 and saudara_sayah >= 1):
        bagiansaudarisayah = "termahjub"
        bagiansaudarasayah = "termahjub"
        print(f"bagian saudari seayah 1 {bagiansaudarisayah}")
        print(f"bagian saudara seayah 1 {bagiansaudarasayah}")
    elif (saudari_sayah >= 1 and saudara_sayah == 0):
        bagiansaudarisayah = "termahjub"
        print(f"bagian saudari seayah {bagiansaudarisayah}")
    elif (saudari_sayah == 0 and saudara_sayah >= 1):
        bagiansaudarasayah = "termahjub"
        print(f"bagian saudara seayah {bagiansaudarasayah}")
###################################### SAUDARI SEIBU ##############################################################
if (ayah == "0" and kakek == "0" and anak_pr == 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk == 0):
    if (saudari_sibu > 1 and saudara_sibu > 1):
        bagiansaudarisibu = 0.3
        bagiansaudarasibu = 0.3
        print(f"bagian saudari seibu {bagiansaudarisibu}")
        print(f"bagian saudara seibu {bagiansaudarasibu}")
    elif (saudari_sibu == 1 and saudara_sibu == 1):
        bagiansaudarisibu = 0.16
        bagiansaudarasibu = 0.16
        print(f"bagian saudari seibu - {bagiansaudarisibu}")
        print(f"bagian saudara seibu - {bagiansaudarasibu}")
    elif (saudari_sibu == 1 and saudara_sibu > 1):
        bagiansaudarisibu = 0.16
        bagiansaudarasibu = 0.3
        print(f"bagian saudari seibu {bagiansaudarisibu}")
        print(f"bagian saudara seibu {bagiansaudarasibu}")
    elif (saudari_sibu > 1 and saudara_sibu == 1):
        bagiansaudarisibu = 0.3
        bagiansaudarasibu = 0.16
        print(f"bagian saudari seibu {bagiansaudarisibu}")
        print(f"bagian saudara seibu {bagiansaudarasibu}")
    elif (saudari_sibu == 0 and saudara_sibu == 1):
        bagiansaudarasibu = 0.16
        print(f"bagian saudara seibu {bagiansaudarasibu}")
    elif (saudari_sibu == 0 and saudara_sibu > 1):
        bagiansaudarasibu = 0.3
        print(f"bagian saudara seibu {bagiansaudarasibu}")
    elif (saudari_sibu == 1 and saudara_sibu == 0):
        bagiansaudarisibu = 0.16
        print(f"bagian saudari seibu + {bagiansaudarisibu}")
    elif (saudari_sibu > 1 and saudara_sibu == 0):
        bagiansaudarisibu = 0.3
        print(f"bagian saudari seibu {bagiansaudarisibu}")
elif (ayah == "y" or kakek == "y" or anak_pr >= 0 or anak_lk >= 0 or cucu_pr >= 0 or cucu_lk >= 0):
    if (saudari_sibu >= 1 and saudara_sibu >= 1):
        bagiansaudarisibu = "termahjub"
        bagiansaudarasibu = "teermahjub"
        print(f"bagian saudari seibu {bagiansaudarisibu}")
        print(f"bagian saudara seibu  1 {bagiansaudarasibu}")
    elif (saudari_sibu >= 1 and saudara_sibu == 0):
        bagiansaudarisibu = "termahjub"
        print(f"bagian saudari seibu  {bagiansaudarisibu}")
    elif (saudari_sibu == 0 and saudara_sibu >= 1):
        bagiansaudarasibu = "termahjub"
        print(f"bagian saudara seibu 2 {bagiansaudarasibu}")

##################### Asal Masalah #################################
asalmasalah = 0

# pembagian asal masalah
if (pewaris == "suami" or pewaris == "Suami" or pewaris == "1" or pewaris == "SUAMI"):
    if (bagianIstri == 0.125):
        if (ayah == "0" and kakek == "0" and anak_lk == 0 and cucu_lk == 0):
                asalmasalah = 8
        else:
            if(ayah == "0" and ibu == "0" and kakek == "0" and nenek == 0):
                if(cucu_lk > 0 and anak_pr > 1):
                    asalmasalah = 24
                else:
                    asalmasalah = 8
            else:
                asalmasalah = 24
    elif (bagianIstri == 0.25):
        if(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
            print("Asal Masalah Awal 4 Menjadi ", asalmasalah)
        elif(kakek == "y" and nenek > 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 12
        else:
            if(ayah == "y" and nenek > 0 and kakek == "0" and ibu == "0"):
                asalmasalah = 12
            else:
                asalmasalah = 4
    elif (istri == 0 and bagianIstri == 0):
        if(kakek == "0" and nenek == 0 and ayah == "y" and ibu == "y" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 3
        # ayah
        elif(kakek == "0" and nenek == 0 and ayah == "y" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
        # ibu
        elif(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "y" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
        # kakek
        elif(kakek == "y" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
        # nenek
        elif(kakek == "0" and nenek > 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
        # cucupr
        elif(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr > 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah_cucupr = (1 * cucu_pr)
            asalmasalah = asalmasalah_cucupr
        # cuculk
        elif(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk > 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah_cuculk = (1 * cucu_lk)
            asalmasalah = asalmasalah_cuculk
        # cuculk and cucu pr
        elif(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk > 0 and cucu_pr > 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudara_sibu == 0 and saudara_sibu == 0):
            asalmasalah_cucupr = (1 * cucu_pr)
            asalmasalah_cuculk = (2 * cucu_lk)
            asalmasalah = asalmasalah_cucupr + asalmasalah_cuculk
        # batas
        elif(kakek == "y" and nenek > 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 6
        elif(kakek == "y" and nenek == 0 and ayah == "0" and ibu == "y" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 3
        elif(kakek == "0" and nenek > 0 and ayah == "y" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 6 
        elif(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr >= 0 and anak_lk >= 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudara_sibu == 0 and saudara_sibu == 0):
            if(anak_pr > 0 and anak_lk == 0):
                asalmasalah_anakpr = (1 * anak_pr)
                asalmasalah = asalmasalah_anakpr
            elif(anak_pr == 0 and anak_lk > 0):
                asalmasalah_anaklk = (1 * anak_lk)
                asalmasalah = asalmasalah_anaklk
            elif(anak_pr > 0 and anak_lk > 0):
                asalmasalah_anakpr = (1 * anak_pr)
                asalmasalah_anaklk = (2 * anak_lk)
                asalmasalah = asalmasalah_anakpr + asalmasalah_anaklk
        else:
            asalmasalah = 6
elif (pewaris == "istri" or pewaris == "Istri" or pewaris == "2" or pewaris == "ISTRI"):
    if (bagiansuami == 0.5):
        if(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
            print("Asal Masalah Awal 2 Menjadi ", asalmasalah)
        elif(kakek == "y" and nenek > 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 6
        else:
            if(ayah == "y" and nenek > 0 and kakek == "0" and ibu == "0"):
                asalmasalah = 6
            else:
                asalmasalah = 2
    elif (bagiansuami == 0.25):
        # old
        # if(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0"):
        #     if(anak_pr > 1):
        #         asalmasalah = 12
        #     else:
        #         asalmasalah = 4
        # else:
        #     asalmasalah = 12
        if (ayah == "0" and kakek == "0" and anak_lk == 0):
            if(ibu == "y" and anak_pr > 1):
                asalmasalah = 12
            elif(nenek > 0 and anak_pr > 1):
                asalmasalah = 12
            else:
                if(ibu == "y" and nenek == 0 and anak_pr == 1 and cucu_pr > 0 and cucu_lk == 0):
                    asalmasalah = 12
                elif(ibu == "0" and nenek > 0 and anak_pr == 1 and cucu_pr > 0 and cucu_lk == 0):
                    asalmasalah = 12
                else:
                    if(anak_pr > 1):
                        asalmasalah = 12
                    else:
                        if(cucu_lk > 0 or cucu_pr > 0):
                            asalmasalah = 12
                        else:
                            asalmasalah = 4
        else:
            if(ayah == "0" and ibu == "0" and kakek == "0" and nenek == 0):
                asalmasalah = 4
            else:
                asalmasalah = 12
    elif (bagiansuami == 0):
        if(kakek == "0" and nenek == 0 and ayah == "y" and ibu == "y" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 3
        # ayah
        elif(kakek == "0" and nenek == 0 and ayah == "y" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
        # ibu
        elif(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "y" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
        # kakek
        elif(kakek == "y" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
        # ibu
        elif(kakek == "0" and nenek > 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
        # cucupr
        elif(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr > 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah_cucupr = (1 * cucu_pr)
            asalmasalah = asalmasalah_cucupr
        # cuculk
        elif(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk > 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah_cuculk = (1 * cucu_lk)
            asalmasalah = asalmasalah_cuculk
        # cuculk and cucu pr
        elif(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk > 0 and cucu_pr > 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudara_sibu == 0 and saudara_sibu == 0):
            asalmasalah_cucupr = (1 * cucu_pr)
            asalmasalah_cuculk = (2 * cucu_lk)
            asalmasalah = asalmasalah_cucupr + asalmasalah_cuculk
        # batas
        elif(kakek == "y" and nenek > 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 6
        elif(kakek == "y" and nenek == 0 and ayah == "0" and ibu == "y" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 3
        elif(kakek == "0" and nenek > 0 and ayah == "y" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 6 
        elif(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr >= 0 and anak_lk >= 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudara_sibu == 0 and saudara_sibu == 0):
            if(anak_pr > 0 and anak_lk == 0):
                asalmasalah_anakpr = (1 * anak_pr)
                asalmasalah = asalmasalah_anakpr
            elif(anak_pr == 0 and anak_lk > 0):
                asalmasalah_anaklk = (1 * anak_lk)
                asalmasalah = asalmasalah_anaklk
            elif(anak_pr > 0 and anak_lk > 0):
                asalmasalah_anakpr = (1 * anak_pr)
                asalmasalah_anaklk = (2 * anak_lk)
                asalmasalah = asalmasalah_anakpr + asalmasalah_anaklk
        else:
            asalmasalah = 6
print(f"Asal Masalah : {asalmasalah}")
########################## Batas Asal Masalah ###############################

####################### Penghitungan Asal Masalah ###########################
# asal masalah suami
if (suami == "y"):
    if (cucu_lk > 0 or cucu_pr > 0):
        hitungasalmasalah_suami = (asalmasalah / 4) * 1
        asalmasalah_suami = int(hitungasalmasalah_suami)
        print(f"Tampil Siham Masalah Suami : {asalmasalah_suami}")
    elif (anak_lk > 0 or anak_pr > 0):
        hitungasalmasalah_suami = (asalmasalah / 4) * 1
        asalmasalah_suami = int(hitungasalmasalah_suami)
        print(f"Tampil Siham Masalah Suami : {asalmasalah_suami}")
    elif (cucu_pr == 0 and anak_pr == 0 and anak_lk == 0 and anak_pr == 0):
        if(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah_suami = 1
            print(f"Tampil Siham Masalah Suami : {asalmasalah_suami}")
        else:
            hitungasalmasalah_suami = (asalmasalah / 2) * 1
            asalmasalah_suami = int(hitungasalmasalah_suami)
            print(f"Tampil Siham Masalah Suami : {asalmasalah_suami}")
else:
    asalmasalah_suami = 0
    
# asal masalah istri
if (istri > 0):
    if (cucu_lk > 0 or cucu_pr > 0):
        hitungasalmasalah_istri = (asalmasalah / 8) * 1
        asalmasalah_istri = int(hitungasalmasalah_istri)
        print(f"Tampil Siham Masalah Istri : {asalmasalah_istri}")
    elif (anak_lk > 0 or anak_pr > 0):
        hitungasalmasalah_istri = (asalmasalah / 8) * 1
        asalmasalah_istri = int(hitungasalmasalah_istri)
        print(f"Tampil Siham Masalah Istri : {asalmasalah_istri}")
    elif (cucu_pr == 0 and anak_pr == 0 and anak_lk == 0 and anak_pr == 0):
        if(kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah_istri = 1
            print(f"Tampil Siham Masalah Istri : {asalmasalah_istri}")
        else:
            hitungasalmasalah_istri = (asalmasalah / 4) * 1
            asalmasalah_istri = int(hitungasalmasalah_istri)
            print(f"Tampil Siham Masalah Istri : {asalmasalah_istri}")
else:
    asalmasalah_istri = 0

# asal masalah ibu
if (ibu == "y"):
    if (bagiansisaibu == "*sisa"):
        asalmasalah_ibu = 1
        print(f"Tampil Siham Masalah Ibu : {asalmasalah_ibu}")
    else:
        if(pewaris == "SUAMI" or pewaris == "suami" or pewaris == "Suami" or pewaris == "1"):
                hitungasalmasalah_ibu = (asalmasalah / 6) * 1
                asalmasalah_ibu = int(hitungasalmasalah_ibu)
                print(f"Tampil Siham Masalah Ibu : {asalmasalah_ibu}")
        elif(pewaris == "ISTRI" or pewaris == "istri" or pewaris == "Istri" or pewaris == "2"):
            if(suami == "y" and bagiansuami == 0.25 and asalmasalah == 4):
                asalmasalah_ibu = 1
                print(f"Tampil Siham Masalah Ibu : {asalmasalah_ibu}")    
            else:
                if(suami == "0" and anak_pr == 0 and anak_lk == 0):
                    asalmasalah_ibu = 1
                    print(f"Tampil Siham Masalah Ibu : {asalmasalah_ibu}")
                else:
                    hitungasalmasalah_ibu = (asalmasalah / 6) * 1
                    asalmasalah_ibu = int(hitungasalmasalah_ibu)
                    print(f"Tampil Siham Masalah Ibu : {asalmasalah_ibu}")
else:
    asalmasalah_ibu = 0
    
#asal masalah nenek   
if (nenek > 0 and bagiannenek != "termahjub"):
    if(ayah == "0" and kakek =="0" and anak_lk == 0 and anak_pr == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudara_sayah == 0 and saudari_sayah == 0 and saudara_sibu == 0 and saudari_sibu == 0):
        asalmasalah_nenek = 1
        print(f"Tampil Siham Masalah Nenek : {asalmasalah_nenek}")
    else:    
        if(pewaris == "SUAMI" or pewaris == "suami" or pewaris == "Suami" or pewaris == "1"):
                if(istri == 0 and anak_pr == 0 and anak_lk == 0):
                    asalmasalah_nenek = 1
                    print(f"Tampil Siham Masalah Nenek : {asalmasalah_nenek}")
                else:
                    hitungasalmasalah_nenek = (asalmasalah / 6) * 1
                    asalmasalah_nenek = int(hitungasalmasalah_nenek)
                    print(f"Tampil Siham Masalah Nenek : {asalmasalah_nenek}")
        elif(pewaris == "ISTRI" or pewaris == "istri" or pewaris == "Istri" or pewaris == "2"):
            if(suami == "y" and bagiansuami == 0.25 and asalmasalah == 4):
                asalmasalah_nenek = 1
                print(f"Tampil Siham Masalah Nenek : {asalmasalah_nenek}")    
            else:
                if(suami == "0" and anak_pr == 0 and anak_lk == 0):
                    asalmasalah_nenek = 1
                    print(f"Tampil Siham Masalah Nenek : {asalmasalah_nenek}")
                else:
                    hitungasalmasalah_nenek = (asalmasalah / 6) * 1
                    asalmasalah_nenek = int(hitungasalmasalah_nenek)
                    print(f"Tampil Siham Masalah Nenek : {asalmasalah_nenek}")
else:
    asalmasalah_nenek = 0

# asal masalah ayah
if (ayah == "y"):
    if (bagianayah == "sisa"):
        if(pewaris == "istri" or pewaris == "Istri" or pewaris=="ISTRI" or pewaris == "2"):
            if(suami == "0"):
                if(ibu == "0" and nenek > 0):
                    asalmasalah_ayah = 1
                else:
                    if(nenek == 0 and kakek == "0" and ibu == "0"):
                        asalmasalah_ayah = 1
                    else :
                        asalmasalah_ayah = 2
            else:
                if(suami == "y"):
                    if(ibu == "0" and kakek == "0" and nenek == 0):
                        asalmasalah_ayah = 1
                    else:
                        asalmasalah_ayah = 2
                else:
                    asalmasalah_ayah = 1
            if(ibu == "y" and asalmasalah_ayah == 2):
                print(f"Tampil Siham Masalah Ayah : {asalmasalah_ayah}")
            elif(ibu == "y" and asalmasalah_ayah == 1):
                print(f"Tampil Siham Masalah Ayah : {asalmasalah_ayah}")
        else:    
            if(istri == 0):
                if(ibu == "0" and nenek > 0):
                    asalmasalah_ayah = 1
                else:
                    if(nenek == 0 and kakek == "0" and ibu == "0"):
                        asalmasalah_ayah = 1
                    else :
                        asalmasalah_ayah = 2
            else:
                if(istri > 0):
                    if(ibu == "0" and kakek == "0" and nenek == 0):
                        asalmasalah_ayah = 1
                    else:
                        asalmasalah_ayah = 2
                else:
                    asalmasalah_ayah = 1
            if(ibu == "y" and asalmasalah_ayah == 2):
                print(f"Tampil Siham Masalah Ayah : {asalmasalah_ayah}")
            elif(ibu == "y" and asalmasalah_ayah == 1):
                print(f"Tampil Siham Masalah Ayah : {asalmasalah_ayah}")
    else:
        hitungasalmasalah_ayah = (asalmasalah / 6) * 1
        asalmasalah_ayah = int(hitungasalmasalah_ayah)
        print(f"Tampil Siham Masalah Ayah : {asalmasalah_ayah}")
else:
    asalmasalah_ayah = 0
#asal masalah kakek 
if(kakek == "y"):
    if(bagiankakek == "sisa"):
        if(pewaris == "suami" or pewaris == "SUAMI" or pewaris == "Suami" or pewaris == "1"):
            if(istri > 0 and ibu == "y"):
                asalmasalah_kakek = 2
                print(f"Tampil Siham Masalah Kakek : {asalmasalah_kakek}")
            else:
                if(istri == 0 and anak_pr == 0 and anak_lk == 0):
                    if(ibu == "0" and nenek > 0):
                        asalmasalah_kakek = 1
                    else:
                        if(nenek == 0 and ayah == "0" and ibu == "0"):
                            asalmasalah_kakek = 1
                        else :
                            asalmasalah_kakek = 2
                else:
                    if(istri > 0):
                        if(ibu == "0" and ayah == "0" and nenek == 0):
                            asalmasalah_kakek = 1
                        else:
                            asalmasalah_kakek = 2
                    else:
                        asalmasalah_kakek = 1
                if(ibu == "y" and asalmasalah_ayah == 2):
                    print(f"Tampil Siham Masalah Kakek : {asalmasalah_kakek}")
                elif(ibu == "y" and asalmasalah_ayah == 1):
                    print(f"Tampil Siham Masalah Kakek : {asalmasalah_kakek}")
        elif(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
            if(suami == "y" and ibu == "y" and nenek == 0):
                asalmasalah_kakek = 2
                print(f"Tampil Siham Masalah Kakek : {asalmasalah_kakek}")
            elif(suami == "y" and ibu == "0" and nenek > 0):
                asalmasalah_kakek = 2
            else:
                if(suami == "0" and anak_pr == 0 and anak_lk == 0):
                    if(ibu == "0" and nenek > 0):
                        asalmasalah_kakek = 1
                    else:
                        if(nenek == 0 and ayah == "0" and ibu == "0"):
                            asalmasalah_kakek = 1
                        else :
                            asalmasalah_kakek = 2
                else:
                    if(suami == "y"):
                        if(ibu == "0" and ayah == "0" and nenek == 0):
                            asalmasalah_kakek = 1
                        else:
                            asalmasalah_kakek = 2
                    else:
                        asalmasalah_kakek = 1
                print(f"Tampil Siham Masalah Kakek : {asalmasalah_kakek}")
    else:
        hitungasalmasalah_kakek = (asalmasalah / 6)*1
        asalmasalah_kakek = int(hitungasalmasalah_kakek)
        print(f"Tampil Siham Masalah Kakek : {asalmasalah_kakek}")
else:
    asalmasalah_kakek = 0
        
#################################### Hitung Asal Masalah ###################################
# tanpa anak
if (anak_lk == 0 and anak_pr == 0):
    asalmasalah_anakpr = 0
    asalmasalah_anaklk = 0   
    # mengambil nilai asal masalah suami/istri
    if (suami == "y"):
        ambil_asalmasalah = asalmasalah_suami
    else:
        ambil_asalmasalah = asalmasalah_istri
    # batas mendapatkan nilai
    # totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_nenek + asalmasalah_kakek
    asalmasalah_cucupr = 0
    asalmasalah_cuculk = 0
    if(suami == "0" and istri == 0 and ayah == "0" and ibu == "0" and kakek == "0" and nenek == 0 and anak_lk == 0 and anak_pr == 0 and cucu_lk == 0 and saudara_knd == 0 and saudari_knd == 0 and saudara_sayah == 0 and saudari_sayah == 0 and saudara_sibu == 0 and saudari_sibu == 0):
        asalmasalah_cucupr = 1
    else:
        if(cucu_pr > 0 and cucu_lk == 0):
            if(pewaris == "suami" or pewaris == "Suami" or pewaris == "SUAMI" or pewaris == "1") : 
                if(cucu_pr < 2 and cucu_pr > 0):
                    if(kakek == "0" and ayah == "0"):
                        hitungasalmasalah_cucupr = (6 / 2) * 1
                        asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                        print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
                    else:
                        hitungasalmasalah_cucupr = (asalmasalah / 2) * 1
                        asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                        print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")           
                else:
                    if(kakek == "0" and ayah == "0"):
                        hitungasalmasalah_cucupr = (6 / 3) * 2
                        asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                        print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
                    else:
                        hitungasalmasalah_cucupr = (asalmasalah / 3) * 2
                        asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                        print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
            elif(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
                if(suami == "y"):
                    if(asalmasalah == 4):
                        hitungasalmasalah_cucupr = (6 / 2) * 1
                        asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                        print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
                    else:
                        if(cucu_pr < 2 and cucu_pr > 0):
                            hitungasalmasalah_cucupr = (asalmasalah/ 2) * 1
                            asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                            print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
                        else:
                            hitungasalmasalah_cucupr = (asalmasalah/ 3) * 2
                            asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                            print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
                else:
                    if(cucu_pr < 2 and cucu_pr > 0):
                        hitungasalmasalah_cucupr = (asalmasalah / 2) * 1
                        asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                        print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
                    else:
                        hitungasalmasalah_cucupr = (asalmasalah/ 3) * 2
                        asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                        print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
        elif(cucu_pr > 0 and cucu_lk > 0):
            if(anak_pr > 0 and anak_pr < 2):
                asalmasalah_cucupr = (1 * cucu_pr)
            asalmasalah_cuculk = (2 * cucu_lk)        
    if(pewaris == "suami" or pewaris == "Suami" or pewaris == "SUAMI" or pewaris == "1"):
        if(istri == 0 and ibu == "y"):
            if(cucu_lk > 0):
                totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_ayah + asalmasalah_kakek
            else:
                totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_ayah + asalmasalah_kakek + asalmasalah_cucupr
        elif(istri == 0 and nenek > 0):
            if(cucu_lk > 0):
                totalasalmasalah = ambil_asalmasalah + asalmasalah_nenek + asalmasalah_ayah + asalmasalah_kakek
            else:
                totalasalmasalah = ambil_asalmasalah + asalmasalah_nenek + asalmasalah_cucupr + asalmasalah_ayah + asalmasalah_kakek
        else:
            # ibu
            if(istri > 0 and ayah == "0" and kakek == "0" and ibu == "y" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu
                else:
                    totalasalmasalah = ambil_asalmasalah
            # kakek
            elif(istri == 0 and ayah == "0" and kakek == "y" and ibu == "0" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_cucupr
            elif(istri > 0 and ayah == "0" and kakek == "y" and ibu == "0" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_cucupr
            # ayah
            elif(istri == 0 and ayah == "y" and kakek == "0" and ibu == "0" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah
                else :
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_cucupr
            elif(istri > 0 and ayah == "y" and kakek == "0" and ibu == "0" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah
                else :
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_cucupr
            # nenek
            elif(istri > 0 and ayah == "0" and kakek == "0" and ibu == "0" and nenek > 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah
                else:
                    totalasalmasalah = ambil_asalmasalah
            elif(istri > 0 and ayah == "0" and kakek == "0" and ibu == "0" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah
                else:
                    totalasalmasalah = ambil_asalmasalah
            # ayah dan ibu
            elif(istri > 0 and ayah == "y" and kakek == "0" and ibu == "y" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_cucupr
            # ayah dan nenek
            elif(istri > 0 and ayah == "y" and kakek == "0" and ibu == "0" and nenek > 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_nenek
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_nenek + asalmasalah_cucupr
             # kakek dan nenek
            elif(istri > 0 and ayah == "0" and kakek == "y" and ibu == "0" and nenek > 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_nenek
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_nenek + asalmasalah_cucupr
            # kakek dan ibu
            elif(istri > 0 and ayah == "0" and kakek == "y" and ibu == "y" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_ibu
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_ibu + asalmasalah_cucupr
            else:
                if(cucu_lk > 0):
                    if(istri == 0 and ayah == "0" and ibu == "0" and kakek =="0" and nenek == 0 and anak_lk == 0 and anak_pr == 0 and cucu_pr == 0 and cucu_lk > 0 and saudara_knd == 0 and saudari_knd == 0 and saudara_sayah == 0 and saudari_sayah == 0 and saudara_sibu == 0 and saudari_sibu == 0):
                        asalmasalah_cuculk = (1 * cucu_lk)
                        print(f"Tampil Siham Masalah Cucu Laki-Laki : 1")
                        totalasalmasalah = asalmasalah_cuculk
                    elif(istri == 0 and kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk > 0 and cucu_pr > 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudara_sibu == 0 and saudara_sibu == 0):
                        asalmasalah_cucupr = (1 * cucu_pr)
                        asalmasalah_cuculk = (2 * cucu_lk)
                        print(f"Tampil Siham Masalah Cucu Laki-Laki : 2")
                        print(f"Tampil Siham Masalah Cucu Perempuan : 1")
                        totalasalmasalah = asalmasalah_cucupr + asalmasalah_cuculk
                    else:
                        totalasalmasalah = ambil_asalmasalah + asalmasalah_nenek
                else:
                    if(istri == 0 and ayah == "0" and ibu == "0" and kakek =="0" and nenek == 0 and anak_lk == 0 and anak_pr == 0 and cucu_pr > 0 and cucu_lk == 0 and saudara_knd == 0 and saudari_knd == 0 and saudara_sayah == 0 and saudari_sayah == 0 and saudara_sibu == 0 and saudari_sibu == 0):
                        asalmasalah_cucupr = (1 * cucu_pr)
                        print(f"Tampil Siham Masalah Cucu Perempuan : 1")
                        totalasalmasalah = asalmasalah_cucupr
                    else:
                        totalasalmasalah = ambil_asalmasalah + asalmasalah_nenek + asalmasalah_cucupr
    else:
        if(suami == "0" and ibu == "y"):
            if(cucu_lk > 0):
                totalasalmasalah = asalmasalah_ibu + asalmasalah_ayah + asalmasalah_kakek
            else:
                totalasalmasalah = asalmasalah_ibu + asalmasalah_ayah + asalmasalah_kakek + asalmasalah_cucupr
        elif(suami == "0" and nenek > 0):
            if(cucu_lk > 0):
                totalasalmasalah = asalmasalah_nenek + asalmasalah_ayah + asalmasalah_kakek
            else:
                totalasalmasalah = asalmasalah_nenek + asalmasalah_ayah + asalmasalah_kakek + asalmasalah_cucupr
        else:
            if(suami == "0" and ayah == "0" and kakek == "y" and ibu == "0" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = asalmasalah_kakek
                else:
                    totalasalmasalah = asalmasalah_kakek + asalmasalah_cucupr
            elif(suami == "y" and ayah == "0" and kakek == "y" and ibu == "0" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_cucupr
            elif(suami == "y" and ayah == "0" and kakek == "0" and ibu == "0" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah
                else:
                    totalasalmasalah = ambil_asalmasalah
            elif(suami == "y" and ayah == "0" and kakek == "0" and ibu == "y" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_cucupr
            elif(suami == "0" and ayah == "y" and kakek == "0" and ibu == "0" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = asalmasalah_ayah
                else:
                    totalasalmasalah = asalmasalah_ayah + asalmasalah_cucupr
            elif(suami == "y" and ayah == "y" and kakek == "0" and ibu == "0" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_cucupr
            elif(suami == "y" and ayah == "0" and kakek == "0" and ibu == "0" and nenek > 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_nenek
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_nenek + asalmasalah_cucupr
            elif(suami == "y" and ayah == "y" and kakek == "0" and ibu == "y" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_cucupr
            elif(suami == "y" and ayah == "0" and kakek == "y" and ibu == "y" and nenek == 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_ibu
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_ibu + asalmasalah_cucupr
            # ayah dan nenek
            elif(suami == "y" and ayah == "y" and kakek == "0" and ibu == "0" and nenek > 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_nenek
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_nenek + asalmasalah_cucupr
             # kakek dan nenek
            elif(suami == "y" and ayah == "0" and kakek == "y" and ibu == "0" and nenek > 0):
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_nenek
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_kakek + asalmasalah_nenek + asalmasalah_cucupr
            else:
                if(cucu_lk > 0):
                    if(istri == 0 and ayah == "0" and ibu == "0" and kakek =="0" and nenek == 0 and anak_lk == 0 and anak_pr == 0 and cucu_pr == 0 and cucu_lk > 0 and saudara_knd == 0 and saudari_knd == 0 and saudara_sayah == 0 and saudari_sayah == 0 and saudara_sibu == 0 and saudari_sibu == 0):
                        asalmasalah_cuculk = (1 * cucu_lk)
                        print(f"Tampil Siham Masalah Cucu Laki-Laki : 1")
                        totalasalmasalah = asalmasalah_cuculk
                    elif(istri == 0 and kakek == "0" and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk > 0 and cucu_pr > 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudara_sibu == 0 and saudara_sibu == 0):
                        asalmasalah_cucupr = (1 * cucu_pr)
                        asalmasalah_cuculk = (2 * cucu_lk)
                        print(f"Tampil Siham Masalah Cucu Laki-Laki : 2")
                        print(f"Tampil Siham Masalah Cucu Perempuan : 1")
                        totalasalmasalah = asalmasalah_cucupr + asalmasalah_cuculk
                    else:
                        totalasalmasalah = ambil_asalmasalah + asalmasalah_nenek
                else:
                    if(istri == 0 and ayah == "0" and ibu == "0" and kakek =="0" and nenek == 0 and anak_lk == 0 and anak_pr == 0 and cucu_pr > 0 and cucu_lk == 0 and saudara_knd == 0 and saudari_knd == 0 and saudara_sayah == 0 and saudari_sayah == 0 and saudara_sibu == 0 and saudari_sibu == 0):
                        asalmasalah_cucupr = (1 * cucu_pr)
                        print(f"Tampil Siham Masalah Perempuan : 1")
                        totalasalmasalah = asalmasalah_cucupr
                    else:
                        totalasalmasalah = ambil_asalmasalah + asalmasalah_nenek + asalmasalah_cucupr
    sisa = asalmasalah - totalasalmasalah
    if(pewaris == "Suami" or pewaris == "SUAMI" or pewaris == "suami" or pewaris == "1"):
        if(asalmasalah_cucupr == 16):
            jumlahasalmasalah = totalasalmasalah
        else:
            if(ayah == "0" and kakek == "0"):
                if(cucu_pr > 0 and cucu_lk == 0):
                    jumlahasalmasalah = totalasalmasalah
                else:
                    jumlahasalmasalah = asalmasalah
            else:
                jumlahasalmasalah = asalmasalah
    else:
        if(asalmasalah_cucupr == 16):
            jumlahasalmasalah = totalasalmasalah
        else:
            if(ayah == "0" and kakek == "0"):
                if(cucu_pr > 0 and cucu_lk == 0):
                    jumlahasalmasalah = totalasalmasalah
                else:
                    jumlahasalmasalah = asalmasalah
            else:
                if(cucu_pr > 0 and cucu_lk == 0):
                    jumlahasalmasalah = totalasalmasalah
                else:
                    jumlahasalmasalah = asalmasalah
elif (anak_pr > 0 and anak_lk == 0):
    # asal masalah anak perempuan lebih dari 1 dan tanpa anak laki-laki
    if (anak_pr > 1 and anak_lk == 0):
        if(pewaris == "suami" or pewaris == "Suami" or pewaris == "SUAMI" or pewaris == "1"):
            if (ayah == "0" and kakek == "0" and cucu_pr == 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (6 / 3) * 2
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            else:
                hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            print(
                f"Tampil Siham Masalah Anak Perempuan : {asalmasalah_anakpr}")
        elif(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
            # old
            # if (ayah == "0" and ibu == "y" and kakek == "0" and cucu_pr == 0 and cucu_lk == 0):
            #     hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
            #     asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            # elif(ibu == "0" and ayah == "0" and kakek == "0" and cucu_pr == 0 and cucu_lk == 0):
            #     hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
            #     asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            # else:
            #     hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
            #     asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            
            # new
            if (ayah == "0" and kakek == "0" and cucu_pr == 0 and cucu_lk == 0):
                if(ibu == "y"):
                    hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
                elif(nenek > 0):
                    hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
                else:
                    hitungasalmasalah_anakpr = (6 / 3) * 2
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            else:
                hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            print(
                f"Tampil Siham Masalah Anak Perempuan : {asalmasalah_anakpr}")
    elif (anak_pr == 1 and anak_lk == 0):
        if(pewaris == "suami" or pewaris == "Suami" or pewaris == "SUAMI" or pewaris == "1"):
            if (ayah == "0" and ibu == "y" and kakek == "0" and cucu_pr == 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (6 / 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            elif(ibu == "0" and ayah == "0" and kakek == "0" and cucu_pr == 0 and cucu_lk == 0):
                if(nenek > 0):
                    hitungasalmasalah_anakpr = (6/ 2) * 1
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
                else:
                    hitungasalmasalah_anakpr = (2/ 2) * 1
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            elif(ibu == "0" and ayah == "0" and kakek == "0" and cucu_pr > 0 and cucu_lk == 0):
                if(nenek > 0):
                    hitungasalmasalah_anakpr = (6/ 2) * 1
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
                else:
                    hitungasalmasalah_anakpr = (6 / 2) * 1
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            elif(ibu == "y" and ayah == "0" and kakek == "0" and cucu_pr > 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (6 / 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            else:
                hitungasalmasalah_anakpr = (asalmasalah / 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            print(
                f"Tampil Siham Masalah Anak Perempuan : {asalmasalah_anakpr}")
        elif(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
            if (ayah == "0" and ibu == "y" and kakek == "0" and cucu_pr == 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (6 / 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            elif(ibu == "0" and ayah == "0" and kakek == "0" and cucu_pr == 0 and cucu_lk == 0):
                if(nenek > 0):
                    hitungasalmasalah_anakpr = (6/ 2) * 1
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
                else:
                    hitungasalmasalah_anakpr = (2/ 2) * 1
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            elif(ibu == "0" and ayah == "0" and kakek == "0" and cucu_pr > 0 and cucu_lk == 0):
                if(nenek > 0):
                    if(suami == "y"):
                        hitungasalmasalah_anakpr = (asalmasalah / 2) * 1
                        asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
                    else:
                        hitungasalmasalah_anakpr = (6/ 2) * 1
                        asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
                else:
                    hitungasalmasalah_anakpr = (6 / 2) * 1
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            elif(ibu == "y" and ayah == "0" and kakek == "0" and cucu_pr > 0 and cucu_lk == 0):
                if(suami == "y"):
                    hitungasalmasalah_anakpr = (asalmasalah / 2) * 1
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
                else:
                    hitungasalmasalah_anakpr = (6 / 2) * 1
                    asalmasalah_anakpr = int(hitungasalmasalah_anakpr)                 
            else:
                hitungasalmasalah_anakpr = (asalmasalah / 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            print(
                f"Tampil Siham Masalah Anak Perempuan : {asalmasalah_anakpr}")
    elif (anak_pr == 0):
        asalmasalah_anakpr = 0
    # pemabagian siham cucu lk and cucu perempuan
    asalmasalah_cucupr = 0
    asalmasalah_cuculk = 0
    if(cucu_pr > 0 and cucu_lk == 0):
        if(anak_pr > 0 and anak_pr < 2):
            if(pewaris == "suami" or pewaris == "Suami" or pewaris == "SUAMI" or pewaris == "1") :            
                hitungasalmasalah_cucupr = (asalmasalah / 6) * 1
                asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
            elif(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
                if(suami == "y"):
                    if(asalmasalah == 4):
                        hitungasalmasalah_cucupr = (6/ 6) * 1
                        asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                        print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
                    else:
                        hitungasalmasalah_cucupr = (asalmasalah/ 6) * 1
                        asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                        print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
                else:
                    hitungasalmasalah_cucupr = (asalmasalah / 6) * 1
                    asalmasalah_cucupr = int(hitungasalmasalah_cucupr)
                    print(f"Tampil Siham Masalah Cucu Perempuan : {asalmasalah_cucupr}")
    elif(cucu_pr > 0 and cucu_lk > 0):
        if(anak_pr > 0 and anak_pr < 2):
            asalmasalah_cucupr = (1 * cucu_pr)
        else:
            asalmasalah_cucupr = 0
        asalmasalah_cuculk = (2 * cucu_lk)
    # totalasalmasalah dengan anak perempuan tanpa anak lk
    # mengambil nilai asal masalah suami/istri
    if (suami == "y"):
        ambil_asalmasalah = asalmasalah_suami
    else:
        ambil_asalmasalah = asalmasalah_istri
    if(ayah == "0" and kakek == "0"):
        if(pewaris == "istri" or pewaris == "ISTRI" or pewaris == "Istri" or pewaris == "2"):
            if(ibu == "y" and nenek == 0):
                if(anak_pr > 1):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek + asalmasalah_cucupr
                elif(anak_pr == 1):
                    if(cucu_lk > 0):
                        totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_nenek + asalmasalah_anakpr
                    else:
                        if(suami == "y"):
                            if(cucu_pr > 0):
                                totalasalmasalah = ambil_asalmasalah + asalmasalah_anakpr + asalmasalah_cucupr + asalmasalah_ibu
                            else:
                                totalasalmasalah = ambil_asalmasalah
                        else : 
                            totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_nenek + asalmasalah_anakpr + asalmasalah_cucupr
                else:
                    totalasalmasalah = ambil_asalmasalah
            elif(ibu == "0" and nenek > 0):
                if(anak_pr > 1):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek + asalmasalah_cucupr
                elif(anak_pr == 1):
                    if(cucu_lk > 0):
                        totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_nenek + asalmasalah_anakpr
                    else:
                        if(suami == "y"):
                            if(cucu_pr > 0):
                                totalasalmasalah = ambil_asalmasalah + asalmasalah_anakpr + asalmasalah_cucupr + asalmasalah_nenek
                            else:
                                totalasalmasalah = ambil_asalmasalah
                        else : 
                            totalasalmasalah = asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_cucupr
                            # totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_nenek + asalmasalah_anakpr + asalmasalah_cucupr
                else:
                    totalasalmasalah = ambil_asalmasalah
            elif(ibu == "0" and nenek == 0):
                if(anak_pr > 1):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek + asalmasalah_cucupr
                elif(anak_pr == 1):
                    if(cucu_lk > 0):
                        totalasalmasalah = ambil_asalmasalah + asalmasalah_anakpr
                    else:
                        if(suami == 'y'):
                            totalasalmasalah = ambil_asalmasalah
                        else:
                            totalasalmasalah = asalmasalah_anakpr + asalmasalah_cucupr
                else:
                    totalasalmasalah = ambil_asalmasalah
            else:
                # menghilangkan hitung asalmasalah cucu perempuan ketika ada cucu laki-laki
                # bagian cucu perempuan dipindakhkan ke bagian sisa
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek + asalmasalah_cucupr
        elif(pewaris == "suami" or pewaris == "SUAMI" or pewaris == "Suami" or pewaris == "1"):
            # old
            # totalasalmasalah = ambil_asalmasalah
            if(ibu == "y" and nenek == 0):
                if(anak_pr > 1):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek + asalmasalah_cucupr
                elif(anak_pr == 1):
                    if(cucu_lk > 0):
                        totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_nenek + asalmasalah_anakpr
                    else:
                        if(istri > 0):
                            totalasalmasalah = ambil_asalmasalah
                        else : 
                            totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_nenek + asalmasalah_anakpr + asalmasalah_cucupr
                else:
                    totalasalmasalah = ambil_asalmasalah
            elif(ibu == "0" and nenek > 0):
                if(anak_pr > 1):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek + asalmasalah_cucupr
                elif(anak_pr == 1):
                    if(cucu_lk > 0):
                        totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_nenek + asalmasalah_anakpr
                    else:
                        if(istri > 0):
                            totalasalmasalah = ambil_asalmasalah
                        else:
                            totalasalmasalah = asalmasalah_nenek + asalmasalah_anakpr + asalmasalah_cucupr
                            # totalasalmasalah = ambil_asalmasalah + asalmasalah_ibu + asalmasalah_nenek + asalmasalah_anakpr + asalmasalah_cucupr
                else:
                    totalasalmasalah = ambil_asalmasalah
            elif(ibu == "0" and nenek == 0):
                if(anak_pr > 1):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek + asalmasalah_cucupr
                elif(anak_pr == 1):
                    if(cucu_lk > 0):
                        totalasalmasalah = ambil_asalmasalah + asalmasalah_anakpr
                    else:
                        if(istri > 0):
                            totalasalmasalah = ambil_asalmasalah
                        else:
                            totalasalmasalah = asalmasalah_anakpr + asalmasalah_cucupr
                else:
                    totalasalmasalah = ambil_asalmasalah
            else:
                # menghilangkan hitung asalmasalah cucu perempuan ketika ada cucu laki-laki
                # bagian cucu perempuan dipindakhkan ke bagian sisa
                if(cucu_lk > 0):
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek
                else:
                    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek + asalmasalah_cucupr
    else:
        if(cucu_lk > 0):
            totalasalmasalah = ambil_asalmasalah + \
            asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek
        else:
            totalasalmasalah = ambil_asalmasalah + \
                asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_nenek + asalmasalah_kakek + asalmasalah_cucupr
    sisa = asalmasalah - totalasalmasalah
    jumlahasalmasalah = totalasalmasalah
elif(anak_pr > 0 and anak_lk > 0):
    asalmasalah_anakpr = (1 * anak_pr)
    asalmasalah_anaklk = (2 * anak_lk)
    print(f"Tampil Siham Masalah Anak Laki-Laki: {asalmasalah_anaklk}")
    print(f"Tampil Siham Masalah Anak Perempuan: {asalmasalah_anakpr}")
    print("=" * 20)
    if (suami == "y"):
        ambil_asalmasalah = asalmasalah_suami
    else:
        ambil_asalmasalah = asalmasalah_istri
    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_nenek + asalmasalah_kakek
    sisa = asalmasalah - totalasalmasalah
    jumlahasalmasalah = sisa + totalasalmasalah
elif(anak_lk > 0 and anak_pr == 0):
    print("=" * 20)
    if (suami == "y"):
        ambil_asalmasalah = asalmasalah_suami
    else:
        ambil_asalmasalah = asalmasalah_istri
    if(ambil_asalmasalah == 0 and ayah == "0" and ibu =="0" and kakek == "0" and nenek == 0):
        totalasalmasalah = asalmasalah_anaklk
    else:
        totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu +  asalmasalah_nenek + asalmasalah_kakek
    sisa = asalmasalah - totalasalmasalah
    jumlahasalmasalah = sisa + totalasalmasalah
else:
    # mengambil nilai asal masalah suami/istri
    if (suami == "y"):
        ambil_asalmasalah = asalmasalah_suami
    else:
        ambil_asalmasalah = asalmasalah_istri
    # batas mendapatkan nilai
    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu + asalmasalah_nenek
    sisa = asalmasalah - totalasalmasalah
    jumlahasalmasalah = sisa + totalasalmasalah
    
#################################### Batas Hitung Asal Masalah ###################################

if (jumlahasalmasalah == asalmasalah):
    print(f"Jumlah Siham : {int(totalasalmasalah)}")
    print(f"Asal Masalah Sisa: {int(sisa)}")
    # antisipasi Zero division
    # penghitungan bagian suami / istri
    if (suami == "y"):
        if (asalmasalah_suami == 0):
            finalbagiansuami = 0
            ambil_bagian_harta = finalbagiansuami
        else:
            suku_bagian_suami = harta / asalmasalah
            finalbagiansuami = (asalmasalah_suami * suku_bagian_suami)
            ambil_bagian_harta = finalbagiansuami
    else:
        if (asalmasalah_istri == 0):
            finalbagianistri = 0
            ambil_bagian_harta = finalbagianistri
        else:
            suku_bagian_istri = harta / asalmasalah
            finalbagianistri = (asalmasalah_istri * suku_bagian_istri)
            ambil_bagian_harta = finalbagianistri
    # batas penghitungan bagian suami / istri
    # bagiananakpr
    if(asalmasalah_anakpr == 0):
        finalbagiananakpr = 0
    else:
        suku_bagian_anak_pr = harta / asalmasalah
        finalbagiananakpr = (asalmasalah_anakpr * suku_bagian_anak_pr)
    # perhitungan bagian nenek
    if(asalmasalah_nenek != 0):
        if(ayah == "0" and kakek =="0" and anak_lk == 0 and anak_pr == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudara_sayah == 0 and saudari_sayah == 0 and saudara_sibu == 0 and saudari_sibu == 0):
            sisa_harta_nenek = harta - ambil_bagian_harta
            finalbagiannenek = asalmasalah_nenek * sisa_harta_nenek
        else:
            finalbagiannenek = (asalmasalah_nenek * harta) / asalmasalah
    else:
        finalbagiannenek = 0
    # perhitungan bagian ibu
    if (asalmasalah_ibu == 0):
        finalbagianibu = 0
    else:
        if (bagiansisaibu == "*sisa"):
            sisa_harta = harta - ambil_bagian_harta
            if (ayah == "y"):
                asalmasalah_sisa = asalmasalah_ibu + asalmasalah_ayah
                suku_bagian = sisa_harta / asalmasalah_sisa
                finalbagianibu = asalmasalah_ibu * suku_bagian
            elif(kakek == "y"):
                asalmasalah_sisa = asalmasalah_ibu + asalmasalah_kakek
                suku_bagian = sisa_harta / asalmasalah_sisa
                finalbagianibu = asalmasalah_ibu * suku_bagian
            else:
                finalbagianibu = sisa_harta
        else:
            finalbagianibu = (asalmasalah_ibu * harta) / jumlahasalmasalah
    # penghitungan bagian ayah / kakek
    if(asalmasalah_kakek == 0):
        finalbagiankakek = 0
    else:
        finalbagiankakek = (asalmasalah_kakek * harta) / jumlahasalmasalah
    #ayah
    if (asalmasalah_ayah == 0):
        finalbagianayah = 0
        sisa_harta_ayah = 0
    else:
        if (bagianayah == "sisa" and bagiansisa == ""):
            # old
            sisa_harta = harta - ambil_bagian_harta
            # new
            # sisa_harta = harta - ambil_bagian_harta - finalbagianibu - finalbagiannenek
            if(suami == "0" and nenek > 0):
                sisa_harta = harta - ambil_bagian_harta - finalbagiannenek
                asalmasalah_sisa = asalmasalah_ibu + asalmasalah_ayah
            else:
                sisa_harta = harta - ambil_bagian_harta
                asalmasalah_sisa = asalmasalah_ibu + asalmasalah_ayah + asalmasalah_nenek
            suku_bagian = sisa_harta / asalmasalah_sisa
            finalbagianayah = suku_bagian * asalmasalah_ayah
            sisa_harta_ayah = 0
        elif (bagianayah == 0.16 and bagiansisa == "+sisa"):
            harta_cucupr = (asalmasalah_cucupr * harta) / jumlahasalmasalah
            finalbagianayah = (asalmasalah_ayah * harta) / jumlahasalmasalah
            sisa_harta_ayah = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - harta_cucupr - finalbagiananakpr
            if(sisa_harta_ayah <= 0):
                sisa_harta_ayah = 0.0
        else:
            sisa_harta_ayah = 0
            finalbagianayah = (asalmasalah_ayah * harta) / jumlahasalmasalah
    # batas penghitungan bagian ayah/kakek
    # batas antisipasi Zero division error
    print("=" * 40)

    if (suami == "y"):
        print(f"Bagian Harta Suami : {round(finalbagiansuami, 2)}")
    else:
        # tampil bagian istri jika lebih 1 harta per istri
        if (istri > 1):
            bagi_harta_istri = finalbagianistri / istri
            print(f"Bagian Harta Istri : {round(finalbagianistri , 2)}")
            j = 1
            while j <= istri:
                print("Harta Untuk Istri Ke- ",
                      j, " = ", round(bagi_harta_istri, 2))
                j += 1
        else:
            if (istri != 0):
                print(f"Bagian Harta Istri : {round(finalbagianistri, 2)}")
    if(ayah == "y"):
        if(bagiansisa == "+sisa"):
            print(f"Bagian Harta Ayah 1/6 + Sisa : {round(finalbagianayah, 2)} + {round(sisa_harta_ayah, 2)}")
            print(f"Jumlah Harta Ayah : {round(finalbagianayah + sisa_harta_ayah, 2)}")
        else:
            print(f"Bagian Harta Ayah : {round(finalbagianayah, 2)}")
    if(ibu == "y"):
        print(f"Bagian Harta Ibu : {round(finalbagianibu, 2)}")
    if (nenek > 1):
            bagi_harta_nenek = finalbagiannenek / nenek
            print(f"Bagian Harta Nenek : {round(finalbagiannenek, 2)}")
            j = 1
            while j <= nenek:
                print("Harta Untuk Nenek Ke- ",
                      j, " = ", round(bagi_harta_nenek, 2))
                j += 1
    else:
        if (nenek != 0):
            print(f"Bagian Harta Nenek : {round(finalbagiannenek, 2)}")
    sisa_harta_kakek = 0
    if(kakek == "y"):
        if (bagiankakek == "sisa" and bagiansisakakek == ""):
            if(pewaris == "suami" or pewaris == "SUAMI" or pewaris == "Suami" or pewaris == "1"):
                if(istri > 0 and ibu == "y"):
                    sisa_harta_kakek = harta - ambil_bagian_harta   
                    asalmasalah_sisa = asalmasalah_ibu + asalmasalah_kakek
                elif(istri > 0 and nenek > 0):
                    sisa_harta_kakek = harta - ambil_bagian_harta - finalbagiannenek
                    asalmasalah_sisa = asalmasalah_kakek
                elif(istri == 0 and nenek > 0):
                    sisa_harta_kakek = harta - finalbagiannenek
                    asalmasalah_sisa = asalmasalah_kakek
                elif(istri == 0 and ibu == "y"):
                    sisa_harta_kakek = harta - finalbagianibu
                    asalmasalah_sisa = asalmasalah_kakek
                else:
                    sisa_harta_kakek = harta - ambil_bagian_harta
                    asalmasalah_sisa = asalmasalah_kakek
            elif(pewaris == "istri" or pewaris == "ISTRI" or pewaris == "Istri" and pewaris == "2"):
                if(suami == "y" and ibu == "y"):
                    sisa_harta_kakek = harta - ambil_bagian_harta   
                    asalmasalah_sisa = asalmasalah_ibu + asalmasalah_kakek
                elif(suami == "y" and nenek > 0):
                    sisa_harta_kakek = harta - ambil_bagian_harta - finalbagiannenek
                    asalmasalah_sisa = asalmasalah_kakek
                elif(suami == "0" and nenek > 0):
                    sisa_harta_kakek = harta - finalbagiannenek
                    asalmasalah_sisa = asalmasalah_kakek
                elif(suami == "0" and ibu == "y"):
                    sisa_harta_kakek = harta - finalbagianibu
                    asalmasalah_sisa = asalmasalah_kakek
                else:
                    sisa_harta_kakek = harta - ambil_bagian_harta
                    asalmasalah_sisa = asalmasalah_kakek
            suku_bagian = sisa_harta_kakek / asalmasalah_sisa
            finalbagiankakek = suku_bagian * asalmasalah_kakek
        elif (bagiankakek == 0.16 and bagiansisakakek == "+sisa"):
            harta_cucupr = (asalmasalah_cucupr * harta) / jumlahasalmasalah
            finalbagiankakek = (asalmasalah_kakek * harta) / jumlahasalmasalah
            sisa_harta_kakek = harta - ambil_bagian_harta - finalbagiankakek - finalbagianibu - finalbagiannenek - harta_cucupr - finalbagiananakpr
        # tampil harta kakek
        if(bagiansisakakek == "+sisa"):
            if(sisa_harta_kakek <= 0):
                sisa_harta_kakek = 0.0
            print(f"Bagian Harta Kakek 1/6 + sisa: {round(finalbagiankakek, 2)} + {round(sisa_harta_kakek, 2)}")
            print(f"Jumlah Harta Kakek : {round(finalbagiankakek + sisa_harta_kakek, 2)}")
        else:
            print(f"Bagian Harta Kakek : {round(finalbagiankakek, 2)}")
    # bagian harta anak laki dan perempuan
    if (anak_pr > 0 or anak_lk > 0):
        if (anak_pr > 0 and anak_lk == 0):
            asalmasalah_anakpr = (1 * anak_pr)
            asalmasalah_sisa = asalmasalah_anakpr
            harta_cucupr = (asalmasalah_cucupr * harta) / jumlahasalmasalah
            # sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
            sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek - harta_cucupr
            print(f"Sisa Harta : {round(sisa_harta, 2)}")
            suku_bagian = sisa_harta / asalmasalah_sisa
            sisa_harta_anak_pr = (1 * suku_bagian)
            bagianharta_anak_pr = sisa_harta_anak_pr * anak_pr
            print(f"Harta Anak Perempuan : {round(bagianharta_anak_pr, 2)}")
            # pembagian harta per anak perempuan
            if(anak_pr > 1):
                k = 1
                while k <= anak_pr:
                    print("Harta Untuk Anak Perempuan ",
                        k, " = ", round(sisa_harta_anak_pr,2))
                    k += 1
        elif (anak_lk > 0 and anak_pr == 0):
            asalmasalah_anaklk = (1 * anak_lk)
            asalmasalah_sisa = asalmasalah_anaklk
            sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek
            print(f"Sisa Harta : {round(sisa_harta, 2)}")
            suku_bagian = sisa_harta / asalmasalah_sisa
            sisa_harta_anak_lk = (1 * suku_bagian)
            bagianharta_anak_lk = sisa_harta_anak_lk * anak_lk
            print(f"Harta Anak Laki-Laki : {round(bagianharta_anak_lk, 2)}")
            # pembagian harta per anak laki-laki
            if(anak_lk > 1):
                j = 1
                while j <= anak_lk:
                    print("Harta Untuk Anak Laki - Laki ",
                        j, " = ", round(sisa_harta_anak_lk, 2))
                    j += 1
        elif (anak_lk > 0 and anak_lk > 0):
            asalmasalah_anaklk = (2 * anak_lk)
            asalmasalah_anakpr = (1 * anak_pr)
            asalmasalah_sisa = asalmasalah_anaklk + asalmasalah_anakpr
            sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek
            print(f"Sisa Harta : {round(sisa_harta, 2)}")
            suku_bagian = sisa_harta / asalmasalah_sisa
            sisa_harta_anak_pr = (1 * suku_bagian)
            sisa_harta_anak_lk = (2 * suku_bagian)
            bagianharta_anak_pr = sisa_harta_anak_pr * anak_pr
            bagianharta_anak_lk = sisa_harta_anak_lk * anak_lk
            print(f"Harta Anak Perempuan : {round(bagianharta_anak_pr, 2)}")
            # pembagian harta per anak perempuan
            if(anak_pr > 1):
                i = 1
                while i <= anak_pr:
                    print("Harta Untuk Anak Perempuan ",
                        i, " = ", round(sisa_harta_anak_pr, 2))
                    i += 1
            # pembagian harta per anak laki-laki
            print(f"Harta Anak Laki-Laki : {round(bagianharta_anak_lk, 2)}")
            if(anak_lk > 1):
                j = 1
                while j <= anak_lk:
                    print("Harta Untuk Anak Laki - Laki ",
                        j, " = ", round(sisa_harta_anak_lk, 2))
                    j += 1
    # bagianharta cucu
    if (cucu_pr > 0 or cucu_lk > 0):
        if (cucu_pr > 0 and cucu_lk == 0):
            asalmasalah_cucupr = (1 * cucu_pr)
            asalmasalah_sisa = asalmasalah_cucupr
            # sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
            if(kakek == "y" and ayah == "0"):
                sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek - sisa_harta_kakek - finalbagiananakpr
            else:
                sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek - sisa_harta_ayah - finalbagiananakpr
            if(sisa_harta <= 0):
                sisa_harta_cucu_pr = 0.0
                bagianharta_cucu_pr = 0.0
            else:
                suku_bagian = sisa_harta / asalmasalah_sisa
                sisa_harta_cucu_pr = (1 * suku_bagian)
                bagianharta_cucu_pr = sisa_harta_cucu_pr * cucu_pr
                print(f"Sisa Harta : {round(sisa_harta, 2)}")
            # pembagian harta per cucu perempuan
            print("-" * 25)
            if(bagiancucupr != "termahjub"):
                print(f"Harta Cucu Perempuan : {round(bagianharta_cucu_pr, 2)}")
                if(cucu_pr > 1):
                    k = 1
                    while k <= cucu_pr:
                        print("Harta Untuk Cucu Perempuan ",
                            k, " = ", round(sisa_harta_cucu_pr, 2))
                        k += 1
        elif (cucu_lk > 0 and cucu_pr == 0):
            asalmasalah_cuculk = (1 * cucu_lk)
            asalmasalah_sisa = asalmasalah_cuculk
            sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek - finalbagiananakpr
            if(sisa_harta <= 0):
                sisa_harta_cucu_lk = 0.0
                bagianharta_cucu_lk = 0.0
            else:
                print(f"Sisa Harta : {round(sisa_harta, 2)}")
                suku_bagian = sisa_harta / asalmasalah_sisa
                sisa_harta_cucu_lk = (1 * suku_bagian)
                bagianharta_cucu_lk = sisa_harta_cucu_lk * cucu_lk
            print("-" * 25)
            # pembagian harta per cucu laki-laki
            if(bagiancuculk != "termahjub"):
                print(f"Harta Cucu Laki-Laki : {round(bagianharta_cucu_lk, 2)}")
                if(cucu_lk > 1):
                    j = 1
                    while j <= cucu_lk:
                        print("Harta Untuk Cucu Laki - Laki ",
                            j, " = ", round(sisa_harta_cucu_lk, 2))
                        j += 1
        elif (cucu_lk > 0 and cucu_lk > 0):
            asalmasalah_cuculk = (2 * cucu_lk)
            asalmasalah_cucupr = (1 * cucu_pr)
            asalmasalah_sisa = asalmasalah_cuculk + asalmasalah_cucupr
            sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek - finalbagiananakpr
            if(sisa_harta <= 0):
                sisa_harta_cucu_lk = 0.0
                bagianharta_cucu_lk = 0.0
                sisa_harta_cucu_pr = 0.0
                bagianharta_cucu_pr = 0.0
            else:
                print(f"Sisa Harta : {round(sisa_harta, 2)}")
                suku_bagian = sisa_harta / asalmasalah_sisa
                sisa_harta_cucu_pr = (1 * suku_bagian)
                sisa_harta_cucu_lk = (2 * suku_bagian)
                bagianharta_cucu_pr = sisa_harta_cucu_pr * cucu_pr
                bagianharta_cucu_lk = sisa_harta_cucu_lk * cucu_lk
            print("-" * 25)
            # pembagian harta per cucu perempuan
            if(bagiancucupr != "termahjub"):
                print(f"Harta Cucu Perempuan : {round(bagianharta_cucu_pr, 2)}")
                if(cucu_pr > 1):
                    i = 1
                    while i <= cucu_pr:
                        print("Harta Untuk Cucu Perempuan ",
                            i, " = ", round(sisa_harta_cucu_pr, 2))
                        i += 1
            # pembagian harta per cucu laki-laki
            print("-" * 25)
            if(bagiancuculk != "termahjub"):
                print(f"Harta Cucu Laki-Laki : {round(bagianharta_cucu_lk, 2)}")
                if(cucu_lk > 1):
                    j = 1
                    while j <= cucu_lk:
                        print("Harta Untuk Cucu Laki - Laki ",
                            j, " = ", round(sisa_harta_cucu_lk, 2))
                        j += 1
elif (jumlahasalmasalah > asalmasalah):
    print(f"Jumlah Siham : {int(totalasalmasalah)}")
    if(sisa > 0):
        print(f"Asal Masalah Sisa: {int(sisa)}")
    sisa_harta = 0
    suku_bagian = harta / jumlahasalmasalah
    if (suami == "y"):
        if (asalmasalah_suami == 0):
            finalbagiansuami = 0
            ambil_bagian_harta = finalbagiansuami
        else:
            finalbagiansuami = (asalmasalah_suami * harta) / jumlahasalmasalah
            ambil_bagian_harta = finalbagiansuami
    else:
        if (asalmasalah_istri == 0):
            finalbagianistri = 0
            ambil_bagian_harta = finalbagianistri
        else:
            finalbagianistri = (asalmasalah_istri * harta) / jumlahasalmasalah
            ambil_bagian_harta = finalbagianistri
    if (asalmasalah_ibu == 0):
        finalbagianibu = 0
    else:
        if (bagiansisaibu == "*sisa"):
            sisa_harta = harta - ambil_bagian_harta
            if (ayah == "y"):
                asalmasalah_sisa = asalmasalah_ibu + asalmasalah_ayah
                suku_bagian = sisa_harta / asalmasalah_sisa
                finalbagianibu = asalmasalah_ibu * suku_bagian
            else:
                finalbagianibu = sisa_harta
        else:
            finalbagianibu = (asalmasalah_ibu * harta) / jumlahasalmasalah
    # perhitungan bagian nenek lebih
    # old
    # if(asalmasalah_nenek != 0):
    #     if(ayah == "0" and kakek =="0" and anak_lk == 0 and anak_pr == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudara_sayah == 0 and saudari_sayah == 0 and saudara_sibu == 0 and saudari_sibu == 0):
    #         sisa_harta_nenek = harta - ambil_bagian_harta
    #         finalbagiannenek = asalmasalah_nenek * sisa_harta_nenek
    #     else:
    #         finalbagiannenek = (asalmasalah_nenek * harta) / asalmasalah
    # else:
    #     finalbagiannenek = 0
    
    # new
    if (asalmasalah_nenek == 0):
        finalbagiannenek = 0
    else:
        finalbagiannenek = (asalmasalah_nenek * harta) / jumlahasalmasalah
    # penghitungan bagian ayah / kakek
    if (asalmasalah_kakek == 0):
        finalbagiankakek = 0
    else:
        if (bagiankakek == "sisa"):
            sisa_harta = harta - ambil_bagian_harta
            asalmasalah_sisa = asalmasalah_ibu + asalmasalah_kakek
            suku_bagian = sisa_harta / asalmasalah_sisa
            print("=" * 50)
            print("Asal Masalah Sisa ", asalmasalah_sisa)
            print("Suku Bagian ", suku_bagian)
            finalbagiankakek = suku_bagian * asalmasalah_kakek
        else:
            finalbagiankakek = (asalmasalah_kakek * harta) / jumlahasalmasalah
    
    if (asalmasalah_ayah == 0):
        finalbagianayah = 0
    else:
        if (bagianayah == "sisa"):
            sisa_harta = harta - ambil_bagian_harta
            asalmasalah_sisa = asalmasalah_ibu + asalmasalah_ayah
            suku_bagian = sisa_harta / asalmasalah_sisa
            print("=" * 50)
            print("Asal Masalah Sisa ", asalmasalah_sisa)
            print("Suku Bagian ", suku_bagian)
            finalbagianayah = suku_bagian * asalmasalah_ayah
        else:
            finalbagianayah = (asalmasalah_ayah * harta) / jumlahasalmasalah
    # batas penghitungan bagian ayah/kakek
    if(asalmasalah_anakpr == 0):
        finalbagiananakpr = 0
    else:
        finalbagiananakpr = (asalmasalah_anakpr * suku_bagian)
    print("=" * 20)
    print(f"Asal Masalah Awal : {int(asalmasalah)}")
    print(f"Asal Masalah Menjadi : {int(jumlahasalmasalah)}")
    # cucu perempuan
    # bagian cucu laki dan cucu perempuan
    finalbagiancucupr = 0
    finalbagiancuculk = 0
    sisa_cucu = 0
    cucu = ""
    if(cucu_pr > 0 and cucu_lk == 0):
        finalbagiancuculk = 0
        cucu = "kondisi1"
        if(bagiancucupr != "termahjub") :  
            if (cucu_pr > 0 and anak_pr > 0):
                if(ayah == "0" and kakek == "0"):
                    if(ibu == "y"):
                        asalmasalah_sisa = asalmasalah_anakpr + asalmasalah_cucupr + asalmasalah_ibu
                    else:
                        if(nenek > 0):
                            asalmasalah_sisa = asalmasalah_anakpr + asalmasalah_cucupr + asalmasalah_nenek
                        else:
                            asalmasalah_sisa = asalmasalah_anakpr + asalmasalah_cucupr
                    sisa_harta_cucu_pr = harta - ambil_bagian_harta
                    suku_bagian_cucu = sisa_harta_cucu_pr / asalmasalah_sisa
                else:
                    suku_bagian_cucu = harta / jumlahasalmasalah
                finalbagiancucupr = asalmasalah_cucupr * suku_bagian_cucu
                # sisa_harta_cucu_pr = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek
            else:
                finalbagiancucupr = asalmasalah_cucupr * suku_bagian
        else:
            finalbagiancucupr = 0
    elif(cucu_pr == 0 and cucu_lk > 0):
        if(bagiancuculk != "termahjub"):
            cucu = "kondisi2"
            sisa_harta_cucu = harta - ambil_bagian_harta - finalbagiananakpr - finalbagianayah - finalbagiankakek - finalbagianibu - finalbagiannenek
            if(sisa_harta_cucu <= 0):
                sisa_harta_cucu_lk = 0
                finalbagiancuculk = 0
            else:
                sisa_harta_cucu_lk = (1 * sisa_harta_cucu)
                finalbagiancuculk = sisa_harta_cucu_lk * cucu_lk
        else:
            finalbagiancuculk = 0
        sisa_cucu = finalbagiancuculk
    
    elif(cucu_pr > 0 and cucu_lk > 0):
        cucu = "kondisi3"
        asalmasalah_sisa_cucu = asalmasalah_cucupr + asalmasalah_cuculk
        sisa_harta_cucu = harta - ambil_bagian_harta - finalbagiananakpr - finalbagianayah - finalbagiankakek - finalbagianibu - finalbagiannenek
        if(sisa_harta_cucu <= 0):
            sisa_harta_cucu = 0
        else:
            sisa_harta_cucu = sisa_harta_cucu
        suku_bagian_cucu = sisa_harta_cucu / asalmasalah_sisa_cucu
        sisa_harta_cucu_pr = (1 * suku_bagian_cucu)
        sisa_harta_cucu_lk = (2 * suku_bagian_cucu)
        if(bagiancucupr != "termahjub"):
            finalbagiancucupr = sisa_harta_cucu_pr * cucu_pr
        else:
            finalbagiancucupr = 0
        if(bagiancuculk != "termahjub"):
            finalbagiancuculk = sisa_harta_cucu_lk * cucu_lk
        else:
            finalbagiancuculk = 0
        sisa_cucu = finalbagiancucupr + finalbagiancuculk 
        
    # batas cucu perempuan
    if (suami == "y"):
        print(f"Bagian Harta Suami : {round(finalbagiansuami, 2)}")
    else:
        # tampil bagian istri jika lebih 1 harta per istri
        if (istri > 1):
            bagi_harta_istri = finalbagianistri / istri
            print(f"Bagian Harta Istri : {round(finalbagianistri, 2)}")
            j = 1
            while j <= istri:
                print("Harta Untuk Istri Ke- ",
                        j, " = ", bagi_harta_istri)
                j += 1
        else:
            if (istri != 0):
                print(f"Bagian Harta Istri : {round(finalbagianistri , 2)}")
    if (bagianayah == 0.16 and bagiansisa == "+sisa"):
        print(f"Bagian Harta Ayah 1/6 + sisa: {round(finalbagianayah, 2)} + {round(sisa_harta, 2)}")
        print(f"Harta untuk ayah =  {round(finalbagianayah + sisa_harta, 2)}")
    else:
        if(ayah == "y"):
            print(f"Bagian Harta Ayah : {round(finalbagianayah, 2)}")
    if(ibu == "y"):
        print(f"Bagian Harta Ibu : {round(finalbagianibu, 2)}")
    if (nenek > 1):
            bagi_harta_nenek = finalbagiannenek / nenek
            print(f"Bagian Harta Nenek : {round(finalbagiannenek, 2)}")
            j = 1
            while j <= nenek:
                print("Harta Untuk Nenek Ke- ",
                      j, " = ", round(bagi_harta_nenek, 2))
                j += 1
    else:
        if (nenek != 0):
            print(f"Bagian Harta Nenek : {round(finalbagiannenek, 2)}")
    # tampil bagian kakek
    if(kakek == "y"):
        if (bagiankakek == "sisa" and bagiansisakakek == ""):
            if(pewaris == "suami" or pewaris == "SUAMI" or pewaris == "Suami" or pewaris == "1"):
                if(istri > 0 and ibu == "y"):
                    sisa_harta_kakek = harta - ambil_bagian_harta   
                    asalmasalah_sisa = asalmasalah_ibu + asalmasalah_kakek
                elif(istri > 0 and nenek > 0):
                    sisa_harta_kakek = harta - ambil_bagian_harta - finalbagiannenek
                    asalmasalah_sisa = asalmasalah_kakek
                elif(istri == 0 and nenek > 0):
                    sisa_harta_kakek = harta - finalbagiannenek
                    asalmasalah_sisa = asalmasalah_kakek
                elif(istri == 0 and ibu == "y"):
                    sisa_harta_kakek = harta - finalbagianibu
                    asalmasalah_sisa = asalmasalah_kakek
                else:
                    sisa_harta_kakek = harta - ambil_bagian_harta
                    asalmasalah_sisa = asalmasalah_kakek
            elif(pewaris == "istri" or pewaris == "ISTRI" or pewaris == "Istri" and pewaris == "2"):
                if(suami == "y" and ibu == "y"):
                    sisa_harta_kakek = harta - ambil_bagian_harta   
                    asalmasalah_sisa = asalmasalah_ibu + asalmasalah_kakek
                elif(suami == "y" and nenek > 0):
                    sisa_harta_kakek = harta - ambil_bagian_harta - finalbagiannenek
                    asalmasalah_sisa = asalmasalah_kakek
                elif(suami == "0" and nenek > 0):
                    sisa_harta_kakek = harta - finalbagiannenek
                    asalmasalah_sisa = asalmasalah_kakek
                elif(suami == "0" and ibu == "y"):
                    sisa_harta_kakek = harta - finalbagianibu
                    asalmasalah_sisa = asalmasalah_kakek
                else:
                    sisa_harta_kakek = harta - ambil_bagian_harta
                    asalmasalah_sisa = asalmasalah_kakek
            suku_bagian = sisa_harta_kakek / asalmasalah_sisa
            finalbagiankakek = suku_bagian * asalmasalah_kakek
            print(f"Bagian Harta Kakek : {round(finalbagiankakek, 2)}")
        elif (bagiankakek == 0.16 and bagiansisakakek == "+sisa"):
            print(f"Bagian Harta Kakek 1/6 + sisa: {round(finalbagiankakek, 2)} + {round(sisa_harta ,2)}")
            print(f"Harta untuk kakek =  {round(finalbagiankakek + sisa_harta, 2)}")
        else:
            print(f"Bagian Harta Kakek : {round(finalbagiankakek, 2)}")
    if (anak_pr > 0 and anak_lk == 0):
        asalmasalah_anakpr = (1 * anak_pr)
        asalmasalah_sisa = asalmasalah_anakpr
        # batas ambil bagian suami / istri
        # sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek - finalbagiancucupr
        print(f"Sisa Harta : {round(sisa_harta , 2)}")
        suku_bagian = sisa_harta / asalmasalah_sisa
        sisa_harta_anak_pr = (1 * suku_bagian)
        bagianharta_anak_pr = sisa_harta_anak_pr * anak_pr
        print(f"Harta Anak Perempuan : {round(bagianharta_anak_pr ,2)}")
        # pembagian harta per anak perempuan
        k = 1
        while k <= anak_pr:
            print("Harta Untuk Anak Perempuan ",
                    k, " = ", round(sisa_harta_anak_pr, 2))
            k += 1
    elif (anak_lk > 0 and anak_pr == 0):
        asalmasalah_anaklk = (1 * anak_lk)
        asalmasalah_sisa = asalmasalah_anaklk
        # batas ambil bagian suami / istri
        # sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek
        print(f"Sisa Harta : {round(sisa_harta, 2)}")
        suku_bagian = sisa_harta / asalmasalah_sisa
        sisa_harta_anak_lk = (1 * suku_bagian)
        bagianharta_anak_lk = sisa_harta_anak_lk * anak_lk
        print(f"Harta Anak Laki-Laki : {round(bagianharta_anak_lk, 2)}")
        # pembagian harta per anak laki-laki
        j = 1
        while j <= anak_lk:
            print("Harta Untuk Anak Laki - Laki ",
                    j, " = ", round(sisa_harta_anak_lk, 2))
            j += 1
    elif (anak_lk > 0 and anak_pr > 0):
        asalmasalah_anaklk = (2 * anak_lk)
        asalmasalah_anakpr = (1 * anak_pr)
        asalmasalah_sisa = asalmasalah_anaklk + asalmasalah_anakpr
        # ambil bagian suami jika ada jika tidak ada ambil bagian istri
        if (suami == "y"):
            ambil_bagian_harta = finalbagiansuami
        else:
            ambil_bagian_harta = finalbagianistri
        # batas ambil bagian suami / istri
        # sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek
        print(f"Sisa Harta : {round(sisa_harta, 2)}")
        suku_bagian = sisa_harta / asalmasalah_sisa
        sisa_harta_anak_pr = (1 * suku_bagian)
        sisa_harta_anak_lk = (2 * suku_bagian)
        bagianharta_anak_pr = sisa_harta_anak_pr * anak_pr
        bagianharta_anak_lk = sisa_harta_anak_lk * anak_lk
        print(f"Harta Anak Perempuan : {round(bagianharta_anak_pr, 2)}")
        print(f"Harta Anak Laki-Laki : {round(bagianharta_anak_lk, 2)}")
        # pembagian harta per anak perempuan
        i = 1
        while i <= anak_pr:
            print("Harta Untuk Anak Perempuan ",
                    i, " = ", round(sisa_harta_anak_pr, 2))
            i += 1
        # pembagian harta per anak laki-laki
        j = 1
        while j <= anak_lk:
            print("Harta Untuk Anak Laki - Laki ",
                    j, " = ", round(sisa_harta_anak_lk, 2))
            j += 1
    # # bagian harta cucu pr
    # if(cucu_pr > 0):
    #     print(f"Bagian Harta Cucu Perempuan : {int(finalbagiancucupr)}")
    #     if(finalbagiancucupr == 0):
    #         sisa_harta_cucu_pr = 0
    #     else:    
    #         sisa_harta_cucu_pr = finalbagiancucupr / cucu_pr
    #     # pembagian harta per cucu perempuan
    #     if(cucu_pr > 1):
    #         i = 1
    #         while i <= cucu_pr:
    #             print("Harta Untuk Cucu Perempuan ", i, " = ", sisa_harta_cucu_pr)
    #             i += 1
    # bagian harta cucu pr
    if(cucu == "kondisi1"):
        if(bagiancucupr != "termahjub"):
            print(f"Bagian Harta Cucu Perempuan : {round(finalbagiancucupr, 2)}")
            if(finalbagiancucupr == 0):
                sisa_harta_cucu_pr = 0
            else:    
                sisa_harta_cucu_pr = finalbagiancucupr / cucu_pr
            # pembagian harta per cucu perempuan
            if(cucu_pr > 1):
                i = 1
                while i <= cucu_pr:
                    print("Harta Untuk Cucu Perempuan ", i, " = ", round(sisa_harta_cucu_pr, 2))
                    i += 1
    elif(cucu == "kondisi2"):
        # pembagian harta per cucu laki-laki
        if(bagiancuculk != "termahjub"):
            print(f"Harta Cucu Laki-Laki : {round(finalbagiancuculk, 2)}")
            if(cucu_lk > 1):
                j = 1
                while j <= cucu_lk:
                    print("Harta Untuk Cucu Laki - Laki ",
                            j, " = ", round(sisa_harta_cucu_lk, 2))
                    j += 1
    elif(cucu == "kondisi3"):
        # pembagian harta per cucu perempuan
        if(bagiancucupr != "termahjub"):
            print(f"Harta Cucu Perempuan : {round(finalbagiancucupr, 2)}")
            if(cucu_pr > 1):
                i = 1
                while i <= cucu_pr:
                    print("Harta Untuk Cucu Perempuan ",
                            i, " = ", sisa_harta_cucu_pr)
                    i += 1
        # pembagian harta per cucu laki-laki
        if(bagiancuculk != "termahjub"):
            print(f"Harta Cucu Laki-Laki : {round(finalbagiancuculk, 2)}")
            if(cucu_lk > 1):
                j = 1
                while j <= cucu_lk:
                    print("Harta Untuk Cucu Laki - Laki ",
                            j, " = ", round(sisa_harta_cucu_lk, 2))
                    j += 1
elif (jumlahasalmasalah < asalmasalah):
    tampil = ""
    print(f"Jumlah Siham : {int(totalasalmasalah)}")
    # antisipasi Zero division error
    # hitung harta suami/istri
    if (suami == "y"):
        # old
        # suku_bagian = harta / jumlahasalmasalah
        # if (asalmasalah_suami == 0):
        #     finalbagiansuami = 0
        #     ambil_bagian_harta = finalbagiansuami
        # else:
        #     if(ayah == "0" and ibu == "0" and kakek == "0" and nenek == 0):
        #         suku_bagian = harta / totalasalmasalah
        #         finalbagiansuami = asalmasalah_suami * suku_bagian
        #         ambil_bagian_harta = finalbagiansuami
        #     else:
        #         finalbagiansuami = asalmasalah_suami * suku_bagian
        #         ambil_bagian_harta = finalbagiansuami 
        
        #new
        suku_bagian = harta / asalmasalah
        if (asalmasalah_suami == 0):
            finalbagiansuami = 0
            ambil_bagian_harta = finalbagiansuami
        else:
            finalbagiansuami = asalmasalah_suami * suku_bagian
            ambil_bagian_harta = finalbagiansuami
    else:
        suku_bagian = harta / asalmasalah
        if (asalmasalah_istri == 0):
            finalbagianistri = 0
            ambil_bagian_harta = finalbagianistri
        else:
            finalbagianistri = asalmasalah_istri * suku_bagian
            ambil_bagian_harta = finalbagianistri
    # hitung harta ibu
    if (asalmasalah_ibu == 0):
        finalbagianibu = 0
    else:
        sisa_harta = harta - ambil_bagian_harta
        if (bagiansisaibu == "*sisa"):
            if (ayah == "y"):
                asalmasalah_sisa = asalmasalah_ibu + asalmasalah_ayah
                suku_bagian = sisa_harta / asalmasalah_sisa
                finalbagianibu = asalmasalah_ibu * suku_bagian
            else:
                finalbagianibu = asalmasalah_ibu * suku_bagian
        else:
            if(ayah == "0" and kakek == "0" and anak_pr == 1 and ibu == "y" and cucu_lk == 0):
                if(cucu_pr > 0):
                    asalmasalah_sisa = asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_cucupr
                else:
                    asalmasalah_sisa = asalmasalah_ibu + asalmasalah_anakpr
                tampil = "ubah"
                sisa_harta = harta - ambil_bagian_harta
                finalbagianibu = (sisa_harta * asalmasalah_ibu) / int(asalmasalah_sisa)
            elif(ayah == "0" and kakek == "0" and anak_pr == 0 and ibu == "y" and cucu_lk == 0):
                if(cucu_pr > 0):
                    tampil = "ubah"
                    asalmasalah_sisa = asalmasalah_ibu + asalmasalah_cucupr
                    sisa_harta = harta - ambil_bagian_harta
                    finalbagianibu = (sisa_harta * asalmasalah_ibu) / int(asalmasalah_sisa)
                else:
                    finalbagianibu = suku_bagian * asalmasalah_ibu
            elif(ayah == "0"  and kakek == "0" and anak_pr > 1 and ibu == "y" and cucu_lk == 0):
                tampil = "ubah"
                asalmasalah_sisa = asalmasalah_ibu + asalmasalah_anakpr
                sisa_harta = harta - ambil_bagian_harta
                finalbagianibu = (sisa_harta * asalmasalah_ibu) / int(asalmasalah_sisa)
            else:
                finalbagianibu = suku_bagian * asalmasalah_ibu
    # perhitungan bagian nenek
    # if(asalmasalah_nenek != 0):
    #     if(ayah == "0" and kakek =="0" and anak_lk == 0 and anak_pr == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudara_sayah == 0 and saudari_sayah == 0 and saudara_sibu == 0 and saudari_sibu == 0):
    #         sisa_harta_nenek = harta - ambil_bagian_harta
    #         finalbagiannenek = asalmasalah_nenek * sisa_harta_nenek
    #     else:
    #         finalbagiannenek = (asalmasalah_nenek * harta) / asalmasalah
    # else:
    #     finalbagiannenek = 0
    if (asalmasalah_nenek == 0):
        finalbagiannenek = 0
    else:
        sisa_harta = harta - ambil_bagian_harta
        if(ayah == "0" and kakek == "0" and anak_pr == 1 and nenek > 0 and cucu_lk == 0):
            if(cucu_pr > 0):
                asalmasalah_sisa = asalmasalah_nenek + asalmasalah_anakpr + asalmasalah_cucupr
            else:
                asalmasalah_sisa = asalmasalah_nenek + asalmasalah_anakpr
            tampil = "ubah"
            sisa_harta = harta - ambil_bagian_harta
            finalbagiannenek = (sisa_harta * asalmasalah_nenek) / int(asalmasalah_sisa)
        elif(ayah == "0" and kakek == "0" and anak_pr == 0 and nenek > 0 and cucu_lk == 0):
            if(cucu_pr > 0):
                tampil = "ubah"
                sisa_harta = harta - ambil_bagian_harta
                asalmasalah_sisa = asalmasalah_nenek + asalmasalah_cucupr
                finalbagiannenek = (sisa_harta * asalmasalah_nenek) / int(asalmasalah_sisa)
            else:
                finalbagiannenek = suku_bagian * asalmasalah_nenek
        elif(ayah == "0"  and kakek == "0" and anak_pr > 1 and nenek > 0 and cucu_lk == 0):
            tampil = "ubah"
            asalmasalah_sisa = asalmasalah_nenek + asalmasalah_anakpr
            sisa_harta = harta - ambil_bagian_harta
            finalbagiannenek = (sisa_harta * asalmasalah_nenek) / int(asalmasalah_sisa)
        else:
            finalbagiannenek = suku_bagian * asalmasalah_nenek
    # hitung harta anak perempuan  
    finalbagiananakpr = asalmasalah_anakpr * suku_bagian
    #hitung harta kakek
    # if (asalmasalah_kakek == 0):
    #     finalbagiankakek = 0
    # else:
    #     if (bagiankakek == "sisa" and bagiansisakakek == ""):
    #         finalbagiankakek = suku_bagian * asalmasalah_kakek
    #         sisa_harta = harta - ambil_bagian_harta - \
    #             finalbagianibu - finalbagiananakpr - finalbagiannenek - finalbagiankakek
    #     elif (bagianayah == 0.16 and bagiansisa == "+sisa"):
    #         asalmasalah_sisa = sisa
    #         finalbagiankakek = suku_bagian * asalmasalah_kakek
    #     else:
    #         finalbagikakek = suku_bagian * asalmasalah_kakek
        
    # hitung harta ayah
    if (asalmasalah_ayah == 0):
        finalbagianayah = 0
    else:
        if (bagianayah == "sisa" and bagiansisa == ""):
            finalbagianayah = suku_bagian * asalmasalah_ayah
            sisa_harta = harta - ambil_bagian_harta - finalbagianibu - finalbagiananakpr - finalbagianayah - finalbagiannenek
        elif (bagianayah == 0.16 and bagiansisa == "+sisa"):
            asalmasalah_sisa = sisa
            finalbagianayah = suku_bagian * asalmasalah_ayah
        else:
            finalbagianayah = suku_bagian * asalmasalah_ayah
    #batas hitung harta ayah
    # hitung harta kakek
    if (asalmasalah_kakek == 0):
        finalbagiankakek = 0
    else:
        if (bagiankakek == "sisa" and bagiansisakakek == ""):
            finalbagiankakek = suku_bagian * asalmasalah_kakek
            sisa_harta = harta - ambil_bagian_harta - finalbagianibu - finalbagiananakpr - finalbagiankakek - finalbagiannenek
            # suku_bagian = sisa_harta / asalmasalah_sisa
        elif (bagiankakek == 0.16 and bagiansisakakek == "+sisa"):
            asalmasalah_sisa = sisa
            finalbagiankakek = suku_bagian * asalmasalah_kakek
        else:
            finalbagiankakek = suku_bagian * asalmasalah_kakek
    # batas hitung harta kakek
    print("=" * 20)
    if(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
        if(ayah == "0" and ibu == "y"):
            sisa_harta = harta - finalbagianibu - ambil_bagian_harta
        else :
            sisa_harta = harta - finalbagianayah - finalbagianibu - \
            finalbagiananakpr - ambil_bagian_harta - finalbagiankakek - finalbagiannenek
    else:
        if(ayah == "0" and ibu == "y"):
            sisa_harta = harta - ambil_bagian_harta - finalbagianibu
        else :
            sisa_harta = harta - finalbagianayah - finalbagianibu - \
            finalbagiananakpr - ambil_bagian_harta - finalbagiankakek - finalbagiannenek
    if(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
        if(tampil == "ubah"):
            if(anak_pr > 0 and nenek > 0):
                asalmasalah_ubah = asalmasalah_nenek + asalmasalah_anakpr + asalmasalah_cucupr
                print(f"Asal Masalah Sisa {sisa}")
                print(f"Siham Anak Perempuan : {asalmasalah_anakpr}")
                if(cucu_pr > 0):
                    print(f"Siham Cucu Perempuan : {asalmasalah_cucupr}")
                print(f"Siham Nenek : {asalmasalah_nenek}")
                print(f"Asal Masalah Awal : 6")
                print(f"Asal Masalah Menjadi : {int(asalmasalah_ubah)}")
                print("=" * 20)
            elif(anak_pr > 0 and ibu == "y"):
                asalmasalah_ubah = asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_cucupr
                print(f"Asal Masalah Sisa {sisa}")
                print(f"Siham Anak Perempuan : {asalmasalah_anakpr}")
                if(cucu_pr > 0):
                    print(f"Siham Cucu Perempuan : {asalmasalah_cucupr}")
                print(f"Siham Ibu : {asalmasalah_ibu}")
                print(f"Asal Masalah Awal : 6")
                print(f"Asal Masalah Menjadi : {int(asalmasalah_ubah)}")
                print("=" * 20)
            else:
                if(cucu_pr > 0 and ibu == "y"):
                    asalmasalah_ubah = asalmasalah_ibu +  asalmasalah_cucupr
                    print(f"Asal Masalah Sisa {sisa}")
                    print(f"Siham Cucu Perempuan : {asalmasalah_cucupr}")
                    print(f"Siham Ibu : {asalmasalah_ibu}")
                    print(f"Asal Masalah Awal : 6")
                    print(f"Asal Masalah Menjadi : {int(asalmasalah_ubah)}")
                    print("=" * 20)
                elif(cucu_pr > 0 and nenek > 0):
                    asalmasalah_ubah = asalmasalah_nenek +  asalmasalah_cucupr
                    print(f"Asal Masalah Sisa {sisa}")
                    print(f"Siham Cucu Perempuan : {asalmasalah_cucupr}")
                    print(f"Siham Nenek : {asalmasalah_nenek}")
                    print(f"Asal Masalah Awal : 6")
                    print(f"Asal Masalah Menjadi : {int(asalmasalah_ubah)}")
                    print("=" * 20)
                else:
                    print(f"Asal Masalah Awal : {int(asalmasalah)}")
                    print(f"Asal Masalah Menjadi : {int(jumlahasalmasalah)}")
        else:
            print(f"Asal Masalah Sisa : {int(asalmasalah - jumlahasalmasalah)}")
    else :
        if(tampil == "ubah"):
            if(anak_pr > 0 and nenek > 0):
                asalmasalah_ubah = asalmasalah_nenek + asalmasalah_anakpr + asalmasalah_cucupr
                print(f"Asal Masalah Sisa {sisa}")
                print(f"Siham Anak Perempuan : {asalmasalah_anakpr}")
                if(cucu_pr > 0):
                    print(f"Siham Cucu Perempuan : {asalmasalah_cucupr}")
                print(f"Siham Nenek : {asalmasalah_nenek}")
                print(f"Asal Masalah Awal : 6")
                print(f"Asal Masalah Menjadi : {int(asalmasalah_ubah)}")
                print("=" * 20)
            elif(anak_pr > 0 and ibu == "y"):
                asalmasalah_ubah = asalmasalah_ibu + asalmasalah_anakpr + asalmasalah_cucupr
                print(f"Asal Masalah Sisa {sisa}")
                print(f"Siham Anak Perempuan : {asalmasalah_anakpr}")
                if(cucu_pr > 0):
                    print(f"Siham Cucu Perempuan : {asalmasalah_cucupr}")
                print(f"Siham Ibu : {asalmasalah_ibu}")
                print(f"Asal Masalah Awal : 6")
                print(f"Asal Masalah Menjadi : {int(asalmasalah_ubah)}")
                print("=" * 20)
            else:
                if(cucu_pr > 0 and ibu == "y"):
                    asalmasalah_ubah = asalmasalah_ibu +  asalmasalah_cucupr
                    print(f"Asal Masalah Sisa {sisa}")
                    print(f"Siham Cucu Perempuan : {asalmasalah_cucupr}")
                    print(f"Siham Ibu : {asalmasalah_ibu}")
                    print(f"Asal Masalah Awal : 6")
                    print(f"Asal Masalah Menjadi : {int(asalmasalah_ubah)}")
                    print("=" * 20)
                elif(cucu_pr > 0 and nenek > 0):
                    asalmasalah_ubah = asalmasalah_nenek +  asalmasalah_cucupr
                    print(f"Asal Masalah Sisa {sisa}")
                    print(f"Siham Cucu Perempuan : {asalmasalah_cucupr}")
                    print(f"Siham Nenek : {asalmasalah_nenek}")
                    print(f"Asal Masalah Awal : 6")
                    print(f"Asal Masalah Menjadi : {int(asalmasalah_ubah)}")
                    print("=" * 20)
                else:
                    print(f"Asal Masalah Awal : {int(asalmasalah)}")
                    print(f"Asal Masalah Menjadi : {int(jumlahasalmasalah)}")
        else:
            print(f"Asal Masalah Sisa : {int(sisa)}")
    # bagian cucu laki dan cucu perempuan
    finalbagiancucupr = 0
    finalbagiancuculk = 0
    sisa_cucu = 0
    cucu = ""
    if(cucu_pr > 0 and cucu_lk == 0):
        cucu = "kondisi1"
        finalbagiancuculk = 0  
        if(bagiancucupr != "termahjub") :  
            if (cucu_pr > 0 and anak_pr > 0):
                if(ayah == "0" and kakek == "0"):
                    if(ibu == "y"):
                        asalmasalah_sisa = asalmasalah_anakpr + asalmasalah_cucupr + asalmasalah_ibu
                    else:
                        if(nenek > 0):
                            asalmasalah_sisa = asalmasalah_anakpr + asalmasalah_cucupr + asalmasalah_nenek
                        else:
                            asalmasalah_sisa = asalmasalah_anakpr + asalmasalah_cucupr
                    sisa_harta_cucu_pr = harta - ambil_bagian_harta
                    suku_bagian_cucu = sisa_harta_cucu_pr / asalmasalah_sisa
                else:
                    suku_bagian_cucu = harta / asalmasalah
                finalbagiancucupr = asalmasalah_cucupr * suku_bagian_cucu
                # sisa_harta_cucu_pr = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek
            elif (cucu_pr > 0 and anak_pr == 0):
                if(ayah == "0" and kakek == "0"):
                    if(ibu == "y"):
                        asalmasalah_sisa = asalmasalah_anakpr + asalmasalah_cucupr + asalmasalah_ibu
                    else:
                        if(nenek > 0):
                            asalmasalah_sisa = asalmasalah_anakpr + asalmasalah_cucupr + asalmasalah_nenek
                        else:
                            asalmasalah_sisa = asalmasalah_anakpr + asalmasalah_cucupr
                    sisa_harta_cucu_pr = harta - ambil_bagian_harta
                    suku_bagian_cucu = sisa_harta_cucu_pr / asalmasalah_sisa
                else:
                    suku_bagian_cucu = harta / asalmasalah
                finalbagiancucupr = asalmasalah_cucupr * suku_bagian_cucu
                # sisa_harta_cucu_pr = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu - finalbagiannenek - finalbagiankakek
            
            else:
                finalbagiancucupr = asalmasalah_cucupr * suku_bagian
        else:
            finalbagiancucupr = 0
    elif(cucu_pr == 0 and cucu_lk > 0):
        if(bagiancuculk != "termahjub"):
            cucu = "kondisi2"
            sisa_harta_cucu = harta - ambil_bagian_harta - finalbagiananakpr - finalbagianayah - finalbagiankakek - finalbagianibu - finalbagiannenek
            sisa_harta_cucu_lk = (1 * sisa_harta_cucu)
            finalbagiancuculk = sisa_harta_cucu_lk * cucu_lk
        else:
            finalbagiancuculk = 0
        sisa_cucu = finalbagiancuculk
    
    elif(cucu_pr > 0 and cucu_lk > 0):
        cucu = "kondisi3"
        asalmasalah_sisa_cucu = asalmasalah_cucupr + asalmasalah_cuculk
        sisa_harta_cucu = harta - ambil_bagian_harta - finalbagiananakpr - finalbagianayah - finalbagiankakek - finalbagianibu - finalbagiannenek
        suku_bagian_cucu = sisa_harta_cucu / asalmasalah_sisa_cucu
        sisa_harta_cucu_pr = (1 * suku_bagian_cucu)
        sisa_harta_cucu_lk = (2 * suku_bagian_cucu)
        if(bagiancucupr != "termahjub"):
            finalbagiancucupr = sisa_harta_cucu_pr * cucu_pr
        else:
            finalbagiancucupr = 0
        if(bagiancuculk != "termahjub"):
            finalbagiancuculk = sisa_harta_cucu_lk * cucu_lk
        else:
            finalbagiancuculk = 0
        sisa_cucu = finalbagiancucupr + finalbagiancuculk 
    # tampil bagian suami
    if (suami == "y"):
            print(f"Bagian Harta Suami : {round(finalbagiansuami, 2)}")
    else:
        # tampil bagian istri jika lebih 1 harta per istri
        if (istri > 1):
            bagi_harta_istri = finalbagianistri / istri
            print(f"Bagian Harta Istri : {round(finalbagianistri, 2)}")
            j = 1
            while j <= istri:
                print("Harta Untuk Istri Ke- ",
                        j, " = ", bagi_harta_istri)
                j += 1
        else:
            if (istri != 0):
                print(f"Bagian Harta Istri : {round(finalbagianistri, 2)}")
    if (bagianayah == 0.16 and bagiansisa == "+sisa"):
        sisa_harta_ayah = harta - ambil_bagian_harta - finalbagianayah - finalbagiananakpr - finalbagianibu - finalbagiannenek - finalbagiancucupr
        print(
            f"Bagian Harta Ayah 1/6 + sisa: {round(finalbagianayah, 2)} + {round(sisa_harta_ayah, 2)}")
        print(f"Harta untuk ayah =  {round(finalbagianayah + sisa_harta_ayah , 2)}")
    else:
        sisa_harta_ayah = 0
        if(ayah == "y"):
            print(f"Bagian Harta Ayah : {round(finalbagianayah)}")
    if(ibu == "y"):
        print(f"Bagian Harta Ibu : {round(finalbagianibu, 2)}")
    if (nenek > 1):
            bagi_harta_nenek = finalbagiannenek / nenek
            print(f"Bagian Harta Nenek : {round(finalbagiannenek, 2)}")
            j = 1
            while j <= nenek:
                print("Harta Untuk Nenek Ke- ",
                      j, " = ", round(bagi_harta_nenek, 2))
                j += 1
    else:
        if (nenek != 0):
            print(f"Bagian Harta Nenek : {round(finalbagiannenek, 2)}")
    if (bagiankakek == 0.16 and bagiansisakakek == "+sisa"):
        sisa_harta_kakek = harta - ambil_bagian_harta - finalbagiankakek - finalbagiananakpr - finalbagianibu - finalbagiannenek - finalbagiancucupr
        print(
            f"Bagian Harta Kakek 1/6 + sisa: {round(finalbagiankakek, 2)} + {round(sisa_harta_kakek, 2)}")
        print(f"Harta untuk kakek =  {round(finalbagiankakek + sisa_harta_kakek, 2)}")
    else:
        sisa_harta_kakek = 0
        if(kakek == "y"):
            print(f"Bagian Harta Kakek : {round(finalbagiankakek, 2)}")
    if (anak_pr > 1):
        sisa_harta = harta - ambil_bagian_harta
        if(ayah == "0" and ibu == "0"):
            if(kakek == "y" and nenek > 0):
                # sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - finalbagiannenek - sisa_harta_kakek
                # if(cucu_lk > 0):
                #     sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - finalbagiannenek - sisa_harta_kakek - sisa_cucu
                # else:
                #     sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - finalbagiannenek - sisa_harta_kakek - finalbagiancucupr
                # suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                # finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr 
                finalbagiananakpr = finalbagiananakpr
            elif(kakek == "0" and nenek > 0):
                if(cucu_lk > 0):
                    sisa_harta = harta - ambil_bagian_harta - finalbagiannenek - sisa_cucu
                else:
                    sisa_harta = harta - ambil_bagian_harta - finalbagiannenek - finalbagiancucupr
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
            elif(kakek == "y" and nenek == 0):
                if(bagiankakek == 0.16 and bagiansisakakek == "+sisa"):
                    if(cucu_lk > 0):
                        sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - sisa_harta_kakek - sisa_cucu
                    else:
                        sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - sisa_harta_kakek - finalbagiancucupr 
                    suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                    finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
                else:
                    if(cucu_lk > 0):
                        sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - sisa_cucu
                    else:
                        sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - finalbagiancucupr
                    suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                    finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
            else:
                if(cucu_lk > 0):
                    sisa_harta = harta - ambil_bagian_harta - sisa_cucu
                else:
                    sisa_harta = harta - ambil_bagian_harta - finalbagiancucupr
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr 
                # suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                # finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
        elif(ayah == "0" and ibu == "y"):
            if(kakek == "y"):
                if(cucu_lk > 0):
                    sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - sisa_cucu
                else:
                    sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - finalbagiancucupr
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr 
            else:
                if(cucu_lk > 0):    
                    sisa_harta = harta - ambil_bagian_harta - finalbagianibu - sisa_cucu
                else:
                    sisa_harta = harta - ambil_bagian_harta - finalbagianibu - finalbagiancucupr
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
        elif(ayah == "y" and ibu == "0"):
            if(nenek > 0):
                # sisa_harta = harta - ambil_bagian_harta - finalbagiannenek
                if(cucu_lk > 0):
                    sisa_harta = harta - ambil_bagian_harta - finalbagiannenek - sisa_harta_ayah - finalbagianayah - sisa_cucu
                else:
                    sisa_harta = harta - ambil_bagian_harta - finalbagiannenek - sisa_harta_ayah - finalbagianayah - finalbagiancucupr
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr 
            else: 
                if(bagianayah == 0.16 and bagiansisa == "+sisa"):
                    sisa_harta = harta - ambil_bagian_harta - finalbagianayah - sisa_harta_ayah - finalbagiancucupr
                    suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                    finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
                else:
                    if(cucu_lk > 0):
                        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - sisa_cucu
                    else:
                        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagiancucupr
                    suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                    finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
        print(f"Bagian Harta Anak Perempuan : {round(finalbagiananakpr, 2)}")
        sisa_harta_anak_pr = finalbagiananakpr / anak_pr
        # pembagian harta per anak perempuan
        i = 1
        while i <= anak_pr:
            print("Harta Untuk Anak Perempuan ", i, " = ", round(sisa_harta_anak_pr, 2))
            i += 1
    elif (anak_pr == 1):
        if(ayah == "0" and ibu == "0"):
            if(kakek == "y" and nenek > 0):
                # if(cucu_lk > 0):
                #     sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - finalbagiannenek - sisa_harta_kakek - sisa_cucu
                # else:
                #     sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - finalbagiannenek - sisa_harta_kakek - finalbagiancucupr
                # suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                # finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
                finalbagiananakpr = finalbagiananakpr
            elif(kakek == "0" and nenek > 0):
                if(cucu_lk > 0):
                    sisa_harta = harta - ambil_bagian_harta - finalbagiannenek - sisa_cucu
                else:
                    sisa_harta = harta - ambil_bagian_harta - finalbagiannenek - finalbagiancucupr
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
            elif(kakek == "y" and nenek == 0):
                if(bagiankakek == 0.16 and bagiansisakakek == "+sisa"):
                    if(cucu_lk > 0):
                        sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - sisa_harta_kakek - sisa_cucu
                    else:
                        sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - sisa_harta_kakek - finalbagiancucupr
                    suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                    finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
                else:
                    if(cucu_lk > 0):
                        sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - sisa_cucu
                    else:
                        sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - finalbagiancucupr
                    suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                    finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
            else:
                if(cucu_lk > 0):
                    sisa_harta = harta - ambil_bagian_harta - sisa_cucu
                else:
                    sisa_harta = harta - ambil_bagian_harta - finalbagiancucupr
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr 
        elif(ayah == "0" and ibu == "y"):
            if(kakek == "y"):
                if(cucu_lk > 0):
                    sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - finalbagianibu - sisa_harta_kakek - sisa_cucu
                else:
                    sisa_harta = harta - ambil_bagian_harta - finalbagiankakek - finalbagianibu - sisa_harta_kakek - finalbagiancucupr
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr 
            else:
                if(cucu_lk > 0):
                    sisa_harta = harta - ambil_bagian_harta - finalbagianibu - sisa_cucu
                else:
                    sisa_harta = harta - ambil_bagian_harta - finalbagianibu - finalbagiancucupr
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
        elif(ayah == "y" and ibu == "0"):
            if(nenek > 0):
                # sisa_harta = harta - ambil_bagian_harta - finalbagiannenek
                if(cucu_lk > 0):
                    sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagiannenek - sisa_harta_ayah - sisa_cucu
                else:
                    sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagiannenek - sisa_harta_ayah - finalbagiancucupr
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr 
            else: 
                if(bagianayah == 0.16 and bagiansisa == "+sisa"):
                    if(cucu_lk > 0):
                        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - sisa_harta_ayah - sisa_cucu
                    else:
                        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - sisa_harta_ayah - finalbagiancucupr
                    suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                    finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
                else:
                    if(cucu_lk > 0):
                        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - sisa_cucu
                    else:
                        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagiancucupr
                    suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                    finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr 
        print(f"Bagian Harta Anak Perempuan : {round(finalbagiananakpr, 2)}")
    # bagian harta cucu pr
    if(cucu == "kondisi1"):
        if(bagiancucupr != "termahjub"):
            print(f"Bagian Harta Cucu Perempuan : {round(finalbagiancucupr, 2)}")
            if(finalbagiancucupr == 0):
                sisa_harta_cucu_pr = 0
            else:    
                sisa_harta_cucu_pr = finalbagiancucupr / cucu_pr
            # pembagian harta per cucu perempuan
            if(cucu_pr > 1):
                i = 1
                while i <= cucu_pr:
                    print("Harta Untuk Cucu Perempuan ", i, " = ", round(sisa_harta_cucu_pr, 2))
                    i += 1
    elif(cucu == "kondisi2"):
        # pembagian harta per cucu laki-laki
        if(bagiancuculk != "termahjub"):
            print(f"Harta Cucu Laki-Laki : {round(finalbagiancuculk, 2)}")
            if(cucu_lk > 1):
                j = 1
                while j <= cucu_lk:
                    print("Harta Untuk Cucu Laki - Laki ",
                            j, " = ", round(sisa_harta_cucu_lk, 2))
                    j += 1
    elif(cucu == "kondisi3"):
        # pembagian harta per cucu perempuan
        if(bagiancucupr != "termahjub"):
            print(f"Harta Cucu Perempuan : {round(finalbagiancucupr, 2)}")
            if(cucu_pr > 1):
                i = 1
                while i <= cucu_pr:
                    print("Harta Untuk Cucu Perempuan ",
                            i, " = ", round(sisa_harta_cucu_pr, 2))
                    i += 1
        # pembagian harta per cucu laki-laki
        if(bagiancuculk != "termahjub"):
            print(f"Harta Cucu Laki-Laki : {round(finalbagiancuculk, 2)}")
            if(cucu_lk > 1):
                j = 1
                while j <= cucu_lk:
                    print("Harta Untuk Cucu Laki - Laki ",
                            j, " = ", round(sisa_harta_cucu_lk, 2))
                    j += 1