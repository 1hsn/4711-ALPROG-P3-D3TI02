import datetime as dt
print("Untuk mengetahui informasi umur anda. \nMasukkan tanggal, bulan, dan tahun lahir anda :")

tanggal = int(input('Tanggal \t: ',))
bulan = int(input('Bulan \t\t: ',))
tahun = int(input('Tahun \t\t: ',))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
hari_ini = dt.date.today()

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365;
umur_bulan = (umur_hari.days % 365) // 30

print(f"Umur Anda \t: {umur_tahun} tahun, {umur_bulan} bulan, {umur_hari.days} hari")