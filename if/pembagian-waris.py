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