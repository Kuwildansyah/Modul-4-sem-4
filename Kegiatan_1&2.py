import getpass

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Kegiatan_1:
    def __init__(self):
        self.data = []
        self.users = []

    def tambahData(self, nim, namaAsisten):
        if nim.startswith("IF"):
            self.data.append({"nim": nim, "nama_asisten": namaAsisten})
            return True
        else:
            return False
   
    def tampil(self):
        if len(self.data) > 0:
            print("\nData Praktikan:")
            for i, d in enumerate(self.data):
                print(f"{i+1}. NIM: {d['nim']}, Nama Asisten: {d['nama_asisten']}")
        else:
            print("\nBelum ada data praktikan yang dimasukkan")

    def listNimPraktikan(self):
        if len(self.data) > 0:
            print("\nList NIM Praktikan:")
            for d in self.data:
                print(d['nim'])
        else:
            print("\nBelum ada data praktikan yang dimasukkan")
 
    def listNamaAsisten(self):
        if len(self.data) > 0:
            print("\nList Nama Asisten:")
            for d in self.data:
                print(d['nama_asisten'])
        else:
            print("\nBelum ada data praktikan yang dimasukkan")

    def hapusData(self, nim, namaAsisten):
        for d in self.data:
            if d['nim'] == nim and d['nama_asisten'] == namaAsisten:
                self.data.remove(d)
                return True
        return False
    def editData(self, nim, nama_asisten_baru):
        for d in self.data:
            if d['nim'] == nim:
                d['nama_asisten'] = nama_asisten_baru
                print("Data berhasil diubah")
                return True
        print("Data tidak ditemukan")
        return False
        


    def sign_up(self):
        print("=== Sign Up ===")
        username = input("Enter username: ")
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")

        if password == confirm_password:
            user = User(username, password)
            self.users.append(user)
            print("Sign up successful!")
        else:
            print("Passwords do not match, please try again.")

    def login(self):
        print("=== Login ===")
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in self.users:
            if user.username == username and user.password == password:
                print("Login successful!")
                return True

        print("Invalid username or password.")
        return False

Kegiatan_1 = Kegiatan_1()
logged_in = False

while not logged_in:
    print("=== Halo Bujang ===")
    print("1. Sign Up")
    print("2. Login")

    choice = int(input("Masukkan Pilihan: "))

    if choice == 1:
        Kegiatan_1.sign_up()
    elif choice == 2:
        logged_in = Kegiatan_1.login()
    else:
        print("salah input bro, input yang bener")


if logged_in:
    data = Kegiatan_1

    print("Program Data Praktikan")
    print("======================")

    choice = 0
    while choice != 7:
        print("\nMenu:")
        print("1. Tambah data")
        print("2. Tampilkan semua data")
        print("3. Tampilkan semua NIM praktikan")
        print("4. Tampilkan semua nama asisten")
        print("5. Hapus data")
        print("6. Edit data")
        print("7. Keluar")

        choice = int(input("\nPilihan anda: "))


        if choice == 1:
            nim = input("\nMasukkan NIM praktikan (dengan prefix 'IF'): ")
            nama_asisten = input("Masukkan nama asisten: ")
            if data.tambahData(nim, nama_asisten):
                print("Data berhasil ditambahkan")
            else:
                print("Data gagal ditambahkan")

        elif choice == 2:
            data.tampil()

        elif choice == 3:
            data.listNimPraktikan()

        elif choice == 4:
            data.listNamaAsisten()

        elif choice == 5:
            nim = input("\nMasukkan NIM praktikan yang akan dihapus: ")
            nama_asisten = input("Masukkan nama asisten yang akan dihapus: ")
            if data.hapusData(nim, nama_asisten):
                print("Data berhasil dihapus")
            else:
                print("Data gagal dihapus")

        elif choice == 6:
            nim = input("\nMasukkan NIM praktikan yang akan diedit: ")
            nama_asisten = input("Masukkan nama asisten baru: ")
            if data.editData(nim, nama_asisten):
                print("Data berhasil diedit")
            else:
                print("Data gagal diedit")

        elif choice == 7:
            print("\nTerima kasih telah menggunakan program ini")

        else:
            print("\nPilihan tidak valid, silahkan coba lagi")
