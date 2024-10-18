nama = input(str("masukan nama :"))
jumlah_anak = int(input('jumlah anak :'))
pekerjaan = input(str("pekerjaan : "))
gaji_perbulan =str(input("gaji_perbulan : "))
zakat_presentase = float(input("zakat presentase : "))
nisab = int(input("nisab : "))

#jumlah gaji perbulan dikali zakat presentase
gaji_perbulan = 100000
zakat_presentase = 25
zakat = input(str(gaji_perbulan * zakat_presentase))
print(zakat)

#pembanding nisab kurang lebih gaji perbulan
gaji_perbulan = 100000
nisab = True
zakat_presentase = True
hasil = 'boleh zakat ' if(gaji_perbulan >= 900000)and nisab >= True and zakat_presentase== True else" tidak boleh zakat"
print(hasil)