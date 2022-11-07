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
bagiansaudariknd = ""
bagiansaudaraknd = ""
masuk = ""
hitung = ""

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
print("=" * 50)