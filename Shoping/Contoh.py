ShoppingCart(object):
    # Membuat shopping cart objek
    keranjang = []

    def __init__(self, nama_pembeli):
        # menambah variabel nama_pembeli pada class ShoppingCart
        self.nama_pembeli = nama_pembeli

    def tambah_item(self, produk, harga, jumlah):
        # membuat dictionary untuk menampung data belanjaan
        item = {}
        item["produk"] = produk
        item["harga"] = harga
        item["jumlah"] = jumlah
        item["total"] = jumlah * harga

        # Menambahkan dictionary belanjaan ke keranjang
        self.keranjang.append(item)

    def hapus_item(self, produk):
        i = 0
        # mencari nama produk pada keranjang
        for belanjaan in self.keranjang:
            if(belanjaan["produk"] == produk):
                # hapus data belanjaan di keranjang sesuai nama produk
                del self.keranjang[i]

    def tampil_keranjang(self):
        total_belanja = 0
        print("\nDetail Keranjang")
        print("------------------------")
        print("Pembeli : ", self.nama_pembeli)
        print("Keranjang Belanjaan")
        for belanjaan in self.keranjang:
            total_belanja += belanjaan["total"]
            for x, y in belanjaan.items():
                print(x, ":", y)
        print("Total Belanja : ", total_belanja)


# membuat objek shopping cart
keranjang_ku = ShoppingCart("Juragan")

# menambahkan data ke variabel keranjang pada objek keranjang_ku
keranjang_ku.tambah_item("Laptop Acer", 1200, 2)
keranjang_ku.tambah_item("Monitor LG 19inch", 1500, 2)

# menampilkan data keranjang
keranjang_ku.tampil_keranjang()

# menghapus item yang tidak jadi dibeli
keranjang_ku.hapus_item("Laptop Acer")

# menampilkan data keranjang
keranjang_ku.tampil_keranjang()
