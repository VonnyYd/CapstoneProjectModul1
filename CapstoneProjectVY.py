# Import Library Date Utk Tanggal Terupdate
import datetime



# Mengatur Format Nama, Agar Dapat Capitalize Di Setiap Index Katanya
def FormatNama(Nama):
    SusunanNama = Nama.split(" ") # Setiap Kata Yang Dimasukkan Dispare Berdasarkan Spasi
    OutputNama = ""
    for Kata in (SusunanNama): # Menyatakan Index Di Setiap Katanya
        Kata = Kata.capitalize() # Membuat Capital Di Setiap Katanya
        OutputNama = OutputNama + Kata + " " # Digabungkan Kembali Menjadi Kesatuan Nama Lengkap 
    return OutputNama



# Membuat Database Dalam Bentuk Dictionary
ListData = [
    {
        'tanggal terupdate' : "15/02/2023",  
        'no absen': 130223015,
        'nama lengkap': 'Eka Safitri',
        'jenis kelamin' : 'P',
        'nilai akhir' : 80,
    },
    {
        'tanggal terupdate' : "17/02/2023", 
        'no absen': 130223018,
        'nama lengkap': 'Brony Karim ',
        'jenis kelamin' : 'L',
        'nilai akhir' : 82,
    },
    {
        'tanggal terupdate' : "16/02/2023", 
        'no absen': 130223020,
        'nama lengkap': 'Charsey Putri',
        'jenis kelamin' : 'P',
        'nilai akhir' : 75,
    },
    {
        'tanggal terupdate' : "17/02/2023", 
        'no absen': 130223011,
        'nama lengkap': 'Andyka Fang',
        'jenis kelamin' : 'L',
        'nilai akhir' : 92,
    },
    {
        'tanggal terupdate' : "15/02/2023", 
        'no absen': 130223008,
        'nama lengkap': 'Dea Febilia',
        'jenis kelamin' : 'P',
        'nilai akhir' : 78,
    }
]



# Membuat Variable List Inputan
cart = []



# Membangun Rumusan Menu Pilihan 1 (Menampilkan List Data Nilai)
def MenampilkanListData() :
    print('List Database di Administrasi Akademik.\n')
    print('Index\t| Tanggal Terupdate\t| No Absen \t| Nama Lengkap\t\t| Jenis Kelamin\t| Nilai Akhir')
    for i in range(len(ListData)) :
        print('{}\t| {}\t\t| {}\t| {}\t\t| {}\t\t| {}'.format(i,ListData[i]['tanggal terupdate'],ListData[i]['no absen'],ListData[i]['nama lengkap'],ListData[i]['jenis kelamin'],ListData[i]['nilai akhir']))



# Membangun Rumusan Menu Pilihan 2 (Menambahkan List Data Nilai)
def MenambahkanListData() :
    TodayDate = datetime.datetime.now() # datetime yg pertama utk memanggil Library & yg kedua utk Functionnya
    TodayDate = TodayDate.strftime("%d/%m/%Y") # Menyusun Format Tanggal Yang Akan Ditampilkan

    NoAbsen = input('Masukkan No Absen Murid (130223xxx) : ')
    InputAneh = False 
    while(InputAneh == False):
        if(NoAbsen.isnumeric() == False): # Jika Inputnya Bukan Angka
            NoAbsen = input('Masukkan Angka yaa ... Masukkan Lagi Di Sini : ')
        else:
            InputAneh = True # Jika Inputnya Benar Angka, Maka Ngikutin Rumus Di Atas Lagi
    NoAbsen = int(NoAbsen)

    for Data in ListData: # Rumus Untuk Prim Key Data Duplicate  
        if(Data['no absen'] == NoAbsen):
            print("Datanya Sudah Ada.")
            return

    NamaLengkap = input('Masukkan Nama Lengkap Murid : ')
    NamaLengkap = FormatNama(NamaLengkap) # Memanggil Rumus Pengaturan Format Nama Lengkap Di Atas

    JenisKelamin = input('Masukkan Jenis Kelamin Murid (P/L) : ').upper()
    JenisKelaminAneh = False
    while(JenisKelaminAneh == False) : 
        if (JenisKelamin != "P" and JenisKelamin != "L"): # Jika Yang Diisi Bukan P Atau L, Maka Perlu Input Ulang
            JenisKelamin = input("Jenis Kelamin Salah. Silahkan Ketik Ulang : ").upper()
        else :
            JenisKelaminAneh = True
        
    NilaiAkhir = int(input('Masukkan Nilai Akhir : '))
    Konfirmasi = input("Apakah Anda Yakin Ingin Menambah Data Ini (Y/N) ?  ")
    if (Konfirmasi == "y" or Konfirmasi == "Y"):
        ListData.append({
            'no absen': NoAbsen,
            'nama lengkap': NamaLengkap,
            'jenis kelamin' : JenisKelamin,
            'tanggal terupdate' : TodayDate,
            'nilai akhir': NilaiAkhir,
        })
    else:
        print("Data Batal Disimpan.")
    MenampilkanListData()



# Membangun Rumusan Menu Pilihan 3 (Menghapus List Data Nilai)
def MenghapuskanListData() :
    MenampilkanListData()
    IndexData = input('Masukkan No Index Data Yang Ingin Dihapus : ')
    IndexDataAneh = False
    while(IndexDataAneh == False):
        if(IndexData.isnumeric() == False):
            IndexData = input('Masukkan Angka Index Yang Tepat Di Sini : ')
        else:
            IndexDataAneh = True
    IndexData = int(IndexData)
    if (IndexData > len(ListData) or IndexData < 0):
        print("Data tidak ditemukan")
        return
    else:
        del ListData[IndexData]
    MenampilkanListData()



# Membangun Rumusan Menu Pilihan 4 (Mengedit List Data Nilai)
def MengubahListData() :
    MenampilkanListData()
    NoAbsen = input('Masukkan No Absen Murid yang ingin diubah (130223xxx) : ')
    InputAneh = False
    while(InputAneh == False):
        if(NoAbsen.isnumeric() == False):
            NoAbsen = input('Masukkan Angka yaa ... Masukkan Lagi Di Sini : ')
        else:
            InputAneh = True
    NoAbsen = int(NoAbsen)

    Counter = 0 # Membangun Variable Untuk Pengecekan Apakah Datanya Ada Dalam List Database Kita

    for Data in ListData:
        if(Data['no absen'] == NoAbsen):
            TodayDate = datetime.datetime.now()
            TodayDate = TodayDate.strftime("%d/%m/%Y")
        
            NamaLengkap = input('Masukkan Nama Lengkap Murid : ')
            NamaLengkap = FormatNama(NamaLengkap) 

            JenisKelamin = input('Masukkan Jenis Kelamin Murid (P/L) : ').upper()
            JenisKelaminAneh = False
            while(JenisKelaminAneh == False) : 
                if (JenisKelamin != "P" and JenisKelamin != "L"):
                    JenisKelamin = input("Jenis Kelamin Salah. Silahkan Ketik Ulang : ").upper()
                else :
                    JenisKelaminAneh = True

            NilaiAkhir = int(input('Masukkan Nilai Akhir : '))
            Konfirmasi = input("Apakah Anda Yakin Dengan Data Perubahannya (Y/N) ?  ")
            if (Konfirmasi == "y" or Konfirmasi == "Y"):
                Data['tanggal terupdate'] = TodayDate
                Data['nama lengkap'] = NamaLengkap
                Data['jenis kelamin'] = JenisKelamin
                Data['nilai akhir'] = NilaiAkhir
                Counter += 1
                break
            else:
                print("Data Batal Disimpan.")
    if(Counter == 0):
        print("Data Tidak Ditemukan.")
    MenampilkanListData()



while True :
    pilihanMenu = input('''

        Selamat Datang di Administrasi Akademik

        Daftar Pilihan:
        1. Menampilkan List Data Nilai
        2. Menambahkan List Data Nilai
        3. Menghapus List Data Nilai
        4. Mengedit List Data Nilai
        5. Exit Program

        Masukkan Angka Daftar Yang Dibutuhkan : ''')

    if(pilihanMenu == '1') :
        MenampilkanListData()
    elif(pilihanMenu == '2') :
        MenambahkanListData()
    elif(pilihanMenu == '3') :
        MenghapuskanListData()
    elif(pilihanMenu == '4') :
        MengubahListData()
    elif(pilihanMenu == '5') :
        break
    else:
        print('Masukkan Angka Pilihan Menu Yang Benar!')  
    

