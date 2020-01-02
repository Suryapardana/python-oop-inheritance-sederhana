print("simple program example\n")
class tes():
    def __init__(self,nama,lawan,serangan,pertahanan,darah):
        self.nama = nama
        self.lawan = lawan
        self.serangan = serangan
        self.pertahanan = pertahanan
        self.darah = darah

    def serang(self,serangan):
        print(self.nama,"menyerang",self.lawan)
        dmg = self.serangan//self.pertahanan
        print(dmg,"damage yang di keluarkan")

    def diserang(self,pertahan):
        print(self.nama,"diserang",self.lawan)
        dmg = self.serangan//self.pertahanan
        print(dmg," damage diterima")
        print("darah tersisa",self.darah-dmg)

python = tes("python","cobra",80,10,100)
cobra = tes("cobra","python",85,5,100)

python.serang(cobra)
print("\n")
cobra.diserang(python)
