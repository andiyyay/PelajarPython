def salam():
    print("hello x pplg")
salam()

def coba():
    print("aku andiya")
coba()

def test():
    print("sekolah di smk bpi")
test()

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
#pemanggilan fungsi
print("luas persegi : %d" % luas_persegi(20))

# membuat variabel global
nama = "python"
versi = "1.0.0"
def help():
    #ini variabel lokal
    nama = "c#"
    versi = "1.0.2"
    # mengakses variabel lokal
    print ("nama: %s" % nama)
    print ("versi: %s" % versi)

# memanggil fungsi help()s
help()

def halo_dunia():
    print("halo python! halo dunia")
    #memanggil fungsi
halo_dunia()
