pewaris = input("Pewaris : ")
harta = 0
suami = ""
istri = 0
ayah = ""
ibu = ""
kakek = 0
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
kakek = int(input("Masukan Jumlah kakek? : "))
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
        if (kakek > 0):
            if (anak_pr == 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk == 0):
                bagiankakek = "sisa"
                print(f"Bagian kakek {bagiankakek}")
            elif (anak_pr > 0 and anak_lk == 0 and cucu_pr > 0 and cucu_lk == 0):
                bagiankakek = 0.16
                bagiansisakakek = "+sisa"
                print(f"Bagian kakek {bagiankakek} {bagiansisakakek}")
            elif (anak_pr > 0 and cucu_pr == 0 and anak_lk == 0 and cucu_lk == 0):
                bagiankakek = 0.16
                bagiansisakakek = "+sisa"
                print(f"Bagian kakek {bagiankakek} {bagiansisakakek}")
            elif (anak_pr == 0 and cucu_pr > 0 and anak_lk == 0 and cucu_lk == 0):
                bagiankakek = 0.16
                bagiansisakakek = "+sisa"
                print(f"Bagian kakek {bagiankakek} {bagiansisakakek}")
            elif (anak_pr > 0 and cucu_pr > 0 and anak_lk > 0 and cucu_lk > 0):
                bagiankakek = 0.16
                print(f"Bagian kakek {bagiankakek}")
            elif (anak_pr > 0 and cucu_pr == 0 and anak_lk > 0 and cucu_lk == 0):
                bagiankakek = 0.16
                print(f"Bagian kakek {bagiankakek}")
            elif (anak_pr > 0 and cucu_pr == 0 and anak_lk == 0 and cucu_lk > 0):
                bagiankakek = 0.16
                print(f"Bagian kakek {bagiankakek}")
            elif (anak_pr == 0 and cucu_pr > 0 and anak_lk == 0 and cucu_lk > 0):
                bagiankakek = 0.16
                print(f"Bagian kakek {bagiankakek}")
            elif (anak_pr == 0 and cucu_pr > 0 and anak_lk > 0 and cucu_lk == 0):
                bagiankakek = 0.16
                print(f"Bagian kakek {bagiankakek}")
            elif (anak_pr == 0 and cucu_pr == 0 and anak_lk > 0 and cucu_lk > 0):
                bagiankakek = 0.16
                print(f"Bagian kakek {bagiankakek}")
            elif (anak_pr == 0 and cucu_pr == 0 and anak_lk > 0 and cucu_lk == 0):
                bagiankakek = 0.16
                print(f"Bagian kakek {bagiankakek}")
            elif (anak_pr == 0 and cucu_pr == 0 and anak_lk == 0 and cucu_lk > 0):
                bagiankakek = 0.16
                print(f"Bagian kakek {bagiankakek}")
if (kakek < 3 and kakek != 0):
    if (ayah == "y" or ayah == "ada"):
        bagiankakek = "termahjub"
        print(f"bagian kakek  {bagiankakek}")
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
    # print(f"Bagian ibu {bagianibu}")
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
if (ayah == "0" and kakek == 0 and anak_lk == 0 and cucu_lk == 0):
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
elif (ayah == "y" or kakek > 0 or anak_lk > 0 or cucu_lk > 0):
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
# elif (ayah == "0" and kakek == 0 and anak_lk == 0 and cucu_lk > 0):
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
# elif (ayah == "0" and kakek == 0 and anak_lk > 0 and cucu_lk > 0):
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
# elif (ayah == "y" and kakek >= 0 and anak_lk > 0 and cucu_lk > 0):
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
if (ayah == "0" and kakek == 0 and anak_lk == 0 and cucu_lk == 0 and saudara_knd == 0):
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
elif (ayah == "y" or kakek >= 1 or anak_lk >= 1 or cucu_lk >= 1 or saudara_knd >= 1):
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
if (ayah == "0" and kakek == 0 and anak_pr == 0 and anak_lk == 0 and cucu_pr == 0 and cucu_lk == 0):
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
elif (ayah == "y" or kakek >= 1 or anak_pr >= 0 or anak_lk >= 0 or cucu_pr >= 0 or cucu_lk >= 0):
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
        if (ayah == "0" and kakek == 0 and anak_lk == 0):
            asalmasalah = 8
        else:
            if(ayah == "0" and ibu == "0" and kakek == 0 and nenek == 0):
                asalmasalah = 8
            else:
                asalmasalah = 24
    elif (bagianIstri == 0.25):
        if(kakek == 0 and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
            print("Asal Masalah Awal 4 Menjadi ", asalmasalah)
        else:
            asalmasalah = 4
    elif (istri == 0 and bagianIstri == 0):
        if(kakek == 0 and nenek == 0 and ayah == "y" and ibu == "y" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 3
        else:
            asalmasalah = 6
elif (pewaris == "istri" or pewaris == "Istri" or pewaris == "2" or pewaris == "ISTRI"):
    if (bagiansuami == 0.5):
        if(kakek == 0 and nenek == 0 and ayah == "0" and ibu == "0" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 1
            print("Asal Masalah Awal 2 Menjadi ", asalmasalah)
        else:
            asalmasalah = 2
    elif (bagiansuami == 0.25):
        if(kakek == 0 and nenek == 0 and ayah == "0" and ibu == "0"):
            if(anak_pr > 1):
                asalmasalah = 12
            else:
                asalmasalah = 4
        else:
            asalmasalah = 12
    elif (bagiansuami == 0):
        if(kakek == 0 and nenek == 0 and ayah == "y" and ibu == "y" and anak_pr == 0 and anak_lk == 0 and cucu_lk == 0 and cucu_pr == 0 and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
            asalmasalah = 3
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
        if(kakek == 0 and nenek == 0 and ayah == "0" and ibu == "0" and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
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
        if(kakek == 0 and nenek == 0 and ayah == "0" and ibu == "0" and saudara_knd == 0 and saudari_knd == 0 and saudari_sayah == 0 and saudara_sayah == 0 and saudari_sibu == 0 and saudara_sibu == 0):
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
        hitungasalmasalah_ibu = (asalmasalah / 6) * 1
        asalmasalah_ibu = int(hitungasalmasalah_ibu)
        print(f"Tampil Siham Masalah Ibu : {asalmasalah_ibu}")
else:
    asalmasalah_ibu = 0

# asal masalah ayah
if (ayah == "y"):
    if (bagianayah == "sisa"):
        asalmasalah_ayah = 2
        print(f"Tampil Siham Masalah Ayah : {asalmasalah_ayah}")
    else:
        hitungasalmasalah_ayah = (asalmasalah / 6) * 1
        asalmasalah_ayah = int(hitungasalmasalah_ayah)
        print(f"Tampil Siham Masalah Ayah : {asalmasalah_ayah}")
else:
    asalmasalah_ayah = 0

#################################### Hitung Asal Masalah ###################################
# tanpa anak
if (anak_lk == 0 and anak_pr == 0):
    # mengambil nilai asal masalah suami/istri
    if (suami == "y"):
        ambil_asalmasalah = asalmasalah_suami
    else:
        ambil_asalmasalah = asalmasalah_istri
    # batas mendapatkan nilai
    # totalasalmasalah = ambil_asalmasalah
    totalasalmasalah = ambil_asalmasalah + asalmasalah_ayah + asalmasalah_ibu
    sisa = asalmasalah - totalasalmasalah
    jumlahasalmasalah = asalmasalah
elif (anak_pr > 0 and anak_lk == 0):
    # asal masalah anak perempuan lebih dari 1 dan tanpa anak laki-laki
    if (anak_pr > 1 and anak_lk == 0):
        if(pewaris == "suami" or pewaris == "Suami" or pewaris == "SUAMI" or pewaris == "1"):
            if (ayah == "0" and kakek == 0 and cucu_pr == 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (6 / 3) * 2
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            else:
                hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            print(
                f"Tampil Siham Masalah Anak Perempuan : {asalmasalah_anakpr}")
        elif(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
            if (ayah == "0" and ibu == "y" and kakek == 0 and cucu_pr == 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            elif(ibu == "0" and ayah == "0" and kakek == 0 and cucu_pr == 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            else:
                hitungasalmasalah_anakpr = (asalmasalah / 3) * 2
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            print(
                f"Tampil Siham Masalah Anak Perempuan : {asalmasalah_anakpr}")
    elif (anak_pr > 1 and anak_lk > 0):
        if (ayah == "0" and kakek == 0 and cucu_pr == 0 and cucu_lk == 0):
            hitungasalmasalah_anakpr = (6 / 4) * 1
            asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
        else:
            hitungasalmasalah_anakpr = (asalmasalah / 4) * 1
            asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
        print(
            f"Tampil Siham Masalah Anak Perempuan : {asalmasalah_anakpr}")
    elif (anak_pr == 1 and anak_lk == 0):
        if(pewaris == "suami" or pewaris == "Suami" or pewaris == "SUAMI" or pewaris == "1"):
            if (ayah == "0" and ibu == "y" and kakek == 0 and cucu_pr == 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (6 / 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            elif(ibu == "0" and ayah == "0" and kakek == 0 and cucu_pr == 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (2/ 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            else:
                hitungasalmasalah_anakpr = (asalmasalah / 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            print(
                f"Tampil Siham Masalah Anak Perempuan : {asalmasalah_anakpr}")
        elif(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
            if (ayah == "0" and ibu == "y" and kakek == 0 and cucu_pr == 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (asalmasalah / 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            elif(ibu == "0" and ayah == "0" and kakek == 0 and cucu_pr == 0 and cucu_lk == 0):
                hitungasalmasalah_anakpr = (4 / 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            else:
                hitungasalmasalah_anakpr = (asalmasalah / 2) * 1
                asalmasalah_anakpr = int(hitungasalmasalah_anakpr)
            print(
                f"Tampil Siham Masalah Anak Perempuan : {asalmasalah_anakpr}")
    elif (anak_pr == 0):
        asalmasalah_anakpr = 0
    # totalasalmasalah dengan anak perempuan tanpa anak lk
    # mengambil nilai asal masalah suami/istri
    if (suami == "y"):
        ambil_asalmasalah = asalmasalah_suami
    else:
        ambil_asalmasalah = asalmasalah_istri
    totalasalmasalah = ambil_asalmasalah + \
        asalmasalah_ayah + asalmasalah_ibu + asalmasalah_anakpr
    sisa = asalmasalah - totalasalmasalah
    jumlahasalmasalah = totalasalmasalah
else:
    # mengambil nilai asal masalah suami/istri
    if (suami == "y"):
        ambil_asalmasalah = asalmasalah_suami
    else:
        ambil_asalmasalah = asalmasalah_istri
    # batas mendapatkan nilai
    totalasalmasalah = ambil_asalmasalah + \
        asalmasalah_ayah + asalmasalah_ibu
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
    # penghitungan bagian ayah / kakek
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
    # batas antisipasi Zero division error
    print("=" * 50)

    if (suami == "y"):
        print(f"Bagian Harta Suami : {int(finalbagiansuami)}")
    else:
        # tampil bagian istri jika lebih 1 harta per istri
        if (istri > 1):
            bagi_harta_istri = finalbagianistri / istri
            print(f"Bagian Harta Istri : {int(finalbagianistri)}")
            j = 1
            while j <= istri:
                print("Harta Untuk Istri Ke- ",
                      j, " = ", bagi_harta_istri)
                j += 1
        else:
            if (istri != 0):
                print(f"Bagian Harta Istri : {int(finalbagianistri)}")
    print(f"Bagian Harta Ayah : {int(finalbagianayah)}")
    print(f"Bagian Harta Ibu : {int(finalbagianibu)}")
    if (anak_pr > 0 or anak_lk > 0):
        if (anak_pr > 0 and anak_lk == 0):
            asalmasalah_anakpr = (1 * anak_pr)
            asalmasalah_sisa = asalmasalah_anakpr
            sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
            print(f"Sisa Harta : {int(sisa_harta)}")
            suku_bagian = sisa_harta / asalmasalah_sisa
            sisa_harta_anak_pr = (1 * suku_bagian)
            bagianharta_anak_pr = sisa_harta_anak_pr * anak_pr
            print(f"Harta Anak Perempuan : {int(bagianharta_anak_pr)}")
            # pembagian harta per anak perempuan
            k = 1
            while k <= anak_pr:
                print("Harta Untuk Anak Perempuan ",
                      k, " = ", sisa_harta_anak_pr)
                k += 1
        elif (anak_lk > 0 and anak_pr == 0):
            asalmasalah_anaklk = (1 * anak_lk)
            asalmasalah_sisa = asalmasalah_anaklk
            sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
            print(f"Sisa Harta : {int(sisa_harta)}")
            suku_bagian = sisa_harta / asalmasalah_sisa
            sisa_harta_anak_lk = (1 * suku_bagian)
            bagianharta_anak_lk = sisa_harta_anak_lk * anak_lk
            print(f"Harta Anak Laki-Laki : {int(bagianharta_anak_lk)}")
            # pembagian harta per anak laki-laki
            j = 1
            while j <= anak_lk:
                print("Harta Untuk Anak Laki - Laki ",
                      j, " = ", sisa_harta_anak_lk)
                j += 1
        elif (anak_lk > 0 and anak_lk > 0):
            asalmasalah_anaklk = (2 * anak_lk)
            asalmasalah_anakpr = (1 * anak_pr)
            asalmasalah_sisa = asalmasalah_anaklk + asalmasalah_anakpr
            sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
            print(f"Sisa Harta : {int(sisa_harta)}")
            suku_bagian = sisa_harta / asalmasalah_sisa
            sisa_harta_anak_pr = (1 * suku_bagian)
            sisa_harta_anak_lk = (2 * suku_bagian)
            bagianharta_anak_pr = sisa_harta_anak_pr * anak_pr
            bagianharta_anak_lk = sisa_harta_anak_lk * anak_lk
            print(f"Harta Anak Perempuan : {int(bagianharta_anak_pr)}")
            print(f"Harta Anak Laki-Laki : {int(bagianharta_anak_lk)}")
            # pembagian harta per anak perempuan
            i = 1
            while i <= anak_pr:
                print("Harta Untuk Anak Perempuan ",
                      i, " = ", sisa_harta_anak_pr)
                i += 1
            # pembagian harta per anak laki-laki
            j = 1
            while j <= anak_lk:
                print("Harta Untuk Anak Laki - Laki ",
                      j, " = ", sisa_harta_anak_lk)
                j += 1
elif (jumlahasalmasalah > asalmasalah):
    print(f"Jumlah Siham : {int(totalasalmasalah)}")
    print(f"Asal Masalah Sisa: {int(sisa)}")
    sisa_harta = 0
    print(f"Jumlah asal masalah : {int(jumlahasalmasalah)}")
    suku_bagian = harta / jumlahasalmasalah
    print("Suku Bagian : ", suku_bagian)
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
    # penghitungan bagian ayah / kakek
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
    finalbagiananakpr = (asalmasalah_anakpr * suku_bagian)
    print("=" * 20)
    print(f"Asal Masalah Awal : {int(asalmasalah)}")
    print(f"Jumlah Siham Menjadi : {int(jumlahasalmasalah)}")
    if (suami == "y"):
        print(f"Bagian Harta Suami : {int(finalbagiansuami)}")
    else:
        # tampil bagian istri jika lebih 1 harta per istri
        if (istri > 1):
            bagi_harta_istri = finalbagianistri / istri
            print(f"Bagian Harta Istri : {int(finalbagianistri)}")
            j = 1
            while j <= istri:
                print("Harta Untuk Istri Ke- ",
                        j, " = ", bagi_harta_istri)
                j += 1
        else:
            if (istri != 0):
                print(f"Bagian Harta Istri : {int(finalbagianistri)}")
    if (bagianayah == 0.16 and bagiansisa == "+sisa"):
        print(f"Bagian Harta Ayah 1/6 + sisa: {int(finalbagianayah)} + {int(sisa_harta)}")
        print(f"Harta untuk ayah =  {int(finalbagianayah + sisa_harta)}")
    else:
        print(f"Bagian Harta Ayah sini : {int(finalbagianayah)}")
    print(f"Bagian Harta Ibu : {int(finalbagianibu)}")
    if (anak_pr > 0 and anak_lk == 0):
        asalmasalah_anakpr = (1 * anak_pr)
        asalmasalah_sisa = asalmasalah_anakpr
        # batas ambil bagian suami / istri
        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
        print(f"Sisa Harta : {int(sisa_harta)}")
        suku_bagian = sisa_harta / asalmasalah_sisa
        sisa_harta_anak_pr = (1 * suku_bagian)
        bagianharta_anak_pr = sisa_harta_anak_pr * anak_pr
        print(f"Harta Anak Perempuan : {int(bagianharta_anak_pr)}")
        # pembagian harta per anak perempuan
        k = 1
        while k <= anak_pr:
            print("Harta Untuk Anak Perempuan ",
                    k, " = ", sisa_harta_anak_pr)
            k += 1
    elif (anak_lk > 0 and anak_pr == 0):
        asalmasalah_anaklk = (1 * anak_lk)
        asalmasalah_sisa = asalmasalah_anaklk
        # batas ambil bagian suami / istri
        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
        print(f"Sisa Harta : {int(sisa_harta)}")
        suku_bagian = sisa_harta / asalmasalah_sisa
        sisa_harta_anak_lk = (1 * suku_bagian)
        bagianharta_anak_lk = sisa_harta_anak_lk * anak_lk
        print(f"Harta Anak Laki-Laki : {int(bagianharta_anak_lk)}")
        # pembagian harta per anak laki-laki
        j = 1
        while j <= anak_lk:
            print("Harta Untuk Anak Laki - Laki ",
                    j, " = ", sisa_harta_anak_lk)
            j += 1
    elif (anak_lk > 0 and anak_lk > 0):
        asalmasalah_anaklk = (2 * anak_lk)
        asalmasalah_anakpr = (1 * anak_pr)
        asalmasalah_sisa = asalmasalah_anaklk + asalmasalah_anakpr
        # ambil bagian suami jika ada jika tidak ada ambil bagian istri
        if (suami == "y"):
            ambil_bagian_harta = finalbagiansuami
        else:
            ambil_bagian_harta = finalbagianistri
        # batas ambil bagian suami / istri
        sisa_harta = harta - ambil_bagian_harta - finalbagianayah - finalbagianibu
        print(f"Sisa Harta : {int(sisa_harta)}")
        suku_bagian = sisa_harta / asalmasalah_sisa
        sisa_harta_anak_pr = (1 * suku_bagian)
        sisa_harta_anak_lk = (2 * suku_bagian)
        bagianharta_anak_pr = sisa_harta_anak_pr * anak_pr
        bagianharta_anak_lk = sisa_harta_anak_lk * anak_lk
        print(f"Harta Anak Perempuan : {int(bagianharta_anak_pr)}")
        print(f"Harta Anak Laki-Laki : {int(bagianharta_anak_lk)}")
        # pembagian harta per anak perempuan
        i = 1
        while i <= anak_pr:
            print("Harta Untuk Anak Perempuan ",
                    i, " = ", sisa_harta_anak_pr)
            i += 1
        # pembagian harta per anak laki-laki
        j = 1
        while j <= anak_lk:
            print("Harta Untuk Anak Laki - Laki ",
                    j, " = ", sisa_harta_anak_lk)
            j += 1
elif (jumlahasalmasalah < asalmasalah):
    print(f"Jumlah Siham : {int(totalasalmasalah)}")
    # antisipasi Zero division error
    # hitung harta suami/istri
    if (suami == "y"):
        suku_bagian = harta / jumlahasalmasalah
        if (asalmasalah_suami == 0):
            finalbagiansuami = 0
            ambil_bagian_harta = finalbagiansuami
        else:
            if(ayah == "0" and ibu == "0" and kakek == 0 and nenek == 0):
                suku_bagian = harta / totalasalmasalah
                finalbagiansuami = asalmasalah_suami * suku_bagian
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
            if(ayah == "0" and anak_pr == 1 and ibu == "y"):
                asalmasalah_sisa = asalmasalah_ibu + asalmasalah_anakpr
                sisa_harta = harta - ambil_bagian_harta
                finalbagianibu = (sisa_harta * asalmasalah_ibu) / int(asalmasalah_sisa)
            elif(ayah == "0" and anak_pr > 1 and ibu == "y"):
                asalmasalah_sisa = asalmasalah_ibu + asalmasalah_anakpr
                sisa_harta = harta - ambil_bagian_harta
                finalbagianibu = (sisa_harta * asalmasalah_ibu) / int(asalmasalah_sisa)
            else:
                finalbagianibu = suku_bagian * asalmasalah_ibu
    # hitung harta anak perempuan  
    finalbagiananakpr = asalmasalah_anakpr * suku_bagian
    # hitung harta ayah
    if (asalmasalah_ayah == 0):
        finalbagianayah = 0
    else:
        if (bagianayah == "sisa" and bagiansisa == ""):
            finalbagianayah = suku_bagian * asalmasalah_ayah
            sisa_harta = harta - ambil_bagian_harta - \
                finalbagianibu - finalbagiananakpr - finalbagianayah
            # suku_bagian = sisa_harta / asalmasalah_sisa
            print("=" * 25)
            print("Masuk kondisi sisa ayah asal masalah sisa ", asalmasalah_sisa)
            print("Masuk kondisi sisa ayah suku bagian ", suku_bagian)
            print("Masuk kondisi sisa ayah sisa harta ", sisa_harta)
        elif (bagianayah == 0.16 and bagiansisa == "+sisa"):
            asalmasalah_sisa = sisa
            finalbagianayah = suku_bagian * asalmasalah_ayah
            print("=" * 25)
        else:
            finalbagianayah = suku_bagian * asalmasalah_ayah
    print("=" * 20)
    if(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
        if(ayah == "0" and ibu == "y"):
            sisa_harta = harta - finalbagianibu - ambil_bagian_harta
        else :
            sisa_harta = harta - finalbagianayah - finalbagianibu - \
            finalbagiananakpr - ambil_bagian_harta
    else:
        if(ayah == "0" and ibu == "y"):
            sisa_harta = harta - ambil_bagian_harta - finalbagianibu
        else :
            sisa_harta = harta - finalbagianayah - finalbagianibu - \
            finalbagiananakpr - ambil_bagian_harta
    if(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
        print(f"Asal Masalah Awal : {int(asalmasalah)}")
        print(f"Jumlah Siham Menjadi : {int(jumlahasalmasalah)}")
        print(f"Asal Masalah Sisa : {int(asalmasalah - jumlahasalmasalah)}")
    else :
        print(f"Asal Masalah Sisa : {int(sisa)}")
        print(f"Sisa Harta : {int(sisa_harta)}")
    if (suami == "y"):
            print(f"Bagian Harta Suami : {int(finalbagiansuami)}")
    else:
        # tampil bagian istri jika lebih 1 harta per istri
        if (istri > 1):
            bagi_harta_istri = finalbagianistri / istri
            print(f"Bagian Harta Istri : {int(finalbagianistri)}")
            j = 1
            while j <= istri:
                print("Harta Untuk Istri Ke- ",
                        j, " = ", bagi_harta_istri)
                j += 1
        else:
            if (istri != 0):
                print(f"Bagian Harta Istri : {int(finalbagianistri)}")
    if (bagianayah == 0.16 and bagiansisa == "+sisa"):
        print(
            f"Bagian Harta Ayah 1/6 + sisa: {int(finalbagianayah)} + {int(sisa_harta)}")
        print(f"Harta untuk ayah =  {int(finalbagianayah + sisa_harta)}")
    else:
        print(f"Bagian Harta Ayah : {int(finalbagianayah)}")
    print(f"Bagian Harta Ibu : {int(finalbagianibu)}")
    if (anak_pr > 1):
        if(pewaris == "istri" or pewaris == "Istri" or pewaris == "ISTRI" or pewaris == "2"):
            if(ayah == "0" and ibu == "0"):
                sisa_harta = harta - ambil_bagian_harta
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
        else:
            sisa_harta = harta - ambil_bagian_harta
            if(ayah == "0" and ibu == "0"):
                suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
            elif(ayah == "0" and ibu == "y"):
                asalmasalah_sisa = asalmasalah_anakpr + asalmasalah_ibu
                suku_bagian_sisa = sisa_harta / asalmasalah_sisa
                finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr
        print(f"Bagian Harta Anak Perempuan : {int(finalbagiananakpr)}")
        sisa_harta_anak_pr = finalbagiananakpr / anak_pr
        # pembagian harta per anak perempuan
        i = 1
        while i <= anak_pr:
            print("Harta Untuk Anak Perempuan ", i, " = ", sisa_harta_anak_pr)
            i += 1
    elif (anak_pr == 1):
        if(ayah == "0" and ibu == "0"):
            sisa_harta = harta - ambil_bagian_harta
            suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
            finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr 
        elif(ayah == "0" and ibu == "y"):
            sisa_harta = harta - ambil_bagian_harta - finalbagianibu
            suku_bagian_sisa = sisa_harta / asalmasalah_anakpr
            finalbagiananakpr = suku_bagian_sisa * asalmasalah_anakpr 
        print(f"Bagian Harta Anak Perempuan : {int(finalbagiananakpr)}")
