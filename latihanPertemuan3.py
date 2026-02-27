class Person():
    def __init__(self, nama, gender, umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur

class Karyawaan(Person):
    def __init__(self, nama, gender, umur, gaji):
        Person.__init__(self, nama, gender, umur)
        self.__gaji = gaji
    def getGaji(self):
        return self.__gaji
    def setGaji(self, gaji):
        self.__gaji = gaji

class Rekening(Person):
    def __init__(self, nama, gender, umur, id, pin):
        Person.__init__(self, nama, gender, umur)
        self.id = id
        self.__pin = pin
    def getPin(self):
        return self.__pin
    def setPin(self, pin):
        self.__pin = pin

Karyawaan1 = Karyawaan("Iann From the start", "Lakilaki", 18, 20000000)
Karyawaan2 = Person("Angga Let Down", "Lakilaki", 18)
Karyawaan3 = Rekening("Pacerul Multo", "Lakilaki", 18, 25071207786, "Afgan321")
Karyawaan4 = Karyawaan("Vybii Diet Mountain Dew","Lakilaki", 18, 1000000000000000)

Karyawaan4.setGaji(0)

print(f"Gaji {Karyawaan4.nama} adalah: {Karyawaan4.getGaji()} rupiah :p")
print(f"Gaji {Karyawaan1.nama} adalah: {Karyawaan1.getGaji()} rupiah >v<")
print(f"No Rekening {Karyawaan3.nama} adalah {Karyawaan3.id}")
print(f"Umur {Karyawaan2.nama} adalah {Karyawaan2.umur} tahun")

        