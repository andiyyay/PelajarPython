def kali(a,b):
    c= a*b
    return (c)

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

def selamat_datang (nama):
    print(f'halo {nama}, selamat datang!')

selamat_datang('haechan')
selamat_datang('jeno')
selamat_datang('jaemin')
selamat_datang('mark')
selamat_datang('jisung')
selamat_datang('renjun')
selamat_datang('chenle')

def fluar ():
    def fdalam():
        print('fdalam() dipanggil')
#perintah fungsi untuk fluar()
        print ('fluar() dipanggil')
    #memanggil fungsi fdalam()
    fdalam()
fluar()

def outer_function(siapa):
    def inner_function():
        print(f"hello,{siapa}")
    inner_function()
outer_function("albi ganteng")

# outside function
def outer():
    message = 'local'
    # nested function
    def inner():
        # declare nonlacal variable
        nonlocal message
        message = 'nonlocal'
        print ("inner:", message)
    inner()
    print("outer:", message)
outer()
def f(n):
    import time
    if n == 0:
        print ("go!")
        return
    print(n, end='')
    time.sleep(1)
    f(n-1)
f(3)
f(5)
def faktorial (n):
    if n == 0: return 1
    return n * faktorial(n-1)

def main():
    n = int(input("masukan bilangan bulat : "))
    print ('%d! = %d' % (n, faktorial(n)))
if __name__ == '__main__':
    main()

    x = 1
    print(eval('x + 5'))

    program = 'a = 5\nb=10\nprint("Sum =", a+b)'
    exec(program)

    # get an entire program as input
    program = input('Enter a program: ')

    # execute the program
    exec(program)

    # nama file: mymodule.py

    # mendefinisikan variabel
    x = 100


    # mendefinisikan fungsi
    def kali(a, b):
        return a * b


    haechan = "ganteng"


    def tambah(angka1, angka2, angka3):
        return angka1 + angka2 + angka3

#nama file: mymodule.py

#mendefinisikan variabel
x = 100

#mendefinisikan fungsi
def kali (a,b):
    return a * b

haechan = "ganteng"

def tambah(angka1,angka2,angka3):
    return angka1 + angka2 + angka3

import modul

#mengakses variabel
# print(modul.x)
#
# #mengakses fungsi
# hasil = modul.kali(2,3)
# print(hasil)
#
# print(modul.haechan)
#
# hasil = modul.tambah(3,4,5)
# print(hasil)
from modul import x, kali, haechan, tambah
print(x)
print(kali(2,3))
print(haechan)
print(tambah(3,4,5))

x = 1
print(eval('x + 5'))

program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

# get an entire program as input
program = input('Enter a program: ')

# execute the program
exec(program)